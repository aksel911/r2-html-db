import os
import requests
import pandas as pd
from flask import Flask, render_template, request
import pyodbc
from os.path import splitext
from functools import lru_cache
from typing import Dict, List, Optional, Tuple
from contextlib import contextmanager
from dotenv import load_dotenv
from dataclasses import dataclass, field

load_dotenv()
app = Flask(__name__)

# !URLs for Google Sheets
MONSTER_CLASS_URL = "https://docs.google.com/spreadsheets/d/1fcCO8ZwJsENYZhKBpEfdgaTswANkrGolBtAcqVeTECs/edit?usp=sharing"  # TP_MonsterClass
MONSTER_RACE_URL = "https://docs.google.com/spreadsheets/d/1c3Yh1GD-6GnDufvGzUdfRQtq5zHXkj9DRq_S9t1Lf9s/edit?usp=sharing"  # TP_MonsterRaceType
MONSTER_LOCATION_URL = "https://docs.google.com/spreadsheets/d/1rBuuiMUvlYZwNPaRhdk5PkhTQa1mwj5z8dUDKWoBetU/edit?usp=sharing"  # DT_MonsterLocation
SKILLAPPLYRACE_LOCATION_URL = "https://docs.google.com/spreadsheets/d/1Vz-YWTOGnFUqzlieWfUg0NM-fSilneIEZ03FratjC2E/edit?usp=sharing"    # TP_SkillApplyRace

# !GitHub URL
GITHUB_URL = "https://raw.githubusercontent.com/Aksel911/R2-HTML-DB/main/static/"


# DONT ANYTHING TOUCH BELOW!

# Configuration
def get_database_config() -> Dict[str, str]:
    return {
        'DRIVER': os.getenv('DB_DRIVER'),
        'SERVER': os.getenv('DB_SERVER'),
        'DATABASE': os.getenv('DB_NAME'),
        'UID': os.getenv('DB_USER'),
        'PWD': os.getenv('DB_PASSWORD'),
        'GITHUB_URL': os.getenv('DB_PASSWORD'),
    }


def get_github_url() -> str:
    return os.getenv('GITHUB_URL', GITHUB_URL)


required_env_vars = ['DB_USER', 'DB_PASSWORD']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing config required environment variables: {', '.join(missing_vars)}")

DATABASE_CONFIG = get_database_config()
GITHUB_URL = get_github_url()

DATABASE_NAME = os.getenv('DB_NAME', 'FNLParm')


# Connection pooling
@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn_str = ';'.join(f'{k}={v}' for k, v in DATABASE_CONFIG.items())
    conn = pyodbc.connect(conn_str)
    try:
        yield conn
    finally:
        conn.close()



# ? MODELS

@dataclass
class DT_Item:
    """Data class for items"""
    IID: int
    IName: str
    IDesc: str
    IWeight: float
    IUseClass: str
    IType: int
    IMaxBeadHoleCount: int
    ITermOfValidity: int

    def __post_init__(self):
        self.IUseClass = f"{GITHUB_URL}class/{self.IUseClass}.png"


@dataclass
class DT_ItemResource:
    """Data class for item resources"""
    ROwnerID: int
    RFileName: str
    RPosX: int
    RPosY: int

    def __post_init__(self):
        self.RFileName = splitext(self.RFileName)[0]
        self.file_path = f"{GITHUB_URL}{self.RFileName}_{self.RPosX}_{self.RPosY}.png"


@dataclass
class Monster:
    """Data class for monsters"""
    MID: int
    MName: str
    MClass: int
    MLevel: int
    MHP: int
    MMP: int
    MExp: int
    mRaceType: int
    mIsShowHp: bool
    MChaotic: int
    mDetectTransF: bool
    mDetectTransP: bool
    mDetectChao: int
    mIsResistTransF: bool

    def to_dict(self) -> Dict:
        """Convert monster to dictionary with formatted fields"""
        return {
            "MID": self.MID,
            "MName": self.MName.replace('/n', ' '),
            "MClass": self.MClass,
            "MLevel": self.MLevel,
            "MHP": self.MHP,
            "MMP": self.MMP,
            "mExp": self.MExp,
            "mRaceType": self.mRaceType,
            "mIsShowHp": 'Да' if self.mIsShowHp else 'Нет',
            "MChaotic": self.MChaotic,
            "mDetectTransF": 'Да' if self.mDetectTransF else 'Нет',
            "mDetectTransP": 'Да' if self.mDetectTransP else 'Нет',
            "mDetectChao": self.mDetectChao,
            "mIsResistTransF": 'Да' if self.mIsResistTransF else 'Нет'
        }


@dataclass
class Skill:
    """Data class for skills"""
    sid: int
    name: str
    desc: str
    hit_plus: int
    mp_per_use: int
    skill_type: int
    type_desc: str
    hp_per_use: int
    chao_use: int
    apply_radius: int
    apply_race: int
    casting_delay: int
    consume_item: int
    active_type: int
    animation: str
    casting_speed: int
    skill_effect: int
    cool_time: int
    consume_item2: int
    consume_item_cnt2: int
    item_id: Optional[int]
    item_pic: Optional[str]
    item_name: Optional[str]
    item_use_level: Optional[int]
    item_use_class: Optional[str]
    skill_pack_id: Optional[int]
    skill_pack_desc: Optional[str]
    abnormal_data: Optional[Dict[str, any]] = field(default_factory=dict)
    module_data: Optional[Dict[str, any]] = field(default_factory=dict)

    def __post_init__(self):
        # Очистка описаний от /n
        self.desc = self.desc.replace('/n', ' ⭑ ').replace('\\n', ' ⭑ ') if self.desc else ''
        self.item_name = self.item_name.replace('/n', '') if self.item_name else ''
        self.skill_pack_desc = self.skill_pack_desc.replace('/n', ' ⭑ ').replace('\\n', ' ⭑ ') if self.skill_pack_desc else ''

        # Обработка item_use_class
        if self.item_use_class:
            self.item_use_class = f"{GITHUB_URL}class/{self.item_use_class}.png"
        else:
            self.item_use_class = f"{GITHUB_URL}class/0.png"  # Дефолтное значение

        if self.item_pic and isinstance(self.item_pic, DT_ItemResource):
            self.item_pic = self.item_pic.file_path

        # Очистка и форматирование данных аномалий
        if self.abnormal_data:
            self.abnormal_data = {
                key: (str(value).replace('/n', ' ').strip() if isinstance(value, str) else value)
                for key, value in self.abnormal_data.items()
            }

        # Очистка и форматирование данных модулей
        if self.module_data and "params" in self.module_data:
            self.module_data["params"] = [
                {
                    "name": param.get("name", "").replace('/n', ' ').strip(),
                    "value": param.get("value", None)
                }
                for param in self.module_data["params"]
            ]




# ? Utils

# Google Sheets
def get_google_sheets_data(url: str) -> pd.DataFrame:
    """Fetch monster class data from Google Sheets"""
    # Convert the Google Sheets URL to export format
    sheet_id = url.split('/d/')[1].split('/')[0]
    export_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"

    try:
        # Read the CSV directly from the export URL
        df = pd.read_csv(export_url)
        return df
    except Exception as e:
        print(f"Error fetching Google Sheets data: {e}")
        return pd.DataFrame()

# Template filters
@app.template_filter('remove_extension')
def remove_extension(value):
    """Remove file extension from string"""
    return splitext(value)[0]



