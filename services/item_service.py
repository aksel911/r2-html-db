from typing import List, Dict, Optional, Tuple
from os.path import splitext
from functools import lru_cache
from flask import current_app

from models.item import (DT_Item, DT_ItemResource, TblSpecificProcItem, DT_ItemAbnormalResist,
DT_Bead, DT_ItemBeadModule, TblBeadHoleProb, DT_ItemAttributeAdd, 
DT_ItemAttributeResist, DT_ItemProtect, DT_ItemSlain, DT_ItemPanalty)

from services.database import execute_query, get_db_connection
from services.utils import get_skill_icon_path, clean_description, get_google_sheets_data
from config.settings import ATTRIBUTE_TYPE_WEAPON_URL, ATTRIBUTE_TYPE_ARMOR_URL


def apply_filters(items, filters):
    """Оптимизированная функция применения фильтров"""
    if not items or not filters:
        return items

    # Удаляем пустые фильтры для оптимизации
    filters = {k: v for k, v in filters.items() if v and k != ''}
    if not filters:
        return items

    # Преобразуем списки один раз
    filtered_items = list(items)

    try:
        # Числовые фильтры основные
        if type_filter := filters.get('typeFilter'):
            type_val = int(type_filter)
            filtered_items = [item for item in filtered_items if item.IType == type_val]

        if filters.get('levelMin') or filters.get('levelMax'):
            level_min = int(filters.get('levelMin', 0))
            level_max = int(filters.get('levelMax', 999999))
            filtered_items = [item for item in filtered_items if level_min <= item.ILevel <= level_max]

        if filters.get('weightMin') or filters.get('weightMax'):
            weight_min = float(filters.get('weightMin', 0))
            weight_max = float(filters.get('weightMax', 999999))
            filtered_items = [item for item in filtered_items if weight_min <= item.IWeight <= weight_max]

        # Булевы фильтры (оптимизировано)
        bool_fields = {
            'stackableFilter': ('IMaxStack', lambda x: int(x) if x in ['0', '1'] else None),
            'eventItemFilter': ('IIsEvent', lambda x: bool(int(x))),
            'testItemFilter': ('IIsTest', lambda x: bool(int(x))),
            'indictFilter': ('IIsIndict', lambda x: bool(int(x))),
            'chargeFilter': ('IIsCharge', lambda x: bool(int(x))),
            'partyDropFilter': ('IIsPartyDrop', lambda x: bool(int(x)))
        }

        for filter_name, (attr, converter) in bool_fields.items():
            if filter_val := filters.get(filter_name):
                val = converter(filter_val)
                if val is not None:
                    filtered_items = [item for item in filtered_items if getattr(item, attr) == val]

        # Числовые фильтры дополнительные (оптимизировано)
        numeric_fields = {
            'IDHIT', 'IDDD', 'IRHIT', 'IRDD', 'IMHIT', 'IMDD',
            'IHPPlus', 'IMPPlus', 'ISTR', 'IDEX', 'IINT',
            'IHPRegen', 'IMPRegen', 'IAttackRate', 'IMoveRate', 'ICritical'
        }

        for field in numeric_fields:
            min_key = f"{field}Min"
            max_key = f"{field}Max"
            
            if filters.get(min_key) or filters.get(max_key):
                min_val = float(filters.get(min_key, 0))
                max_val = float(filters.get(max_key, 999999))
                filtered_items = [item for item in filtered_items 
                                if min_val <= float(getattr(item, field, 0) or 0) <= max_val]

        # Квест
        if quest_no := filters.get('questNoFilter'):
            quest_val = int(quest_no)
            filtered_items = [item for item in filtered_items if item.IQuestNo == quest_val]

    except (ValueError, AttributeError) as e:
        print(f"Error applying filters: {e}")
        return items

    return filtered_items




