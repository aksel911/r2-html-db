from typing import List, Dict, Optional, Tuple
from os.path import splitext
from functools import lru_cache
from flask import current_app
from models.item import DT_Item, DT_ItemResource, TblSpecificProcItem, DT_ItemAbnormalResist
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