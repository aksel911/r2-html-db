from typing import List, Dict, Optional, Tuple
from os.path import splitext
from functools import lru_cache
from flask import current_app
from models.item import DT_Item, DT_ItemResource, TblSpecificProcItem, DT_ItemAbnormalResist, DT_Bead, DT_ItemBeadModule, TblBeadHoleProb
from services.database import execute_query, get_db_connection
from services.utils import get_skill_icon_path, clean_description


@lru_cache(maxsize=1000)
def get_item_by_id(item_id: int) -> Optional[DT_Item]:
    """Get item by ID with caching"""
    query = "SELECT * FROM DT_ITem WHERE IID = ?"
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_Item(
            row.IID,
            row.IName,
            row.IDesc.replace('\\n', ' ⭑ ') if row.IDesc else '',
            row.IWeight,
            row.IUseClass,
            row.IType,
            row.IMaxBeadHoleCount,
            row.ITermOfValidity
        )
    return None

@lru_cache(maxsize=1000)
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


def get_item_pic_url(item_id: int):
    item_pic_url = f"{current_app.config['GITHUB_URL']}{item_id.RFileName}_{item_id.RPosX}_{item_id.RPosY}.png"
    return item_pic_url


@lru_cache(maxsize=1000)
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


@lru_cache(maxsize=1000)
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
    type_str = ','.join(str(t) for t in item_types)
    
    # Get item IDs
    query = f"""
    SELECT IID 
    FROM DT_ITem 
    WHERE IType IN ({type_str}) 
    AND IName LIKE ? 
    ORDER BY IID
    """
    rows = execute_query(query, (f'%{search_term}%',))
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