def item_to_dict(item):
    """Конвертирует объект DT_Item в словарь со всеми возможными атрибутами, оптимизировано"""
    attributes = {
        'IID', 'IName', 'IType', 'ILevel', 'IDHIT', 'IDDD', 'IRHIT', 'IRDD', 'IMHIT', 'IMDD',
        'IHPPlus', 'IMPPlus', 'ISTR', 'IDEX', 'IINT', 'IMaxStack', 'IWeight', 'IUseType', 'IUseNum',
        'IRecycle', 'IHPRegen', 'IMPRegen', 'IAttackRate', 'IMoveRate', 'ICritical', 'ITermOfValidity',
        'ITermOfValidityMi', 'IDesc', 'IStatus', 'IFakeID', 'IFakeName', 'IUseMsg', 'IRange', 'IUseClass',
        'IDropEffect', 'IUseLevel', 'IUseEternal', 'IUseDelay', 'IUseInAttack', 'IIsEvent', 'IIsIndict',
        'IAddWeight', 'ISubType', 'IIsCharge', 'INationOp', 'IPShopItemType', 'IQuestNo', 'IIsTest',
        'IQuestNeedCnt', 'IContentsLv', 'IIsConfirm', 'IIsSealable', 'IAddDDWhenCritical', 'mSealRemovalNeedCnt',
        'mIsPracticalPeriod', 'mIsReceiveTown', 'IIsReinforceDestroy', 'IAddPotionRestore',
        'IAddMaxHpWhenTransform', 'IAddMaxMpWhenTransform', 'IAddAttackRateWhenTransform',
        'IAddMoveRateWhenTransform', 'ISupportType', 'ITermOfValidityLv', 'mIsUseableUTGWSvr',
        'IAddShortAttackRange', 'IAddLongAttackRange', 'IWeaponPoisonType', 'IDPV', 'IMPV', 'IRPV',
        'IDDV', 'IMDV', 'IRDV', 'IHDPV', 'IHMPV', 'IHRPV', 'IHDDV', 'IHMDV', 'IHRDV', 'ISubDDWhenCritical',
        'IGetItemFeedback', 'IEnemySubCriticalHit', 'IIsPartyDrop', 'IMaxBeadHoleCount', 'ISubTypeOption',
        'mIsDeleteArenaSvr'
    }

    # Используем __dict__ для получения всех атрибутов объекта
    item_dict = item.__dict__

    # Возвращаем только те атрибуты, которые есть в объекте
    return {attr: item_dict.get(attr, None) for attr in attributes}




