from typing import List, Dict, Optional, Tuple, Union
import pandas as pd
import requests
from flask import current_app
from models.monster import Monster
from services.database import execute_query, get_db_connection
from services.utils import get_google_sheets_data, get_skill_icon_path, clean_description
from config.settings import MONSTER_CLASS_URL, ATTRIBUTE_TYPE_WEAPON_URL, ATTRIBUTE_TYPE_ARMOR_URL
from models.monster import DT_MonsterResource, DT_MonsterAbnormalResist, DT_MonsterAttributeAdd, DT_MonsterAttributeResist, DT_MonsterProtect, DT_MonsterSlain


def get_monster_resource(monster_id: int) -> Optional[DT_MonsterResource]:
    """Get monster resource by MID with caching"""
    query = "SELECT RFileName FROM DT_MonsterResource WHERE ROwnerID = ?"
    row = execute_query(query, (monster_id,), fetch_one=True)
    
    if row:
        return DT_MonsterResource(
            row.RFileName
        )
    return None

def get_monster_resource_url(RFileName):
    monster_model_no = f"{current_app.config['GITHUB_URL']}models/m{int(RFileName):05}"
    
def get_monster_pic_url(monster_id: int):
    monster_pic_url = f"{current_app.config['GITHUB_URL']}{monster_id}.png"
    return monster_pic_url

# Respawn Time Info
def get_monster_mtick(monster_id: int) -> Union[str, int]:
    query = f"SELECT mTick FROM {current_app.config['DATABASE_NAME']}.dbo.TblMonsterSpot WHERE mMID = ?"
    respawn_result = execute_query(query, (monster_id,), fetch_one=True)
    
    if respawn_result is None:
        return 0
    
    return respawn_result[0]


def get_monster_by_id(monster_id: int) -> Optional[Dict]:
    """Get monster information by ID"""
    query = """
    SELECT MID, MName, MClass, MLevel, MHP, MMP, MExp, 
           mRaceType, mIsShowHp, MChaotic, mDetectTransF, 
           mDetectTransP, mDetectChao, mIsResistTransF 
    FROM DT_Monster 
    WHERE MID = ?
    """
    row = execute_query(query, (monster_id,), fetch_one=True)
    
    if row:
        monster = Monster(
            row.MID, row.MName, row.MClass, row.MLevel,
            row.MHP, row.MMP, row.MExp, row.mRaceType,
            row.mIsShowHp, row.MChaotic, row.mDetectTransF,
            row.mDetectTransP, row.mDetectChao, row.mIsResistTransF
        )
        return monster.to_dict()
    return None

def get_monster_drops(monster_id: int) -> List[Dict]:
    """Get all drops for a specific monster"""
    monster_class_df = get_google_sheets_data(MONSTER_CLASS_URL)
    
    query = f"""
    SELECT
        a.MID,
        a.MName,
        a.mClass,
        w.DDropType,
        q.DPercent as GroupDropChance,
        q.DGroup as DropGroupID,
        w.DName as Description,
        e.DDrop as DDropID,
        e.DPercent as ItemDropChance,
        r.DItem,
        c.IName as ItemName,
        r.DNumber as Quantity,
        i.RFileName,
        i.RPosX,
        i.RPosY
    FROM {current_app.config['DATABASE_NAME']}.dbo.DT_Monster a
    LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_MonsterDrop q ON a.MID = q.MID
    LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
    LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
    LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_DropItem r ON e.DDrop = r.DDrop
    LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_Item c ON r.DItem = c.IID
    LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_ItemResource i ON c.IID = i.ROwnerID AND i.RType = 2
    WHERE a.MID = ? AND c.IIsEvent = 0
    ORDER BY r.DItem
    """
    
    rows = execute_query(query, (monster_id,))
    unique_results = {}

    for row in rows:
        # Get monster class info from Google Sheets data
        monster_class_info = monster_class_df[
            monster_class_df['MClass'] == row.mClass
        ]['MName'].iloc[0] if not monster_class_df.empty else ''

        key = row.DItem
        pic = None
        if row.RFileName and row.RPosX is not None and row.RPosY is not None:
            pic = f"{current_app.config['GITHUB_URL']}{row.RFileName.split('.')[0]}_{row.RPosX}_{row.RPosY}.png"

        if key not in unique_results:
            unique_results[key] = {
                "MID": row.MID,
                "MName": row.MName,
                "MClass": monster_class_info,
                "DDropType": row.DDropType,
                "DPercentGroup": row.GroupDropChance,
                "DGroup": row.DropGroupID,
                "DName": row.Description,
                "DDrop": row.DDropID,
                "DPercentItem": round(float(row.ItemDropChance), 1),
                "DItem": row.DItem,
                "IName": row.ItemName,
                "DNumber": row.Quantity,
                "Pic": pic if pic else f"{current_app.config['GITHUB_URL']}no_item_image.png",
                "count": 1
            }
        else:
            unique_results[key]["count"] += 1
            unique_results[key]["DNumber"] += row.Quantity

    results = list(unique_results.values())
    results.sort(key=lambda x: x["DItem"])
    return results