# ! ITEMS
@lru_cache(maxsize=1000)
def get_item_by_id(item_id: int) -> Optional[DT_Item]:
    """Get item by ID with caching"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM DT_ITem WHERE IID = ?"
        cursor.execute(query, (item_id,))
        row = cursor.fetchone()
        if row:
            return DT_Item(
                row.IID, row.IName, row.IDesc.replace('\\n', ' ⭑ ') if row.IDesc else '', row.IWeight,
                row.IUseClass, row.IType, row.IMaxBeadHoleCount,
                row.ITermOfValidity
            )
    return None


@lru_cache(maxsize=1000)
def get_item_resource(item_id: int) -> Optional[DT_ItemResource]:
    """Get item resource by ID with caching"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT * FROM DT_ItemResource WHERE ROwnerID = ? AND RType = 2"
        cursor.execute(query, (item_id,))
        row = cursor.fetchone()
        if row:
            return DT_ItemResource(
                row.ROwnerID, row.RFileName,
                row.RPosX, row.RPosY
            )
    return None

def get_items_by_type(item_types: List[int], search_term: str = '') -> Tuple[List[DT_Item], Dict[int, str]]:
    """Generic function to fetch items by type with optional search"""
    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Convert item types to string for SQL
        type_str = ','.join(str(t) for t in item_types)

        # Get item IDs
        query = f"""
        SELECT IID FROM DT_ITem 
        WHERE IType IN ({type_str}) 
        AND IName LIKE ? 
        ORDER BY IID
        """
        cursor.execute(query, (f'%{search_term}%',))
        item_ids = [row.IID for row in cursor.fetchall()]

        if not item_ids:
            return [], {}

        # Get item resources
        id_str = ','.join(str(i) for i in item_ids)
        query = f"""
        SELECT RFileName, RPosX, RPosY, ROwnerID 
        FROM DT_ItemResource 
        WHERE ROwnerID IN ({id_str}) 
        AND RType = 2
        """
        cursor.execute(query)
        file_paths = {}
        for row in cursor.fetchall():
            file_name = splitext(row.RFileName)[0]
            file_path = f"{GITHUB_URL}{file_name}_{row.RPosX}_{row.RPosY}.png"
            file_paths[row.ROwnerID] = file_path

        # Get items
        query = f"SELECT * FROM DT_ITem WHERE IID IN ({id_str})"
        cursor.execute(query)
        items = [
            DT_Item(
                row.IID, row.IName, (row.IDesc or "").replace('\\n', ' '), row.IWeight,
                row.IUseClass, row.IType, row.IMaxBeadHoleCount,
                row.ITermOfValidity
            )
            for row in cursor.fetchall()
        ]

        return items, file_paths

def get_item_skill(item_id: int) -> Optional[Tuple]:
    """Get skill details by ID"""
    if item_id is None:
        return None

    with get_db_connection() as conn:
        cursor = conn.cursor()
        # *Если выбрать в шаблоне: b1.SID, тогда ссылка будет на Создание скила, если на сам скилл: v2.SID AS v2_SID
        query = """
        SELECT 
            a.IID,
            a.IName,
            b1.SID,
            c1.AID,
            d1.MID,
            v.mSPID,
            v.mName,
            v.mSpriteFile,
            v.mSpriteX,
            v.mSpriteY,
            v2.SID AS v2_SID,
            v2.SName AS v2_SName
        FROM DT_Item a
            INNER JOIN DT_ItemSkill b 
                ON a.IID = b.IID AND a.IID = ?
            INNER JOIN DT_Skill b1 
                ON b.SID = b1.SID
            INNER JOIN DT_SkillAbnormal c 
                ON b1.SID = c.SID
            INNER JOIN DT_Abnormal c1 
                ON c.AbnormalID = c1.AID
            INNER JOIN DT_AbnormalModule d 
                ON c1.AID = d.AID
            INNER JOIN DT_Module d1 
                ON d.MID = d1.MID
            INNER JOIN DT_SkillPack v 
                ON d1.MAParam = v.mSPID
            INNER JOIN DT_SkillPackSkill v1 
                ON v.mSPID = v1.mSPID
            INNER JOIN DT_Skill v2 
                ON v1.mSID = v2.SID
        """
        try:
            cursor.execute(query, (item_id,))
            row = cursor.fetchone()

            if not row:
                return None

            itemdskill_data = (row.IID, row.IName, row.SID, row.AID, row.MID, row.mSPID, row.mName, row.mSpriteFile, row.mSpriteX, row.mSpriteY, row.v2_SID, row.v2_SName)

            itemskill_pic = get_skill_icon_path(row.mSpriteFile, row.mSpriteX, row.mSpriteY)

            return itemdskill_data, itemskill_pic

        except Exception as e:
            print(f"Error in get_item_skill: {e}")
            return None


# ! MONSTERS / NPS