#@lru_cache(maxsize=10000)
def get_item_by_id(item_id: int) -> Optional[DT_Item]:
    """Get item by ID with caching"""
    query = """
    SELECT 
        IID, IName, IType, ILevel, IDHIT, IDDD, IRHIT, IRDD, IMHIT, IMDD,
        IHPPlus, IMPPlus, ISTR, IDEX, IINT, IMaxStack, IWeight, IUseType,
        IUseNum, IRecycle, IHPRegen, IMPRegen, IAttackRate, IMoveRate,
        ICritical, ITermOfValidity, ITermOfValidityMi, IDesc, IStatus,
        IFakeID, IFakeName, IUseMsg, IRange, IUseClass, IDropEffect,
        IUseLevel, IUseEternal, IUseDelay, IUseInAttack, IIsEvent,
        IIsIndict, IAddWeight, ISubType, IIsCharge, INationOp,
        IPShopItemType, IQuestNo, IIsTest, IQuestNeedCnt, IContentsLv,
        IIsConfirm, IIsSealable, IAddDDWhenCritical, mSealRemovalNeedCnt,
        mIsPracticalPeriod, mIsReceiveTown, IIsReinforceDestroy,
        IAddPotionRestore, IAddMaxHpWhenTransform, IAddMaxMpWhenTransform,
        IAddAttackRateWhenTransform, IAddMoveRateWhenTransform, ISupportType,
        ITermOfValidityLv, mIsUseableUTGWSvr, IAddShortAttackRange,
        IAddLongAttackRange, IWeaponPoisonType, IDPV, IMPV, IRPV, IDDV,
        IMDV, IRDV, IHDPV, IHMPV, IHRPV, IHDDV, IHMDV, IHRDV,
        ISubDDWhenCritical, IGetItemFeedback, IEnemySubCriticalHit,
        IIsPartyDrop, IMaxBeadHoleCount, ISubTypeOption, mIsDeleteArenaSvr
    FROM DT_Item 
    WHERE IID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_Item(
            IID=row.IID,
            IName=row.IName,
            IType=row.IType,
            ILevel=row.ILevel,
            IDHIT=row.IDHIT,
            IDDD=row.IDDD,
            IRHIT=row.IRHIT,
            IRDD=row.IRDD,
            IMHIT=row.IMHIT,
            IMDD=row.IMDD,
            IHPPlus=row.IHPPlus,
            IMPPlus=row.IMPPlus,
            ISTR=row.ISTR,
            IDEX=row.IDEX,
            IINT=row.IINT,
            IMaxStack=row.IMaxStack,
            IWeight=float(row.IWeight),
            IUseType=row.IUseType,
            IUseNum=row.IUseNum,
            IRecycle=row.IRecycle,
            IHPRegen=row.IHPRegen,
            IMPRegen=row.IMPRegen,
            IAttackRate=row.IAttackRate,
            IMoveRate=row.IMoveRate,
            ICritical=row.ICritical,
            ITermOfValidity=row.ITermOfValidity,
            ITermOfValidityMi=row.ITermOfValidityMi,
            IDesc=row.IDesc.replace('\\n', ' ⭑ ') if row.IDesc else '',
            IStatus=row.IStatus,
            IFakeID=row.IFakeID,
            IFakeName=row.IFakeName,
            IUseMsg=row.IUseMsg,
            IRange=row.IRange,
            IUseClass=row.IUseClass,
            IDropEffect=row.IDropEffect,
            IUseLevel=row.IUseLevel,
            IUseEternal=bool(row.IUseEternal),
            IUseDelay=row.IUseDelay,
            IUseInAttack=bool(row.IUseInAttack),
            IIsEvent=bool(row.IIsEvent),
            IIsIndict=bool(row.IIsIndict),
            IAddWeight=float(row.IAddWeight),
            ISubType=row.ISubType,
            IIsCharge=bool(row.IIsCharge),
            INationOp=row.INationOp,
            IPShopItemType=row.IPShopItemType,
            IQuestNo=row.IQuestNo,
            IIsTest=bool(row.IIsTest),
            IQuestNeedCnt=row.IQuestNeedCnt,
            IContentsLv=row.IContentsLv,
            IIsConfirm=bool(row.IIsConfirm),
            IIsSealable=bool(row.IIsSealable),
            IAddDDWhenCritical=row.IAddDDWhenCritical,
            mSealRemovalNeedCnt=row.mSealRemovalNeedCnt,
            mIsPracticalPeriod=bool(row.mIsPracticalPeriod),
            mIsReceiveTown=bool(row.mIsReceiveTown),
            IIsReinforceDestroy=bool(row.IIsReinforceDestroy),
            IAddPotionRestore=row.IAddPotionRestore,
            IAddMaxHpWhenTransform=row.IAddMaxHpWhenTransform,
            IAddMaxMpWhenTransform=row.IAddMaxMpWhenTransform,
            IAddAttackRateWhenTransform=row.IAddAttackRateWhenTransform,
            IAddMoveRateWhenTransform=row.IAddMoveRateWhenTransform,
            ISupportType=row.ISupportType,
            ITermOfValidityLv=row.ITermOfValidityLv,
            mIsUseableUTGWSvr=bool(row.mIsUseableUTGWSvr),
            IAddShortAttackRange=row.IAddShortAttackRange,
            IAddLongAttackRange=row.IAddLongAttackRange,
            IWeaponPoisonType=row.IWeaponPoisonType,
            IDPV=row.IDPV,
            IMPV=row.IMPV,
            IRPV=row.IRPV,
            IDDV=row.IDDV,
            IMDV=row.IMDV,
            IRDV=row.IRDV,
            IHDPV=row.IHDPV,
            IHMPV=row.IHMPV,
            IHRPV=row.IHRPV,
            IHDDV=row.IHDDV,
            IHMDV=row.IHMDV,
            IHRDV=row.IHRDV,
            ISubDDWhenCritical=row.ISubDDWhenCritical,
            IGetItemFeedback=row.IGetItemFeedback,
            IEnemySubCriticalHit=row.IEnemySubCriticalHit,
            IIsPartyDrop=bool(row.IIsPartyDrop),
            IMaxBeadHoleCount=row.IMaxBeadHoleCount,
            ISubTypeOption=row.ISubTypeOption,
            mIsDeleteArenaSvr=bool(row.mIsDeleteArenaSvr)
        )
    return None

#@lru_cache(maxsize=1000)
def get_item_resource(item_id: int) -> Optional[DT_ItemResource]:
    """Get item resource by ID with caching"""
    query = "SELECT * FROM DT_ItemResource WHERE ROwnerID = ? AND RType = 2"
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemResource(
            row.ROwnerID,
            row.RFileName,
            row.RPosX,
            row.RPosY
        )
    return None

#@lru_cache(maxsize=1000)
def get_item_pic_url(item_id: int):
    item_pic_url = f"{current_app.config['GITHUB_URL']}{item_id.RFileName}_{item_id.RPosX}_{item_id.RPosY}.png"
    return item_pic_url


#@lru_cache(maxsize=1000)
def get_item_model_resource(item_id: int) -> Optional[DT_ItemResource]:
    """Get item resource by ID with caching"""
    query = "SELECT * FROM DT_ItemResource WHERE ROwnerID = ? AND RType = 0"
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemResource(
            row.ROwnerID,
            row.RFileName,
            row.RPosX,
            row.RPosY
        )
    return None


#@lru_cache(maxsize=1000)
def get_specific_proc_item(item_id: int) -> Optional[TblSpecificProcItem]:
    """Get TblSpecificProcItem"""
    query = """
    SELECT
        a.mIID,
        c.IName,
        a.mProcNo,
        b.mProcDesc,
        a.mAParam,
        b.mAParamDesc,
        a.mBParam,
        b.mBParamDesc,
        a.mCParam,
        b.mCParamDesc,
        a.mDParam,
        b.mDParamDesc 
    FROM
        TblSpecificProcItem AS a
    LEFT JOIN TP_SpecificProcItemType AS b ON ( b.mProcNo = a.mProcNo )
    LEFT JOIN DT_Item AS c ON ( c.IID = a.mIID )
        
    WHERE a.mIID = ?
    """
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return TblSpecificProcItem(
            row.mIID,
            row.IName,
            row.mProcNo,
            row.mProcDesc,
            row.mAParam,
            row.mAParamDesc,
            row.mBParam,
            row.mBParamDesc,
            row.mCParam,
            row.mCParamDesc,
            row.mDParam,
            row.mDParamDesc
            )
    return None



def get_items_by_type(item_types: List[int], search_term: str = '') -> Tuple[List[DT_Item], Dict[int, str]]:
    """Generic function to fetch items by type with optional search"""
    # Используем параметризованный запрос для безопасности
    placeholders = ','.join('?' * len(item_types))
    
    query = f"""
    SELECT IID
    FROM DT_ITem
    WHERE IType IN ({placeholders})
    AND IName LIKE ?
    ORDER BY IID
    """
    
    # Создаем список параметров: сначала item_types, затем search_term
    params = item_types + [f'%{search_term}%']
    
    rows = execute_query(query, params)
    item_ids = [row.IID for row in rows]
    
    if not item_ids:
        return [], {}
        
    # Get items and their resources
    items = []
    file_paths = {}
    
    for item_id in item_ids:
        item = get_item_by_id(item_id)
        if item:
            items.append(item)
            
            resource = get_item_resource(item_id)
            if resource:
                file_paths[item_id] = resource.file_path
            else:
                file_paths[item_id] = f"{current_app.config['GITHUB_URL']}no_item_image.png"
                
    return items, file_paths


# DT_ItemAbnormalResist Check
def get_itemabnormalResist_data(item_id: int) -> Optional[List[DT_ItemAbnormalResist]]:
    """Get item resource by MID with caching"""
    query = """
    SELECT DISTINCT
        a.IID,
        b.IName,
        a.AID,
        c.ADesc,
        c1.AType,
        c1.AName AS 'ATypeDesc',
        d1.SID,
        d1.SName,
        v1.mSPID,
        v1.mName,
        v1.mDesc,
        v1.mSpriteFile,
        v1.mSpriteX,
        v1.mSpriteY 
        -- Можно добавить модули:
        --   e1.MID AS 'ModuleID',
        --   e1.MType,
        --   e2.MName AS 'MTypeDesc',
        --   e2.MDesc,
        --   
        --   
        --   e1.MAParam,
        --   e2.MAParamName,
        --   
        --   e1.MBParam,
        --   e2.MBParamName,
        --   
        --   e1.MCParam,
        --   e2.MCParamName
        --
    
    FROM
    DT_ItemAbnormalResist AS a
    
    LEFT OUTER JOIN DT_Item AS b ON ( b.IID = a.IID )
    
    LEFT OUTER JOIN DT_Abnormal AS c ON ( c.AID = a.AID )
    LEFT OUTER JOIN TP_AbnormalType AS c1 ON ( c1.AType = c.AType )

    LEFT OUTER JOIN DT_SkillAbnormal AS d ON ( c.AID = d.AbnormalID )
    LEFT OUTER JOIN DT_Skill AS d1 ON ( d.SID = d1.SID )
    LEFT OUTER JOIN DT_SkillPackSkill AS v ON ( d1.SID = v.mSID )
    LEFT OUTER JOIN DT_SkillPack AS v1 ON ( v.mSPID = v1.mSPID ) 
    
    --   LEFT JOIN DT_AbnormalModule AS e ON (c.AID = e.AID)
    --   LEFT JOIN DT_Module AS e1 ON (e.MID = e1.MID)
    --   LEFT JOIN TP_ModuleType AS e2 ON (e1.MType = e2.MType)
    
    WHERE
        a.IID = ? 
    ORDER BY
        a.IID
    """
    rows  = execute_query(query, (item_id,), fetch_one=False)
    
    if rows:
        result = []
        for row in rows:
            # Создаем базовый словарь с данными
            resist_data = {
                'IID': row[0],
                'IName': row[1],
                'AID': row[2],
                'ADesc': clean_description(row[3]),
                'AType': row[4],
                'ATypeDesc': clean_description(row[5]),
                'SID': row[6],
                'SName': row[7],
                'mSPID': row[8],
                'SkillPackName': row[9],
                'SkillPackDesc': clean_description(row[10]),
            }
            
            # Генерируем путь к иконке используя get_skill_icon_path
            resist_data['skill_icon_path'] = get_skill_icon_path(
                sprite_file=row[11],  # mSpriteFile
                sprite_x=row[12],     # mSpriteX
                sprite_y=row[13]      # mSpriteY
            )
            
            result.append(resist_data)
        
        return result
    
    return None

# DT_Bead Check
def get_rune_bead_data(item_id: int) -> Optional[DT_Bead]:
    """Get detailed bead/rune data by item ID with caching"""
    query = """
    SELECT
        a.mBeadNo,
        c.mName as 'mBead_Name',
        c.mBeadType,
        d1.mDesc as 'mBeadTypeDesc',
        CASE 
            WHEN c.mChkGroup = 0 THEN 'По умолчанию (0)'
            WHEN c.mChkGroup = 1 THEN 'Атака всем (1)'
            WHEN c.mChkGroup = 2 THEN 'Атака навыком (2)'
            WHEN c.mChkGroup = 3 THEN 'Атака оружием (3)'
            WHEN c.mChkGroup = 4 THEN 'Атака всем по умолчанию (4)'
            WHEN c.mChkGroup = 5 THEN 'Атака навыком по умолчанию (5)'
            WHEN c.mChkGroup = 6 THEN 'Атака оружием по умолчанию (6)'
            WHEN c.mChkGroup = 7 THEN 'Вероятность навыка по умолчанию (7)'
            WHEN c.mChkGroup = 8 THEN 'Вероятность оружия по умолчанию (8)'
            WHEN c.mChkGroup = 9 THEN 'Урон по умолчанию (9)'
            WHEN c.mChkGroup = 10 THEN 'Урон навыком по умолчанию (10)'
            WHEN c.mChkGroup = 11 THEN 'Физический урон по умолчанию (11)'
            WHEN c.mChkGroup = 12 THEN 'Магический урон по умолчанию (12)'
            WHEN c.mChkGroup = 13 THEN 'Отраженный урон по умолчанию (13)'
            WHEN c.mChkGroup = 14 THEN 'Привязанный к навыку умение по умолчанию (14)'
            WHEN c.mChkGroup = 15 THEN 'Урон навыка (15)'
            WHEN c.mChkGroup = 16 THEN 'Критический урон по умолчанию (16)'
            WHEN c.mChkGroup = 17 THEN 'Привязанное умение по умолчанию (17)'
            ELSE 'Неизвестно'
        END AS mChkGroup,
        c.mPercent,
        CASE 
            WHEN c.mApplyTarget = 0 THEN 'На себя (0)'
            WHEN c.mApplyTarget = 1 THEN 'На других (1)'
            WHEN c.mApplyTarget = 2 THEN 'На других игроков (2)'
            WHEN c.mApplyTarget = 3 THEN 'На других NPC (3)'
            ELSE 'Неизвестно'
        END AS mApplyTarget,
        c.mParamA,
        d1.mDescA as 'mParamADesc',
        c.mParamB,
        d1.mDescB as 'mParamBDesc',
        c.mParamC,
        d1.mDescC as 'mParamCDesc',
        c.mParamD,
        d1.mDescD as 'mParamDDesc',
        c.mParamE,
        d1.mDescE as 'mParamEDesc',
        CASE 
            WHEN d.mTargetIPos = 0 THEN 'Оружие (0)'
            WHEN d.mTargetIPos = 1 THEN 'Щит (1)'
            WHEN d.mTargetIPos = 2 THEN 'Доспех (броня) (2)'
            WHEN d.mTargetIPos = 3 THEN 'Кольцо 1 (левое) (3)'
            WHEN d.mTargetIPos = 4 THEN 'Кольцо 2 (правое) (4)'
            WHEN d.mTargetIPos = 5 THEN 'Амулет (5)'
            WHEN d.mTargetIPos = 6 THEN 'Обувь (6)'
            WHEN d.mTargetIPos = 7 THEN 'Перчатки (7)'
            WHEN d.mTargetIPos = 8 THEN 'Головной убор (шлем) (8)'
            WHEN d.mTargetIPos = 9 THEN 'Пояс (9)'
            WHEN d.mTargetIPos = 10 THEN 'Плащ (10)'
            WHEN d.mTargetIPos = 11 THEN 'Сфера Мастера (11)'
            WHEN d.mTargetIPos = 12 THEN 'Сфера Души (12)'
            WHEN d.mTargetIPos = 13 THEN 'Сфера Защиты (13)'
            WHEN d.mTargetIPos = 14 THEN 'Сфера Разрушения (14)'
            WHEN d.mTargetIPos = 15 THEN 'Сфера Жизни (15)'
            WHEN d.mTargetIPos = 16 THEN 'Сфера 1 Слот (Удачи/Ремесленника) (16)'
            WHEN d.mTargetIPos = 17 THEN 'Сфера 2 Слот (Перевоплощения) (17)'
            WHEN d.mTargetIPos = 18 THEN 'Сфера 3 Слот (Мудрости, Охоты, Разума) (18)'
            WHEN d.mTargetIPos = 19 THEN 'Питомец (19)'
            ELSE 'Неизвестно'
        END AS mTargetIPos,
        d.mProb as 'mProb',
        d.mGroup,
        d.mItemSubType,
        a2.mMaxHoleCount,
        a2.mHoleCount,
        a2.mProb as 'mHoleProb',
        a1.MID
    FROM DT_ItemBeadEffect as a
    LEFT JOIN DT_ItemBeadModule as a1 on (a.IID = a1.IID)
    LEFT JOIN TblBeadHoleProb as a2 on (a.IID = a2.IID)
    INNER JOIN DT_Item as b on (a.IID = b.IID)
    INNER JOIN DT_BeadEffect as c on (a.mBeadNo = c.mBeadNo)
    INNER JOIN DT_Bead as d on (a.IID = d.IID)
    INNER JOIN TP_BeadType as d1 on (d1.mBeadType = c.mBeadType)
    WHERE a.IID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_Bead(
            row.mBeadNo,
            row.mBead_Name,
            row.mBeadType,
            row.mBeadTypeDesc,
            row.mChkGroup,
            row.mPercent,
            row.mApplyTarget,
            row.mParamA,
            row.mParamADesc,  
            row.mParamB,
            row.mParamBDesc,  
            row.mParamC,
            row.mParamCDesc,  
            row.mParamD,
            row.mParamDDesc, 
            row.mParamE,
            row.mParamEDesc, 
            row.mTargetIPos,
            row.mProb,
            row.mGroup,
            row.mItemSubType,
            row.mMaxHoleCount,
            row.mHoleCount,
            row.mHoleProb,
            row.MID
        )
    return None