def get_monster_drop_info(item_id: int) -> List[Dict]:
    """Get all drops for a specific monster"""
    monster_class_df = get_google_sheets_data(MONSTER_CLASS_URL)
   
    query = f"""
        SELECT
            a.MID,
            a.MName,
            a.mClass,  
            w.DDropType,
            q.DPercent as GroupDropChance,
            q.DGroup as DropGroupID,
            w.DName as Description,
            e.DDrop as DDropID,
            e.DPercent as ItemDropChance,
            r.DItem,
            c.IName as ItemName,
            r.DNumber as Quantity
        FROM {current_app.config['DATABASE_NAME']}.dbo.DT_Monster a
        LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_MonsterDrop q ON a.MID = q.MID
        LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
        LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
        LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_DropItem r ON e.DDrop = r.DDrop
        LEFT JOIN {current_app.config['DATABASE_NAME']}.dbo.DT_Item c ON r.DItem = c.IID
        WHERE r.DItem = ? AND c.IIsEvent = 0
        ORDER BY a.MID
    """
   
    rows = execute_query(query, (item_id,), fetch_one=False)
    unique_results = {}
    for row in rows:
        # Получаем информацию о классе монстра из данных Google Sheets
        monster_class_info = monster_class_df[
            monster_class_df['MClass'] == row.mClass
        ]['MName'].iloc[0] if not monster_class_df.empty else ''
       
        # Используем комбинацию MID и DGroup как ключ
        key = (row.MID, row.DropGroupID)
        
        pic = f"{current_app.config['GITHUB_URL']}{row.MID}.png"
        
        if key not in unique_results:
            unique_results[key] = {
                "MID": row.MID,
                "MName": row.MName.replace("/n", " "),
                "MClass": monster_class_info,
                "DDropType": row.DDropType,
                "DPercentGroup": row.GroupDropChance,
                "DGroup": row.DropGroupID,
                "DName": row.Description,
                "DDrop": row.DDropID,
                "DPercentItem": round(float(row.ItemDropChance), 1),
                "DItem": row.DItem,
                "IName": row.ItemName,
                "DNumber": row.Quantity,
                "Pic": pic if pic else f"{current_app.config['GITHUB_URL']}no_item_image.png",
                "count": 1
            }
        else:
            # Обновляем только счетчик, так как это тот же самый монстр и группа
            unique_results[key]["count"] += 1
            
    # Преобразуем словарь в список и сортируем
    results = list(unique_results.values())
    results.sort(key=lambda x: (x["MID"], x["DGroup"]))
   
    return results


def get_monsters_by_class(class_ids: List[int]) -> Tuple[List[Tuple], Dict]:
    """Get monsters by class IDs"""
    class_str = ','.join(str(c) for c in class_ids)
    query = f"""
        SELECT MID, MName, MClass 
        FROM DT_Monster 
        WHERE MClass IN ({class_str}) 
        ORDER BY MID
    """
    
    monsters = execute_query(query)
    monsters = [(row.MID, row.MName, row.MClass) for row in monsters]

    # Get file paths
    file_paths = {
        monster[0]: f"{current_app.config['GITHUB_URL']}{monster[0]}.png"
        for monster in monsters
    }

    return monsters, file_paths