# def get_monster_drop_info(item_id: int) -> List[Dict]:
#     """Get monster drop information for an item"""
#     with get_db_connection() as conn:
#         cursor = conn.cursor()
#         query = f"""
#         SELECT
#             a.MID,
#             a.MName,
#             w.DDropType,
#             q.DPercent as GroupDropChance,
#             q.DGroup as DropGroupID,
#             w.DName as Description,
#             e.DDrop as DDropID,
#             e.DPercent as ItemDropChance,
#             r.DItem,
#             c.IName as ItemName,
#             r.DNumber as Quantity
#         FROM {DATABASE_NAME}.dbo.DT_Monster a
#         LEFT JOIN {DATABASE_NAME}1602.dbo.TP_MonsterClass b ON a.mClass = b.MClass
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_MonsterDrop q ON a.MID = q.MID
#         LEFT JOIN {DATABASE_NAME}.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_DropItem r ON e.DDrop = r.DDrop
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_Item c ON r.DItem = c.IID
#         WHERE r.DItem = ? AND c.IIsEvent = 0
#         ORDER BY a.MID
#         """
#         cursor.execute(query, (item_id,))
#
#         unique_results = {}
#
#         for row in cursor.fetchall():
#             # Используем только MID как ключ для уникальности
#             key = row.MID
#
#             # Если такого монстра еще нет в результатах, добавляем его
#             if key not in unique_results:
#                 monster_pic = f"{GITHUB_URL}{row.MID}.png"
#
#                 unique_results[key] = {
#                     "MID": row.MID,
#                     "MName": row.MName.replace('/n', ' ') if row.MName else '',
#                     "DDropType": row.DDropType,
#                     "DPercentGroup": row.GroupDropChance,
#                     "DGroup": row.DropGroupID,
#                     "DName": row.Description,
#                     "DDrop": row.DDropID,
#                     "DPercentItem": round(float(row.ItemDropChance), 1),
#                     "DItem": row.DItem,
#                     "IName": row.ItemName,
#                     "DNumber": row.Quantity,
#                     "Pic": monster_pic
#                 }
#
#         return list(unique_results.values())
def get_monster_drop_info(item_id: int) -> List[Dict]:
    """TP_MonsterClass"""
    monster_class_df = get_google_sheets_data(MONSTER_CLASS_URL)

    with get_db_connection() as conn:
        cursor = conn.cursor()
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
        FROM {DATABASE_NAME}.dbo.DT_Monster a
        LEFT JOIN {DATABASE_NAME}.dbo.DT_MonsterDrop q ON a.MID = q.MID
        LEFT JOIN {DATABASE_NAME}.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
        LEFT JOIN {DATABASE_NAME}.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
        LEFT JOIN {DATABASE_NAME}.dbo.DT_DropItem r ON e.DDrop = r.DDrop
        LEFT JOIN {DATABASE_NAME}.dbo.DT_Item c ON r.DItem = c.IID
        WHERE r.DItem = ? AND c.IIsEvent = 0
        ORDER BY a.MID
        """
        cursor.execute(query, (item_id,))
        unique_results = {}

        for row in cursor.fetchall():
            # Get monster class info from Google Sheets data
            monster_class_info = monster_class_df[
                monster_class_df['MClass'] == row.mClass
                ]['MName'].iloc[0] if not monster_class_df.empty else ''

            key = row.MID
            if key not in unique_results:
                monster_pic = f"{GITHUB_URL}{row.MID}.png"
                unique_results[key] = {
                    "MID": row.MID,
                    "MName": row.MName.replace('/n', ' ') if row.MName else '',
                    "MClass": monster_class_info,  # Added monster class info from Google Sheets
                    "DDropType": row.DDropType,
                    "DPercentGroup": row.GroupDropChance,
                    "DGroup": row.DropGroupID,
                    "DName": row.Description,
                    "DDrop": row.DDropID,
                    "DPercentItem": round(float(row.ItemDropChance), 1),
                    "DItem": row.DItem,
                    "IName": row.ItemName,
                    "DNumber": row.Quantity,
                    "Pic": monster_pic
                }

        return list(unique_results.values())


def get_monster_by_id(monster_id: int) -> Optional[Dict]:
    """Get monster information by ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
        SELECT MID, MName, MClass, MLevel, MHP, MMP, MExp, 
               mRaceType, mIsShowHp, MChaotic, mDetectTransF, 
               mDetectTransP, mDetectChao, mIsResistTransF 
        FROM DT_Monster 
        WHERE MID = ?
        """
        cursor.execute(query, (monster_id,))
        row = cursor.fetchone()
        if row:
            monster = Monster(
                row.MID, row.MName, row.MClass, row.MLevel,
                row.MHP, row.MMP, row.MExp, row.mRaceType,
                row.mIsShowHp, row.MChaotic, row.mDetectTransF,
                row.mDetectTransP, row.mDetectChao, row.mIsResistTransF
            )
            return monster.to_dict()
    return None

# def get_monster_drops(monster_id: int) -> List[Dict]:
#     """Get all drops for a specific monster"""
#     with get_db_connection() as conn:
#         cursor = conn.cursor()
#         query = f"""
#         SELECT
#             a.MID,
#             a.MName,
#             w.DDropType,
#             q.DPercent as GroupDropChance,
#             q.DGroup as DropGroupID,
#             w.DName as Description,
#             e.DDrop as DDropID,
#             e.DPercent as ItemDropChance,
#             r.DItem,
#             c.IName as ItemName,
#             r.DNumber as Quantity,
#             i.RFileName,
#             i.RPosX,
#             i.RPosY
#         FROM {DATABASE_NAME}.dbo.DT_Monster a
#         LEFT JOIN {DATABASE_NAME}1602.dbo.TP_MonsterClass b ON a.mClass = b.MClass
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_MonsterDrop q ON a.MID = q.MID
#         LEFT JOIN {DATABASE_NAME}.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_DropItem r ON e.DDrop = r.DDrop
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_Item c ON r.DItem = c.IID
#         LEFT JOIN {DATABASE_NAME}.dbo.DT_ItemResource i ON c.IID = i.ROwnerID AND i.RType = 2
#         WHERE a.MID = ? AND c.IIsEvent = 0
#         ORDER BY r.DItem
#         """
#         cursor.execute(query, (monster_id,))
#
#         # Словарь для хранения уникальных предметов и подсчета дубликатов
#         unique_results = {}
#
#         for row in cursor.fetchall():
#             # Используем DItem как ключ
#             key = row.DItem
#
#             pic = None
#             if row.RFileName and row.RPosX is not None and row.RPosY is not None:
#                 pic = f"{GITHUB_URL}{row.RFileName.split('.')[0]}_{row.RPosX}_{row.RPosY}.png"
#
#             if key not in unique_results:
#                 # Если предмет встречается впервые, создаем новую запись
#                 unique_results[key] = {
#                     "MID": row.MID,
#                     "MName": row.MName,
#                     "DDropType": row.DDropType,
#                     "DPercentGroup": row.GroupDropChance,
#                     "DGroup": row.DropGroupID,
#                     "DName": row.Description,
#                     "DDrop": row.DDropID,
#                     "DPercentItem": round(float(row.ItemDropChance), 1),
#                     "DItem": row.DItem,
#                     "IName": row.ItemName,
#                     "DNumber": row.Quantity,  # Начальное количество
#                     "Pic": pic if pic else f"{GITHUB_URL}no_item_image.png",
#                     "count": 1  # Счетчик дубликатов
#                 }
#             else:
#                 # Если предмет уже есть, увеличиваем счетчик и обновляем количество
#                 unique_results[key]["count"] += 1
#                 unique_results[key]["DNumber"] += row.Quantity
#
#         # Преобразуем словарь обратно в список
#         results = list(unique_results.values())
#
#         # Сортируем результаты по DItem
#         results.sort(key=lambda x: x["DItem"])
#
#         return results