# DT_ItemBeadModule Check
def get_item_bead_module_data(item_id: int) -> Optional[List[DT_ItemBeadModule]]:
    query = """
        SELECT
            a.MID,
            c.MType,
            c1.MName,
            c1.MDesc,
            c.MLevel,
            c.MAParam,
            c1.MAParamName,
            c.MBParam,
            c1.MBParamName,
            c.MCParam,
            c1.MCParamName
        FROM
            DT_ItemBeadModule AS a
        INNER JOIN DT_Item AS b ON ( a.IID = b.IID )
        INNER JOIN DT_Module AS c ON ( a.MID = c.MID )
        INNER JOIN TP_ModuleType AS c1 ON ( c.MType = c1.MType )
        
        WHERE
            a.IID = ?
    """
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemBeadModule(
            row.MID,
            row.MType,
            row.MName,
            row.MDesc,
            row.MLevel,
            row.MAParam,
            row.MAParamName,
            row.MBParam,
            row.MBParamName,
            row.MCParam,
            row.MCParamName
        )
    return None


# TblBeadHoleProb Check
def get_item_bead_holeprob_data(item_id: int) -> Optional[List[TblBeadHoleProb]]:
    query = """
    SELECT 
        b.IName,
        a.mMaxHoleCount,
        a.mHoleCount,
        a.mProb
    FROM dbo.TblBeadHoleProb AS a
    INNER JOIN DT_Item AS b ON (a.IID = b.IID)
    WHERE a.IID = ?
    ORDER BY a.mMaxHoleCount, a.mHoleCount
    """
    

    
    rows = execute_query(query, (item_id,), fetch_one=False)
    #print(f"DEBUG: iid= {item_id}, Rows={rows}")
    if not rows:
        return None
        
    results = []
    for row in rows:
        results.append(TblBeadHoleProb(
            row.IName,
            row.mMaxHoleCount,
            row.mHoleCount,
            float(row.mProb)  # Явное приведение к float
        ))
    
    return results



