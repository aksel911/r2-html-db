from typing import List, Dict, Optional, Tuple
import pandas as pd
import requests
from flask import current_app
from models.monster import Monster
from services.database import execute_query, get_db_connection
from services.utils import get_google_sheets_data
from config.settings import MONSTER_CLASS_URL

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
            a.mClass,  -- Added mClass to fetch for joining with Google Sheets data
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
    
    rows = execute_query(query, (item_id,))
    unique_results = {}

    for row in rows:
        # Get monster class info from Google Sheets data
        monster_class_info = monster_class_df[
            monster_class_df['MClass'] == row.mClass
        ]['MName'].iloc[0] if not monster_class_df.empty else ''

        key = row.DItem
        pic = None
        pic = f"{current_app.config['GITHUB_URL']}{row.MID}.png"
        #pic = f"{current_app.config['GITHUB_URL']}{row.RFileName.split('.')[0]}_{row.RPosX}_{row.RPosY}.png"

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