def get_monster_drops(monster_id: int) -> List[Dict]:
    """TP_MonsterClass"""
    monster_class_df = get_google_sheets_data(MONSTER_CLASS_URL)

    with get_db_connection() as conn:
        cursor = conn.cursor()
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
            r.DNumber as Quantity,
            i.RFileName,
            i.RPosX,
            i.RPosY
        FROM {DATABASE_NAME}.dbo.DT_Monster a
        LEFT JOIN {DATABASE_NAME}.dbo.DT_MonsterDrop q ON a.MID = q.MID
        LEFT JOIN {DATABASE_NAME}.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
        LEFT JOIN {DATABASE_NAME}.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
        LEFT JOIN {DATABASE_NAME}.dbo.DT_DropItem r ON e.DDrop = r.DDrop
        LEFT JOIN {DATABASE_NAME}.dbo.DT_Item c ON r.DItem = c.IID
        LEFT JOIN {DATABASE_NAME}.dbo.DT_ItemResource i ON c.IID = i.ROwnerID AND i.RType = 2
        WHERE a.MID = ? AND c.IIsEvent = 0
        ORDER BY r.DItem
        """
        cursor.execute(query, (monster_id,))

        # Dictionary to store unique items and count duplicates
        unique_results = {}

        for row in cursor.fetchall():
            # Get monster class info from Google Sheets data
            monster_class_info = monster_class_df[
                monster_class_df['MClass'] == row.mClass
                ]['MName'].iloc[0] if not monster_class_df.empty else ''

            # Use DItem as key
            key = row.DItem

            pic = None
            if row.RFileName and row.RPosX is not None and row.RPosY is not None:
                pic = f"{GITHUB_URL}{row.RFileName.split('.')[0]}_{row.RPosX}_{row.RPosY}.png"

            if key not in unique_results:
                # If item appears for the first time, create new entry
                unique_results[key] = {
                    "MID": row.MID,
                    "MName": row.MName,
                    "MClass": monster_class_info,  # Added monster class info from Google Sheets
                    "DDropType": row.DDropType,
                    "DPercentGroup": row.GroupDropChance,
                    "DGroup": row.DropGroupID,
                    "DName": row.Description,
                    "DDrop": row.DDropID,
                    "DPercentItem": round(float(row.ItemDropChance), 1),
                    "DItem": row.DItem,
                    "IName": row.ItemName,
                    "DNumber": row.Quantity,
                    "Pic": pic if pic else f"{GITHUB_URL}no_item_image.png",
                    "count": 1
                }
            else:
                # If item already exists, increment counter and update quantity
                unique_results[key]["count"] += 1
                unique_results[key]["DNumber"] += row.Quantity

        # Convert dictionary back to list
        results = list(unique_results.values())

        # Sort results by DItem
        results.sort(key=lambda x: x["DItem"])

        return results


def get_monsters_by_class(class_ids: List[int]) -> Tuple[List[Tuple], Dict]:
    """Get monsters by class IDs"""
    base_github_url = "https://raw.githubusercontent.com/Aksel911/R2-HTML-DB/main/static/"

    with get_db_connection() as conn:
        cursor = conn.cursor()
        class_str = ','.join(str(c) for c in class_ids)
        query = f"""
            SELECT MID, MName, MClass 
            FROM DT_Monster 
            WHERE MClass IN ({class_str}) 
            ORDER BY MID
        """
        cursor.execute(query)
        monsters = [(row.MID, row.MName, row.MClass) for row in cursor.fetchall()]

        # Get file paths - без проверок существования
        file_paths = {
            monster[0]: f"{base_github_url}{monster[0]}.png"
            for monster in monsters
        }

        return monsters, file_paths



# ! CRAFT

# Рецепт крафта
def check_base_items_for_craft(item_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
        SELECT DISTINCT
  a.RID,
  a.RItemID0,
  b.IName,
  c.RItemID,
  b1.IName AS 'CraftItems',
  a.RSuccess,
  a.RIsCreateCnt,
  c.ROrderNo
FROM
  DT_Refine AS a
  INNER JOIN DT_Item AS b ON ( a.RItemID0 = b.IID )
  INNER JOIN DT_RefineMaterial AS c ON ( a.RID = c.RID )
  INNER JOIN DT_Item AS b1 ON ( c.RItemID = b1.IID ) 
WHERE
  a.RItemID0 = ? 
ORDER BY
  a.RID, c.ROrderNo"""

        cursor.execute(query, (item_id,))
        craft_results = cursor.fetchall()

        # Используем словарь для хранения уникальных записей
        unique_results = {}

        for row in craft_results:
            # Используем RItemID как ключ для уникальности
            key = row.RItemID

            # Обновляем запись только если её ещё нет или если это первое появление
            if key not in unique_results:
                item_resource = get_item_resource(row.RItemID)

                if item_resource:
                    file_name = item_resource.RFileName.split('.')[0]
                    image_path = f"{GITHUB_URL}{file_name}_{item_resource.RPosX}_{item_resource.RPosY}.png"
                else:
                    image_path = f"{GITHUB_URL}no_item_image.png"

                unique_results[key] = {
                    'RID': row.RID,
                    'RItemID0': row.RItemID0,
                    'IName': row.IName,
                    'RItemID': row.RItemID,
                    'CraftItems': row.CraftItems,
                    'RSuccess': round(float(row.RSuccess), 1),
                    'RIsCreateCnt': row.RIsCreateCnt,
                    'ROrderNo': row.ROrderNo,
                    'ImagePath': image_path
                }

        # Преобразуем словарь обратно в список
        return list(unique_results.values())


# Нужен для крафта
def check_next_craft_item(item_id: int):
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
SELECT DISTINCT
  a.RID,
  a.RItemID0,
  b.IName,
  a.RSuccess,
  a.RIsCreateCnt
FROM
  DT_Refine AS a
  INNER JOIN DT_Item AS b ON ( a.RItemID0 = b.IID )
  INNER JOIN DT_RefineMaterial AS c ON ( a.RID = c.RID )
  INNER JOIN DT_Item AS b1 ON ( c.RItemID = b1.IID )
WHERE
  c.RItemID = ?