# DT_ItemAttributeAdd Check
def get_item_attribute_add_data(item_id: int) -> Optional[List[DT_ItemAttributeAdd]]:
    attribute_type_weapon_df = get_google_sheets_data(ATTRIBUTE_TYPE_WEAPON_URL)

    query = """
    SELECT
        a.AID,
        b.AType,
        b.ALevel,
        b.ADiceDamage,
        b.ADamage 
    FROM
        DT_ItemAttributeAdd AS a
    INNER JOIN DT_AttributeAdd AS b ON ( a.AID = b.AID )

    WHERE
        a.IID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        AName = attribute_type_weapon_df[attribute_type_weapon_df['AType'] == row[1]]['AName'].iloc[0] if not attribute_type_weapon_df.empty else ''

        return DT_ItemAttributeAdd(
            row.AID,
            row.AType,
            AName,
            row.ALevel,
            row.ADiceDamage,
            row.ADamage
        )
    else:
        return None
    


# DT_ItemAttributeResist Check
def get_item_attribute_resist_data(item_id: int) -> Optional[List[DT_ItemAttributeResist]]:
    attribute_type_weapon_df = get_google_sheets_data(ATTRIBUTE_TYPE_ARMOR_URL)

    query = """
    SELECT
        a.AID,
        b.AType,
        b.ALevel,
        b.ADiceDamage,
        b.ADamage 
    FROM
        DT_ItemAttributeResist AS a
    INNER JOIN DT_AttributeResist AS b ON ( a.AID = b.AID )
    
    WHERE
        a.IID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        AName = attribute_type_weapon_df[attribute_type_weapon_df['AType'] == row[1]]['AName'].iloc[0] if not attribute_type_weapon_df.empty else ''

        return DT_ItemAttributeResist(
            row.AID,
            row.AType,
            AName,
            row.ALevel,
            row.ADiceDamage,
            row.ADamage
        )
    else:
        return None
    
    