def get_monsterabnormalResist_data(monster_id: int) -> Optional[List[DT_MonsterAbnormalResist]]:
    """Get monster resource by MID with caching"""
    query = """
        SELECT DISTINCT
            a.MID,
            b.MName,
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
    DT_MonsterAbnormalResist AS a
    
    LEFT OUTER JOIN DT_Monster AS b ON ( b.MID = a.MID )
    
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
        a.MID = ? 
    ORDER BY
        a.MID
    """
    rows  = execute_query(query, (monster_id,), fetch_one=False)
    
    if rows:
        result = []
        for row in rows:
            # Создаем базовый словарь с данными
            resist_data = {
                'MID': row[0],
                'MName': row[1],
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





# DT_MonsterAttributeAdd Check
def get_monster_attribute_add_data(monster_id: int) -> Optional[List[DT_MonsterAttributeAdd]]:
    attribute_type_weapon_df = get_google_sheets_data(ATTRIBUTE_TYPE_WEAPON_URL)

    query = """
    SELECT
        a.AID,
        b.AType,
        b.ALevel,
        b.ADiceDamage,
        b.ADamage 
    FROM
        DT_MonsterAttributeAdd AS a
    INNER JOIN DT_AttributeAdd AS b ON ( a.AID = b.AID )

    WHERE
        a.MID = ?
    """
    
    row = execute_query(query, (monster_id,), fetch_one=True)
    
    if row:
        AName = attribute_type_weapon_df[attribute_type_weapon_df['AType'] == row[1]]['AName'].iloc[0] if not attribute_type_weapon_df.empty else ''

        return DT_MonsterAttributeAdd(
            row.AID,
            row.AType,
            AName,
            row.ALevel,
            row.ADiceDamage,
            row.ADamage
        )
    else:
        return None
    


# DT_MonsterAttributeResist Check
def get_monster_attribute_resist_data(monster_id: int) -> Optional[List[DT_MonsterAttributeResist]]:
    attribute_type_weapon_df = get_google_sheets_data(ATTRIBUTE_TYPE_ARMOR_URL)

    query = """
    SELECT
        a.AID,
        b.AType,
        b.ALevel,
        b.ADiceDamage,
        b.ADamage 
    FROM
        DT_MonsterAttributeResist AS a
    INNER JOIN DT_AttributeResist AS b ON ( a.AID = b.AID )
    
    WHERE
        a.MID = ?
    """
    
    row = execute_query(query, (monster_id,), fetch_one=True)
    
    if row:
        AName = attribute_type_weapon_df[attribute_type_weapon_df['AType'] == row[1]]['AName'].iloc[0] if not attribute_type_weapon_df.empty else ''

        return DT_MonsterAttributeResist(
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
def get_monster_protect_data(monster_id: int) -> Optional[List[DT_MonsterProtect]]:
    
    query = """
    SELECT
        a.SID,
        c.SID as 'ProtectSID',
        e.SName,
        c.SLevel,
        c.SDPV,
        c.SMPV,
        c.SRPV,
        c.SDDV,
        c.SMDV,
        c.SRDV 
    FROM
        DT_MonsterProtect AS a

    INNER JOIN DT_Protect AS c ON ( a.SID = c.SID )
    INNER JOIN TP_SlainType AS e ON ( c.SType = e.SType ) 
    
    WHERE a.MID = ?
    """
    
    row = execute_query(query, (monster_id,), fetch_one=True)
    
    if row:
        return DT_MonsterProtect(
            row.SID,
            row.ProtectSID,
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
    
    

# DT_MonsterSlain Check
def get_monster_slain_data(item_id: int) -> Optional[List[DT_MonsterSlain]]:
    
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
        
    FROM DT_MonsterSlain AS a
        
    INNER JOIN DT_Slain AS b ON (a.SID = b.SID)
        
    INNER JOIN TP_SlainType AS c ON (b.SType = c.SType)
        
    WHERE a.MID = ?
    """
    
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_MonsterSlain(
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