ORDER BY
  a.RID"""
        cursor.execute(query, (item_id,))
        craft_results = cursor.fetchall()

        # Используем словарь для хранения уникальных записей
        unique_results = {}

        for row in craft_results:
            # Используем RItemID0 как ключ для уникальности
            key = row.RItemID0

            # Обновляем запись только если её ещё нет
            if key not in unique_results:
                item_resource = get_item_resource(row.RItemID0)

                if item_resource:
                    file_name = item_resource.RFileName.split('.')[0]
                    image_path = f"{GITHUB_URL}{file_name}_{item_resource.RPosX}_{item_resource.RPosY}.png"
                else:
                    image_path = f"{GITHUB_URL}no_item_image.png"

                unique_results[key] = {
                    'RID': row.RID,
                    'RItemID0': row.RItemID0,
                    'IName': row.IName,
                    'RSuccess': round(float(row.RSuccess), 1),
                    'RIsCreateCnt': row.RIsCreateCnt,
                    'ImagePath': image_path
                }

        # Преобразуем словарь обратно в список
        return list(unique_results.values())



# ! MERCHANTS

def get_payment_type_name(payment_type):
    payment_types = {
        0: "Серебра",
        1: "Очков чести",
        2: "Очков хаоса",
        3: "ШОПа"
    }
    return payment_types.get(payment_type, "Неизвестная валюта")


def get_merchant_sell_list():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = f"""
            SELECT
              a.ListID,
              c.MID,
              c.MName,
              c.MClass,
              a.ItemID,
              d.IName,
              a.Price,
              b.mPaymentType 
            FROM
              {DATABASE_NAME}.[dbo].[TblMerchantSellList] AS a
              LEFT JOIN {DATABASE_NAME}.[dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
              LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
              LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Item] AS d ON ( a.ItemID = d.IID ) 
            ORDER BY
              c.MName DESC 
        """
        cursor.execute(query)
        merchants_data = [(row.ListID, row.MID, (row.MName.replace('/n', ' ') if row.MName else ''), row.MClass,
                           row.ItemID, row.IName, row.Price, row.mPaymentType) for row in cursor.fetchall()]

        # Get file paths - без проверок существования
        file_paths = {
            monster[0]: f"{GITHUB_URL}{monster[1]}.png"
            for monster in merchants_data
        }

        return merchants_data, file_paths


def get_merchant_sellers(item_id: int) -> List[Dict]:
    """Get merchants selling a specific item"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = f"""
            SELECT
              a.ListID,
              c.MID,
              c.MName,
              a.Price,
              b.mPaymentType 
            FROM
              {DATABASE_NAME}.[dbo].[TblMerchantSellList] AS a
              LEFT JOIN {DATABASE_NAME}.[dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
              LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
            WHERE a.ItemID = ?
            ORDER BY c.MName
        """
        cursor.execute(query, (item_id,))
        merchants = []

        for row in cursor.fetchall():
            if row.MID:  # Проверяем, что торговец существует
                merchants.append({
                    "MerchantID": row.MID,
                    "MerchantName": row.MName.replace('/n', ' ') if row.MName else '',
                    "Price": row.Price,
                    "PaymentType": get_payment_type_name(row.mPaymentType)
                })
        return merchants



# ! SKILLS

def get_skill_icon_path(sprite_file, sprite_x, sprite_y, default_icon="no_monster/no_monster_image.png"):
    """
    Формирует путь к файлу иконки на основе данных спрайта

    Args:
        sprite_file (str): Имя файла спрайта
        sprite_x (int): X координата в спрайте
        sprite_y (int): Y координата в спрайте
        default_icon (str): Имя файла дефолтной иконки

    Returns:
        str: Полный путь к файлу иконки
    """
    try:
        if not sprite_file:
            return f"{GITHUB_URL}{default_icon}"

        # Убираем расширение .dds если оно есть
        if sprite_file.endswith(".dds"):
            sprite_file = sprite_file[:-4]

        # Проверяем наличие координат
        if sprite_x is not None and sprite_y is not None:
            return f"{GITHUB_URL}{sprite_file}_{sprite_x}_{sprite_y}.png"
        else:
            return f"{GITHUB_URL}{default_icon}"

    except Exception as e:
        print(f"Error creating icon path: {e}")
        return f"{GITHUB_URL}{default_icon}"

def get_skills_list():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = f"""
                SELECT
                  c.SID,
                  c.SName,
                  a.mSPID,
                  a.mName,
                  a.mDesc,
                  a.mSpriteFile,
                  a.mSpriteX,
                  a.mSpriteY 
                FROM
                  DT_SkillPack AS a
                  LEFT JOIN DT_SkillPackSkill AS b ON ( a.mSPID = b.mSPID )
                  LEFT JOIN DT_Skill AS c ON ( b.mSID = c.SID ) 
                ORDER BY
                  c.SID
        """
        cursor.execute(query)
        # Преобразуем в список кортежей, как в рабочем примере
        skills_data = [(row.SID,
                       (row.SName.replace('/n', ' ') if row.SName else ''),
                       row.mSPID,
                        row.mName,
                       (row.mDesc.replace('/n', ' ') if row.mDesc else ''),
                       row.mSpriteFile,
                       row.mSpriteX,
                       row.mSpriteY) for row in cursor.fetchall()]

        # Формируем пути к файлам
        file_paths = {
            skill[0]: get_skill_icon_path(
                skill[5],  # mSpriteFile
                skill[6],  # mSpriteX
                skill[7]   # mSpriteY
            )
            for skill in skills_data
        }

        return skills_data, file_paths


def get_skill_detail(skill_id: int) -> Optional[Skill]:
    """Get skill details by ID"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT
                a.SID,
                a.SName,
                a.SDesc,
                a.SHitPlus,
                a.SMPPerUse,
                a.SType,
                b.SName as 'STypeDesc',
                a.SHPPerUse,
                a.SChaoUse,
                a.mApplyRadius,
                a.mApplyRace,
                a.mCastingDelay,
                a.mConsumeItem,
                a.mActiveType,
                a.mAnimation,
                a.mCastingSpeed,
                a.mSkillEffect,
                a.mCoolTime,
                a.mConsumeItem2,
                a.mConsumeItemCnt2,
                c1.IID,
                c1.IName,
                c1.IUseLevel,
                c1.IUseClass,
                d1.mSPID,
                d1.mDesc,
                
                
                e.[AbnormalID],
                e1.ADesc,
                e1.AType,
                e1.ALevel,
                e2.AEffect,
                
                
                f.[MID],
                g.MType,
                g1.MName,
                g1.MDesc as 'ModuleDesc',
                g.Mlevel,
                g.MAParam,
                g1.MAParamName,
                g.MBParam,
                g1.MBParamName,
                g.MCParam,
                g1.MCParamName 
                
            FROM DT_SKill as a
            
            
            
            
            LEFT JOIN TP_SkillType as b ON (a.SType = b.SType)
            LEFT OUTER JOIN dbo.DT_ItemSkill as c ON (c.SID = a.SID)
            LEFT OUTER JOIN dbo.DT_Item as c1 ON (c1.IID = c.IID)
            LEFT OUTER JOIN dbo.DT_SkillPackSkill AS d ON (a.SID = d.mSID)
            LEFT OUTER JOIN dbo.DT_SkillPack AS d1 ON (d1.mSPID = d.mSPID)
            
            LEFT OUTER JOIN DT_SkillAbnormal AS e ON ( e.[SID] = a.[SID] ) 
            LEFT OUTER JOIN DT_Abnormal as e1 on ( e1.AID = e.AbnormalID )
            LEFT OUTER JOIN TP_AbnormalType as e2 on ( e2.AType = e1.AType )


            LEFT OUTER JOIN DT_AbnormalModule AS f ON ( e.[AbnormalID] = f.[AID] )
            LEFT OUTER JOIN DT_Module AS g ON ( f.[MID] = g.[MID] )
            LEFT OUTER JOIN TP_ModuleType AS g1 ON ( g1.MType = g.MType )

            WHERE a.SID = ?
        """
        cursor.execute(query, (skill_id,))
        row = cursor.fetchone()

        if not row:
            return None

        item_id = row.IID
        item_pic = get_item_resource(item_id)

        def clean_dict(d):
            return {k: v for k, v in d.items() if v is not None}


        abnormal_data = clean_dict({
            "AbnormalID": row.AbnormalID,
            "ADesc": row.ADesc.replace('\\n', ''),
            "AType": row.AType,
            "ALevel": row.ALevel,
            "AEffect": row.AEffect,
        })

        module_params = [
            {"name": name, "value": value}
            for name, value in [
                (row.MAParamName.replace('\\n', ''), row.MAParam),
                (row.MBParamName.replace('\\n', ''), row.MBParam),
                (row.MCParamName.replace('\\n', ''), row.MCParam)
            ]
            if name is not None and value is not None
        ]

        module_data = clean_dict({
            "module_id": row.MID,
            "type": row.MType,
            "type_name": row.MName,
            "type_desc": row.ModuleDesc,
            "level": row.Mlevel,
            "params": module_params if module_params else None
        })



        #print(module_data)
        return Skill(
            sid=row.SID,
            name=row.SName,
            desc=row.SDesc,
            hit_plus=row.SHitPlus,
            mp_per_use=row.SMPPerUse,
            skill_type=row.SType,
            type_desc=row.STypeDesc,
            hp_per_use=row.SHPPerUse,
            chao_use=row.SChaoUse,
            apply_radius=row.mApplyRadius,
            apply_race=row.mApplyRace,
            casting_delay=row.mCastingDelay,
            consume_item=row.mConsumeItem,
            active_type=row.mActiveType,
            animation=row.mAnimation,
            casting_speed=row.mCastingSpeed,
            skill_effect=row.mSkillEffect,
            cool_time=row.mCoolTime,
            consume_item2=row.mConsumeItem2,
            consume_item_cnt2=row.mConsumeItemCnt2,
            item_id=row.IID,
            item_pic=item_pic,
            item_name=row.IName,
            item_use_level=row.IUseLevel,
            item_use_class=row.IUseClass,
            skill_pack_id=row.mSPID,
            skill_pack_desc=row.mDesc,
            abnormal_data=abnormal_data,
            module_data=module_data
        )


# Получить предметы на которых скилл
def get_skill_use_by_spid_items(spid_id: int) -> Optional[Tuple]:
    """Get skill details by ID"""
    if spid_id is None:
        return None

    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
        SELECT
        a.MID,
        b1.AID,
        c1.SID,
        c1.SName,
        d1.IID,
        d1.IName
        FROM DT_Module AS a
        INNER JOIN DT_AbnormalModule AS b ON (a.MID = b.MID)
        INNER JOIN DT_Abnormal AS b1 ON (b.AID = b1.AID)
        INNER JOIN DT_SkillAbnormal AS c ON (b1.AID = c.AbnormalID)
        INNER JOIN DT_Skill AS c1 ON (c.SID = c1.SID)
        INNER JOIN DT_ItemSkill AS d ON (c1.SID = d.SID)
        INNER JOIN DT_Item AS d1 ON (d.IID = d1.IID)
        WHERE a.MType = 101 AND a.MAParam = ?
        """
        try:
            cursor.execute(query, (spid_id,))
            row = cursor.fetchone()
            #print(row)
            if not row:
                return None

            skill_for_item_data = (row.AID, row.SID, row.SName, row.IID, row.IName)

            item_id = row.IID
            skill_for_item_pic = get_item_resource(item_id)

            if skill_for_item_pic and isinstance(skill_for_item_pic, DT_ItemResource):
                skill_for_item_pic = skill_for_item_pic.file_path

            return skill_for_item_data, skill_for_item_pic

        except Exception as e:
            print(f"Error in get_skill_use_by_spid: {e}")
            return None

# Получить скилл создания скилла
def get_skill_use_by_sid(spid_id: int) -> Optional[Tuple]:
    """Get skill details by ID"""
    if spid_id is None:
        return None

    with get_db_connection() as conn:
        cursor = conn.cursor()
        # query = """
        #     SELECT
        #       a.SID,
        #       a.SName,
        #       c1.AID,
        #       v1.MID,
        #       v1.MType,
        #       v1.MAParam,
        #       g.mSPID,
        #       g.mSpriteFile,
        #       g.mSpriteX,
        #       g.mSpriteY
        #     FROM
        #       DT_Skill AS a
        #       INNER JOIN DT_SkillAbnormal AS c ON ( a.SID = c.SID )
        #       INNER JOIN DT_Abnormal AS c1 ON ( c.AbnormalID = c1.AID )
        #       INNER JOIN DT_AbnormalModule AS v ON ( c1.AID = v.AID )
        #       INNER JOIN DT_Module AS v1 ON ( v.MID = v1.MID )
        #       INNER JOIN DT_SkillPack AS g ON ( v1.MAParam = g.mSPID )
        #     WHERE
        #       a.SID = ?
        # """
        query = """
            SELECT
              a.MID,
              b1.AID,
              c1.SID,
              c1.SName,
              e1.mSPID,
              e1.mSpriteFile,
              e1.mSpriteX,
              e1.mSpriteY,
              d1.IID,
              d1.IName 
            FROM
              DT_Module AS a
              INNER JOIN DT_AbnormalModule AS b ON ( a.MID = b.MID )
              INNER JOIN DT_Abnormal AS b1 ON ( b.AID = b1.AID )
              INNER JOIN DT_SkillAbnormal AS c ON ( b1.AID = c.AbnormalID )
              INNER JOIN DT_Skill AS c1 ON ( c.SID = c1.SID )
              LEFT JOIN DT_SkillPackSkill AS e ON ( c1.SID = e.mSID )
              LEFT JOIN DT_SkillPack AS e1 ON ( e.mSPID = e1.mSPID )
              INNER JOIN DT_ItemSkill AS d ON ( c1.SID = d.SID )
              INNER JOIN DT_Item AS d1 ON ( d.IID = d1.IID ) 
            WHERE
              a.MType = 101 
              AND a.MAParam = ?
        """
        try:
            cursor.execute(query, (spid_id,))
            row = cursor.fetchone()
            print(row)
            if not row:
                return None

            #skill_for_skill_data = (row.SID, row.SName, row.AID, row.MID, row.MType, row.MAParam, row.mSPID, row.mSpriteFile, row.mSpriteX, row.mSpriteY)
            skill_for_skill_data = (row.AID, row.SID, row.SName, row.mSPID, row.mSpriteFile, row.mSpriteX, row.mSpriteY, row.IID, row.IName)

            skill_for_skill_pic = get_skill_icon_path(row.mSpriteFile, row.mSpriteX, row.mSpriteY)


            return skill_for_skill_data, skill_for_skill_pic

        except Exception as e:
            print(f"Error in get_skill_use_by_sid: {e}")
            return None



# *Routes
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/item/<int:item_id>')
def item_detail(item_id: int):
    """Item detail page"""
    item = get_item_by_id(item_id)
    use_class = item.IUseClass.split('/')[-1].replace('.png', '')
    use_class = int(use_class)
    #print(f"{item.IType} {use_class}")

    if not item:
        return "Item not found", 404

    item_resource = get_item_resource(item_id)
    if not item_resource:
        return "Item resource not found", 404

    mondropinfo = get_monster_drop_info(item_id)
    merchant_sellers = get_merchant_sellers(item_id)
    craft_items = check_base_items_for_craft(item_id)
    craft_next_item = check_next_craft_item(item_id)

    skill_data = get_item_skill(item_id)
    if skill_data:
        itemdskill_data, itemskill_pic = skill_data
    else:
        itemdskill_data, itemskill_pic = None, None

    # Get item model number
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = "SELECT RPosX, RPosY FROM DT_ItemResource WHERE ROwnerID = ? AND RType = 0"
        cursor.execute(query, (item_id,))
        model_result = cursor.fetchone()
        item_model_no = None
        prefix = None  # Добавляем переменную для префикса

        if model_result:
            base = f"{int(model_result.RPosX):03}{int(model_result.RPosY):03}"
            final = base

            if item.IType == 3:  # Armor
                prefix = 'p'  # Используем одну букву вместо кортежа
                replace_dict = {
                    1: [0, 1],
                    2: [2, 3],
                    4: [4, 5],
                    5: [0, 1, 4, 5],
                    7: [4, 5, 0, 1, 2, 3],
                    8: [6, 7],  # Ассасин
                    15: [0, 1, 2, 3, 4, 5, 6, 7],
                    16: [8, 9],
                    18: [8, 9, 2, 3],
                    19: [8, 9, 2, 3, 0, 1],
                    20: [8, 9, 4, 5],
                    22: [8, 9, 4, 5, 2, 3],
                    23: [0, 1, 2, 3, 4, 5, 8, 9],
                    0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    255: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
                }
                if use_class in replace_dict:
                    for index in replace_dict[use_class]:
                        final = f"0{index}0{base[3:]}"
                        #print(f"FINAL:{final}")

                        #model_url = f"https://raw.githubusercontent.com/Aksel911/R2-HTML-DB/main/static/models/{prefix}{final}/{prefix}{final}.glb"
                        #print(f"Model URL: {model_url}")

                    item_model_no = final
            elif item.IType in [1, 18, 20, 2, 19]:  # Weapons / Shield / Arrows
                prefix = 'i'  # Используем одну букву вместо кортежа
                item_model_no = base
            else:
                prefix = 'i'  # TODO: ЗАГЛУШКА ДЛЯ ОСТАЛЬНОГО!
                item_model_no = base

    return render_template(
        'item_core/item_page_detail.html',
        item=item,
        file_path=item_resource.file_path,
        mondropinfo=mondropinfo,
        merchant_sellers=merchant_sellers,
        monstermodelno_result=item_model_no,
        prefix=prefix,  # Добавляем префикс в рендер
        use_class=use_class,
        craft_result=craft_items,  # Рецепт
        craft_next=craft_next_item,  # Next item
        itemdskill_data=itemdskill_data, # Skill
        itemskill_pic=itemskill_pic # Skill Picture
    )


# @app.route('/monster/<int:monster_id>')
# def monster_detail(monster_id: int):
#     """Monster detail page"""
#     monster = get_monster_by_id(monster_id)
#     if not monster:
#         return "Monster not found", 404
#
#     with get_db_connection() as conn:
#         cursor = conn.cursor()
#
#         # Get class info
#         cursor.execute(
#             f"SELECT MName FROM {DATABASE_NAME}1602.dbo.TP_MonsterClass WHERE MClass = ?",
#             (monster['MClass'],)
#         )
#         class_info = {"MName": cursor.fetchone()[0]}
#
#         # Get race info
#         cursor.execute(
#             f"SELECT mDesc FROM {DATABASE_NAME}1602.dbo.TP_MonsterRaceType WHERE MRaceType = ?",
#             (monster['mRaceType'],)
#         )
#         race_result = cursor.fetchone()
#         race_info = {"mDesc": race_result[0] if race_result else None}
#
#         # Get respawn time
#         cursor.execute(
#             f"SELECT mTick FROM {DATABASE_NAME}.dbo.TblMonsterSpot WHERE mMID = ?",
#             (monster_id,)
#         )
#         respawn_result = cursor.fetchone()
#         respawn_time = respawn_result[0] if respawn_result else 1000
#         respawn_info = {
#             "mTick": respawn_time / 1000,
#             "mTickms": respawn_time
#         }
#
#         # Get monster location
#         cursor.execute(
#             f"SELECT Location, LocationLevel FROM {DATABASE_NAME}1602.dbo.DT_MonsterLocation WHERE MID = ?",
#             (monster_id,)
#         )
#         location_result = cursor.fetchone()
#         monster_location = None
#         if location_result:
#             monster_location = {
#                 "Location": location_result.Location,
#                 "LocationLevel": location_result.LocationLevel
#             }
#
#         # Get Merchant items
#         merchant_items = []
#         cursor.execute(
#             f"""
#             SELECT
#               a.ListID,
#               c.MID,
#               c.MName,
#               c.MClass,
#               a.ItemID,
#               d.IName,
#               a.Price,
#               b.mPaymentType
#             FROM
#               {DATABASE_NAME}.[dbo].[TblMerchantSellList] AS a
#               LEFT JOIN {DATABASE_NAME}.[dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
#               LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
#               LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Item] AS d ON ( a.ItemID = d.IID )
#             WHERE c.MID = ?
#             """,
#             (monster_id,)
#         )
#         merchant_results = cursor.fetchall()
#
#         if merchant_results:
#             for merchant_result in merchant_results:
#                 merch_pic = None
#                 merch_item_pics = get_item_resource(merchant_result.ItemID)
#
#                 if merch_item_pics:
#                     if merch_item_pics.RFileName and merch_item_pics.RPosX is not None and merch_item_pics.RPosY is not None:
#                         merch_pic = f"{GITHUB_URL}{merch_item_pics.RFileName.split('.')[0]}_{merch_item_pics.RPosX}_{merch_item_pics.RPosY}.png"
#
#                 merchant_items.append({
#                     "MerchantListID": merchant_result.ListID,
#                     "MerchantItemID": merchant_result.ItemID,
#                     "MerchantItemName": merchant_result.IName,
#                     "MerchantItemPrice": merchant_result.Price,
#                     "MerchantPaymentType": get_payment_type_name(merchant_result.mPaymentType),
#                     "MerchantItemPicture": merch_pic,
#                 })
#
#         # Get monster model number and set prefix
#         cursor.execute(
#             f"SELECT RFileName FROM {DATABASE_NAME}.dbo.DT_MonsterResource WHERE ROwnerID = ?",
#             (monster_id,)
#         )
#         model_result = cursor.fetchone()
#         monster_model_no = None
#         prefix = 'm'  # Устанавливаем префикс 'm' для всех монстров
#
#         if model_result:
#             monster_model_no = f"{int(model_result.RFileName):05}"
#
#     # Handle images
#     file_path = f"{GITHUB_URL}{monster_id}.png"
#     file_path_gif = f"{GITHUB_URL}gif/{monster_id}_IDLE.gif"
#     try:
#         response = requests.head(file_path_gif)
#         if response.status_code != 200:
#             file_path_gif = None
#     except:
#         file_path_gif = None
#
#     return render_template(
#         'monster_core/monster_page_detail.html',
#         item=monster,
#         file_path=file_path,
#         file_path_gif=file_path_gif,
#         classinfo=class_info,
#         raceinfo=race_info,
#         respawntimeinfo=respawn_info,
#         monlocationinfo=monster_location,
#         merchant_items=merchant_items,
#         mondropinfo=get_monster_drops(monster_id),
#         monstermodelno_result=monster_model_no,
#         prefix=prefix  # Добавляем префикс в контекст шаблона
#     )


# Item type routes
@app.route('/monster/<int:monster_id>')
def monster_detail(monster_id: int):
    """Monster detail page"""
    monster = get_monster_by_id(monster_id)
    if not monster:
        return "Monster not found", 404

    # Fetch data from Google Sheets
    monster_class_df = get_google_sheets_data(MONSTER_CLASS_URL)
    monster_race_df = get_google_sheets_data(MONSTER_RACE_URL)
    monster_location_df = get_google_sheets_data(MONSTER_LOCATION_URL)

    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Get class info from Google Sheets
        class_info = {"MName": ""}
        if not monster_class_df.empty:
            class_match = monster_class_df[monster_class_df['MClass'] == monster['MClass']]
            if not class_match.empty:
                class_info = {"MName": class_match.iloc[0]['MName']}

        # Get race info from Google Sheets
        race_info = {"mDesc": None}
        if not monster_race_df.empty:
            race_match = monster_race_df[monster_race_df['MRaceType'] == monster['mRaceType']]
            if not race_match.empty:
                race_info = {"mDesc": race_match.iloc[0]['mDesc']}

        # Get respawn time
        cursor.execute(
            f"SELECT mTick FROM {DATABASE_NAME}.dbo.TblMonsterSpot WHERE mMID = ?",
            (monster_id,)
        )
        respawn_result = cursor.fetchone()
        respawn_time = respawn_result[0] if respawn_result else 1000
        respawn_info = {
            "mTick": respawn_time / 1000,
            "mTickms": respawn_time
        }

        # Get monster location from Google Sheets
        monster_location = None
        if not monster_location_df.empty:
            location_match = monster_location_df[monster_location_df['MID'] == monster_id]
            if not location_match.empty:
                location_level = location_match.iloc[0]['LocationLevel']

                # Проверяем является ли значение nan
                if pd.isna(location_level):
                    location_level = None

                monster_location = {
                    "Location": location_match.iloc[0]['Location'],
                    "LocationLevel": location_level
                }

        # Get Merchant items
        merchant_items = []
        cursor.execute(
            f"""
            SELECT
              a.ListID,
              c.MID,
              c.MName,
              c.MClass,
              a.ItemID,
              d.IName,
              a.Price,
              b.mPaymentType 
            FROM
              {DATABASE_NAME}.[dbo].[TblMerchantSellList] AS a
              LEFT JOIN {DATABASE_NAME}.[dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
              LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
              LEFT JOIN {DATABASE_NAME}.[dbo].[DT_Item] AS d ON ( a.ItemID = d.IID ) 
            WHERE c.MID = ?
            """,
            (monster_id,)
        )
        merchant_results = cursor.fetchall()

        if merchant_results:
            for merchant_result in merchant_results:
                merch_pic = None
                merch_item_pics = get_item_resource(merchant_result.ItemID)

                if merch_item_pics:
                    if merch_item_pics.RFileName and merch_item_pics.RPosX is not None and merch_item_pics.RPosY is not None:
                        merch_pic = f"{GITHUB_URL}{merch_item_pics.RFileName.split('.')[0]}_{merch_item_pics.RPosX}_{merch_item_pics.RPosY}.png"

                merchant_items.append({
                    "MerchantListID": merchant_result.ListID,
                    "MerchantItemID": merchant_result.ItemID,
                    "MerchantItemName": merchant_result.IName,
                    "MerchantItemPrice": merchant_result.Price,
                    "MerchantPaymentType": get_payment_type_name(merchant_result.mPaymentType),
                    "MerchantItemPicture": merch_pic,
                })

        # Get monster model number and set prefix
        cursor.execute(
            f"SELECT RFileName FROM {DATABASE_NAME}.dbo.DT_MonsterResource WHERE ROwnerID = ?",
            (monster_id,)
        )
        model_result = cursor.fetchone()
        monster_model_no = None
        prefix = 'm'  # Default prefix for all monsters

        if model_result:
            monster_model_no = f"{int(model_result.RFileName):05}"

    # Handle images
    file_path = f"{GITHUB_URL}{monster_id}.png"
    file_path_gif = f"{GITHUB_URL}gif/{monster_id}_IDLE.gif"
    try:
        response = requests.head(file_path_gif)
        if response.status_code != 200:
            file_path_gif = None
    except:
        file_path_gif = None

    return render_template(
        'monster_core/monster_page_detail.html',
        item=monster,
        file_path=file_path,
        file_path_gif=file_path_gif,
        classinfo=class_info,
        raceinfo=race_info,
        respawntimeinfo=respawn_info,
        monlocationinfo=monster_location,
        merchant_items=merchant_items,
        mondropinfo=get_monster_drops(monster_id),
        monstermodelno_result=monster_model_no,
        prefix=prefix
    )


@app.route('/skill/<int:skill_id>')
def skill_detail(skill_id: int):
    """Skill detail page"""
    skill = get_skill_detail(skill_id)



    spid_id = skill.skill_pack_id

    skill_for_item = get_skill_use_by_spid_items(spid_id)
    if skill_for_item:
        skill_for_item_data, skill_for_item_pic = skill_for_item
    else:
        skill_for_item_data, skill_for_item_pic = None, None

    skill_for_skill = get_skill_use_by_sid(spid_id)
    if skill_for_skill:
        skill_for_skill_data, skill_for_skill_pic = skill_for_skill
    else:
        skill_for_skill_data, skill_for_skill_pic = None, None

    if not skill:
        return "Skill not found", 404

    # Получаем информацию о классах использования
    use_class = None
    if skill.item_use_class:
        try:
            use_class = int(skill.item_use_class.split('/')[-1].replace('.png', ''))
        except (ValueError, AttributeError):
            pass

    # Получаем информацию о расах (из Google Sheets)
    skill_apply_race_df = get_google_sheets_data(SKILLAPPLYRACE_LOCATION_URL)
    race_info = None
    if not skill_apply_race_df.empty and skill.apply_race is not None:
        race_match = skill_apply_race_df[skill_apply_race_df['mApplyRace'] == skill.apply_race]
        if not race_match.empty:
            race_info = race_match.iloc[0]['mDesc']

    # Получаем иконку скилла
    skill_icon = None
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT mSpriteFile, mSpriteX, mSpriteY 
            FROM DT_SkillPack a
            LEFT JOIN DT_SkillPackSkill b ON (a.mSPID = b.mSPID)
            WHERE b.mSID = ?
        """, (skill_id,))
        icon_data = cursor.fetchone()
        if icon_data:
            skill_icon = get_skill_icon_path(
                icon_data.mSpriteFile,
                icon_data.mSpriteX,
                icon_data.mSpriteY
            )

    return render_template(
        'skill_core/skill_page_detail.html',
        skill=skill,
        use_class=use_class,
        race_info=race_info,
        skill_icon=skill_icon,
        skill_for_item_data=skill_for_item_data,
        skill_for_item_pic=skill_for_item_pic,
        skill_for_skill_data=skill_for_skill_data,
        skill_for_skill_pic=skill_for_skill_pic
    )






# *Weapon and items routes
@app.route('/weapon')
def weapon():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([1, 18, 20], search_term)
    return render_template('weapon.html', items_wep=items, item_resources=file_paths)


@app.route('/armor')
def armor():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([3], search_term)
    return render_template('armor.html', items_wep=items, item_resources=file_paths)


@app.route('/gloves')
def gloves():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([7], search_term)
    return render_template('gloves.html', items_wep=items, item_resources=file_paths)


@app.route('/boots')
def boots():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([6], search_term)
    return render_template('boots.html', items_wep=items, item_resources=file_paths)


@app.route('/helmet')
def helmet():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([8], search_term)
    return render_template('helmet.html', items_wep=items, item_resources=file_paths)


@app.route('/shield')
def shield():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([2], search_term)
    return render_template('shield.html', items_wep=items, item_resources=file_paths)


@app.route('/arrows')
def arrows():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([19], search_term)
    return render_template('arrows.html', items_wep=items, item_resources=file_paths)


@app.route('/cloak')
def cloak():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([17], search_term)
    return render_template('cloak.html', items_wep=items, item_resources=file_paths)


@app.route('/materials')
def materials():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([10, 16], search_term)
    return render_template('materials.html', items_wep=items, item_resources=file_paths)


@app.route('/ring')
def ring():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([4], search_term)
    return render_template('ring.html', items_wep=items, item_resources=file_paths)


@app.route('/belt')
def belt():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([9], search_term)
    return render_template('belt.html', items_wep=items, item_resources=file_paths)


@app.route('/necklace')
def necklace():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([5], search_term)
    return render_template('necklace.html', items_wep=items, item_resources=file_paths)


@app.route('/earrings')
def earrings():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([42], search_term)
    return render_template('earrings.html', items_wep=items, item_resources=file_paths)


@app.route('/books')
def books():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([12], search_term)
    return render_template('books.html', items_wep=items, item_resources=file_paths)


@app.route('/potions')
def potions():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([10], search_term)
    return render_template('potions.html', items_wep=items, item_resources=file_paths)


@app.route('/etc')
def etc():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([14, 16, 13, 11], search_term)
    return render_template('etc.html', items_wep=items, item_resources=file_paths)


@app.route('/quest')
def quest():
    """Get quest items"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT mID FROM TblQuestCondition WHERE mType = 1")
        item_ids = [row.mID for row in cursor.fetchall()]

        if not item_ids:
            return render_template('quest.html', items_wep=[], item_resources={})

        items, file_paths = get_items_by_type(item_ids)
        return render_template('quest.html', items_wep=items, item_resources=file_paths)