# DT_ItemProtect Check
def get_item_protect_data(item_id: int) -> Optional[List[DT_ItemProtect]]:
    
    query = """
    SELECT
        a.PID,
        c.SID,
        e.SName,
        c.SLevel,
        c.SDPV,
        c.SMPV,
        c.SRPV,
        c.SDDV,
        c.SMDV,
        c.SRDV 
    FROM
        DT_ItemProtect AS a
    INNER JOIN DT_Protect AS c ON ( a.PID = c.SID )
    INNER JOIN TP_SlainType AS e ON ( c.SType = e.SType ) 
    
    WHERE a.IID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemProtect(
            row.PID,
            row.SID,
            row.SName,
            row.SLevel,
            row.SDPV,
            row.SMPV,
            row.SRPV,
            row.SDDV,
            row.SMDV,
            row.SRDV
        )
    else:
        return None
    
    


# DT_ItemSlain Check
def get_item_slain_data(item_id: int) -> Optional[List[DT_ItemSlain]]:
    
    query = """
    SELECT
        a.SID,
        b.SType,
        c.SName,
        b.SLevel,
        b.SHitPlus,
        b.SDDPlus,
        b.SRHitPlus,
        b.SRDDPlus
        
    FROM DT_ItemSlain AS a
        
    INNER JOIN DT_Slain AS b ON (a.SID = b.SID)
        
    INNER JOIN TP_SlainType AS c ON (b.SType = c.SType)
        
    WHERE a.IID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemSlain(
            row.SID,
            row.SType,
            row.SName,
            row.SLevel,
            row.SHitPlus,
            row.SDDPlus,
            row.SRHitPlus,
            row.SRDDPlus
        )
    else:
        return None
    