@app.route('/event')
def event():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([15], search_term)
    return render_template('event.html', items_wep=items, item_resources=file_paths)


@app.route('/sphere')
def sphere():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([22, 23, 24, 25, 26, 27, 28, 29], search_term)
    return render_template('sphere.html', items_wep=items, item_resources=file_paths)





# *Monster routes with class filters
@app.route('/monster_regular')
def monster_regular():
    monsters, file_paths = get_monsters_by_class(
        [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 31, 32, 2]
    )
    return render_template('monster_regular.html', items=monsters, item_resources=file_paths)


@app.route('/monster_imennoy')
def monster_imennoy():
    monsters, file_paths = get_monsters_by_class([28])
    return render_template('monster_imennoy.html', items=monsters, item_resources=file_paths)


@app.route('/monster_boss')
def monster_boss():
    monsters, file_paths = get_monsters_by_class([29, 33, 34, 35, 36, 37, 38])
    return render_template('monster_boss.html', items=monsters, item_resources=file_paths)


@app.route('/monster_raidboss')
def monster_raid_boss():
    monsters, file_paths = get_monsters_by_class([26])
    return render_template('monster_raidboss.html', items=monsters, item_resources=file_paths)


@app.route('/monster_event')
def monster_event():
    monsters, file_paths = get_monsters_by_class([27])
    return render_template('monster_event.html', items=monsters, item_resources=file_paths)


@app.route('/monster_npc')
def monster_npc():
    monsters, file_paths = get_monsters_by_class([23, 35])
    return render_template('monster_npc.html', items=monsters, item_resources=file_paths)



# *Merchants Route
@app.route('/merchants')
def merchants_list():
    merchants_data, file_paths = get_merchant_sell_list()
    return render_template('merchants.html', items=merchants_data, item_resources=file_paths)



# *Skills Route
@app.route('/skills')
def skills_list():
    skills_data, file_paths = get_skills_list()
    return render_template('skills.html', skills=skills_data, item_resources=file_paths)





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=500)