# DT_ItemPanalty Check
def get_item_panalty_data(item_id: int) -> Optional[List[DT_ItemPanalty]]:
    
    query = """
    SELECT
        a.IUseClass,
        a.IDHIT,
        a.IDDD,
        a.IRHIT,
        a.IRDD,
        a.IMHIT,
        a.IMDD,
        a.IHPPlus,
        a.IMPPlus,
        a.ISTR,
        a.IDEX,
        a.IINT,
        a.IHPRegen,
        a.IMPRegen,
        a.IAttackRate,
        a.IMoveRate,
        a.ICritical,
        a.IRange,
        a.IAddWeight,
        a.IAddPotionRestore,
        a.IDPV,
        a.IMPV,
        a.IRPV,
        a.IDDV,
        a.IMDV,
        a.IRDV,
        a.IHDPV,
        a.IHMPV,
        a.IHRPV,
        a.IHDDV,
        a.IHMDV,
        a.IHRDV 
    FROM
        DT_ItemPanalty AS a
        
    WHERE a.IID = ?
    """
    
    
    rows = execute_query(query, (item_id,), fetch_one=False)

    if not rows:
        return None
        
    results = []
    for row in rows:
        
        
        PanaltyClassPic = None
        PanaltyClassPic = f"{current_app.config['GITHUB_URL']}class/{row.IUseClass}.png",
        results.append(DT_ItemPanalty(
            row.IUseClass,
            PanaltyClassPic[0],
            row.IDHIT,
            row.IDDD,
            row.IRHIT,
            row.IRDD,
            row.IMHIT,
            row.IMDD,
            row.IHPPlus,
            row.IMPPlus,
            row.ISTR,
            row.IDEX,
            row.IINT,
            row.IHPRegen,
            row.IMPRegen,
            row.IAttackRate,
            row.IMoveRate,
            row.ICritical,
            row.IRange,
            row.IAddWeight,
            row.IAddPotionRestore,
            row.IDPV,
            row.IMPV,
            row.IRPV,
            row.IDDV,
            row.IMDV,
            row.IRDV,
            row.IHDPV,
            row.IHMPV,
            row.IHRPV,
            row.IHDDV,
            row.IHMDV,
            row.IHRDV
        ))
    
    return results
