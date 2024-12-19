import os
import requests
from flask import Flask, render_template, request
import pyodbc
from os.path import splitext
from functools import lru_cache
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from contextlib import contextmanager
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


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
    return os.getenv('GITHUB_URL', 'https://raw.githubusercontent.com/Aksel911/R2-HTML-DB/main/static/')


required_env_vars = ['DB_USER', 'DB_PASSWORD']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing config required environment variables: {', '.join(missing_vars)}")

DATABASE_CONFIG = get_database_config()
GITHUB_URL = get_github_url()


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


# Cache decorators
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


def get_monster_drop_info(item_id: int) -> List[Dict]:
    """Get monster drop information for an item"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
        SELECT
            a.MID,
            a.MName,
            w.DDropType,
            q.DPercent as GroupDropChance,
            q.DGroup as DropGroupID,
            w.DName as Description,
            e.DDrop as DDropID,
            e.DPercent as ItemDropChance,
            r.DItem,
            c.IName as ItemName,
            r.DNumber as Quantity
        FROM DT_Monster a
        LEFT JOIN FNLParm1602.dbo.TP_MonsterClass b ON a.mClass = b.MClass
        LEFT JOIN FNLParm.dbo.DT_MonsterDrop q ON a.MID = q.MID
        LEFT JOIN FNLParm.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
        LEFT JOIN FNLParm.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
        LEFT JOIN FNLParm.dbo.DT_DropItem r ON e.DDrop = r.DDrop
        LEFT JOIN DT_Item c ON r.DItem = c.IID
        WHERE r.DItem = ? AND c.IIsEvent = 0
        ORDER BY a.MID
        """
        cursor.execute(query, (item_id,))

        unique_results = {}

        for row in cursor.fetchall():
            # Используем только MID как ключ для уникальности
            key = row.MID

            # Если такого монстра еще нет в результатах, добавляем его
            if key not in unique_results:
                monster_pic = f"{GITHUB_URL}{row.MID}.png"

                unique_results[key] = {
                    "MID": row.MID,
                    "MName": row.MName.replace('/n', ' ') if row.MName else '',
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
                row.IID, row.IName, row.IDesc, row.IWeight,
                row.IUseClass, row.IType, row.IMaxBeadHoleCount,
                row.ITermOfValidity
            )
            for row in cursor.fetchall()
        ]

        return items, file_paths


# Routes
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
        craft_result=craft_items, # Рецепт
        craft_next=craft_next_item # Next item
    )


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


def get_monster_drops(monster_id: int) -> List[Dict]:
    """Get all drops for a specific monster"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
        SELECT
            a.MID,
            a.MName,
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
        FROM DT_Monster a
        LEFT JOIN FNLParm1602.dbo.TP_MonsterClass b ON a.mClass = b.MClass
        LEFT JOIN FNLParm.dbo.DT_MonsterDrop q ON a.MID = q.MID
        LEFT JOIN FNLParm.dbo.TP_DropGroup w ON q.DGroup = w.DGroup
        LEFT JOIN FNLParm.dbo.DT_DropGroup e ON w.DGroup = e.DGroup
        LEFT JOIN FNLParm.dbo.DT_DropItem r ON e.DDrop = r.DDrop
        LEFT JOIN DT_Item c ON r.DItem = c.IID
        LEFT JOIN DT_ItemResource i ON c.IID = i.ROwnerID AND i.RType = 2
        WHERE a.MID = ? AND c.IIsEvent = 0
        ORDER BY r.DItem
        """
        cursor.execute(query, (monster_id,))

        # Словарь для хранения уникальных предметов и подсчета дубликатов
        unique_results = {}

        for row in cursor.fetchall():
            # Используем DItem как ключ
            key = row.DItem

            pic = None
            if row.RFileName and row.RPosX is not None and row.RPosY is not None:
                pic = f"{GITHUB_URL}{row.RFileName.split('.')[0]}_{row.RPosX}_{row.RPosY}.png"

            if key not in unique_results:
                # Если предмет встречается впервые, создаем новую запись
                unique_results[key] = {
                    "MID": row.MID,
                    "MName": row.MName,
                    "DDropType": row.DDropType,
                    "DPercentGroup": row.GroupDropChance,
                    "DGroup": row.DropGroupID,
                    "DName": row.Description,
                    "DDrop": row.DDropID,
                    "DPercentItem": round(float(row.ItemDropChance), 1),
                    "DItem": row.DItem,
                    "IName": row.ItemName,
                    "DNumber": row.Quantity,  # Начальное количество
                    "Pic": pic if pic else f"{GITHUB_URL}no_item_image.png",
                    "count": 1  # Счетчик дубликатов
                }
            else:
                # Если предмет уже есть, увеличиваем счетчик и обновляем количество
                unique_results[key]["count"] += 1
                unique_results[key]["DNumber"] += row.Quantity

        # Преобразуем словарь обратно в список
        results = list(unique_results.values())

        # Сортируем результаты по DItem
        results.sort(key=lambda x: x["DItem"])

        return results


@app.route('/monster/<int:monster_id>')
def monster_detail(monster_id: int):
    """Monster detail page"""
    monster = get_monster_by_id(monster_id)
    if not monster:
        return "Monster not found", 404

    with get_db_connection() as conn:
        cursor = conn.cursor()

        # Get class info
        cursor.execute(
            "SELECT MName FROM FNLParm1602.dbo.TP_MonsterClass WHERE MClass = ?",
            (monster['MClass'],)
        )
        class_info = {"MName": cursor.fetchone()[0]}

        # Get race info
        cursor.execute(
            "SELECT mDesc FROM FNLParm1602.dbo.TP_MonsterRaceType WHERE MRaceType = ?",
            (monster['mRaceType'],)
        )
        race_result = cursor.fetchone()
        race_info = {"mDesc": race_result[0] if race_result else None}

        # Get respawn time
        cursor.execute(
            "SELECT mTick FROM FNLParm.dbo.TblMonsterSpot WHERE mMID = ?",
            (monster_id,)
        )
        respawn_result = cursor.fetchone()
        respawn_time = respawn_result[0] if respawn_result else 1000
        respawn_info = {
            "mTick": respawn_time / 1000,
            "mTickms": respawn_time
        }

        # Get monster location
        cursor.execute(
            "SELECT Location, LocationLevel FROM FNLParm1602.dbo.DT_MonsterLocation WHERE MID = ?",
            (monster_id,)
        )
        location_result = cursor.fetchone()
        monster_location = None
        if location_result:
            monster_location = {
                "Location": location_result.Location,
                "LocationLevel": location_result.LocationLevel
            }

        # Get Merchant items
        merchant_items = []
        cursor.execute(
            """
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
              [dbo].[TblMerchantSellList] AS a
              LEFT JOIN [dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
              LEFT JOIN [dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
              LEFT JOIN [dbo].[DT_Item] AS d ON ( a.ItemID = d.IID ) 
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
            "SELECT RFileName FROM FNLParm.dbo.DT_MonsterResource WHERE ROwnerID = ?",
            (monster_id,)
        )
        model_result = cursor.fetchone()
        monster_model_no = None
        prefix = 'm'  # Устанавливаем префикс 'm' для всех монстров

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
        prefix=prefix  # Добавляем префикс в контекст шаблона
    )


# Item type routes
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


# Monster routes with class filters
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


# Sell Items
def get_payment_type_name(payment_type):
    payment_types = {
        0: "Серебра",
        1: "Очков чести",
        2: "Очков хаоса",
        3: "ШОПа"
    }
    return payment_types.get(payment_type, "Неизвестная валюта")


def get_merchant_sell_list():
    """Get monsters by class IDs"""
    base_github_url = "https://raw.githubusercontent.com/Aksel911/R2-HTML-DB/main/static/"

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
              [dbo].[TblMerchantSellList] AS a
              LEFT JOIN [dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
              LEFT JOIN [dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
              LEFT JOIN [dbo].[DT_Item] AS d ON ( a.ItemID = d.IID ) 
            ORDER BY
              c.MName DESC 
        """
        cursor.execute(query)
        merchants_data = [(row.ListID, row.MID, (row.MName.replace('/n', ' ') if row.MName else ''), row.MClass,
                           row.ItemID, row.IName, row.Price, row.mPaymentType) for row in cursor.fetchall()]

        # Get file paths - без проверок существования
        file_paths = {
            monster[0]: f"{base_github_url}{monster[1]}.png"
            for monster in merchants_data
        }

        return merchants_data, file_paths


def get_merchant_sellers(item_id: int) -> List[Dict]:
    """Get merchants selling a specific item"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        query = """
            SELECT
              a.ListID,
              c.MID,
              c.MName,
              a.Price,
              b.mPaymentType 
            FROM
              [dbo].[TblMerchantSellList] AS a
              LEFT JOIN [dbo].[TblMerchantName] AS b ON ( a.ListID = b.mID )
              LEFT JOIN [dbo].[DT_Monster] AS c ON ( b.mID = c.mSellMerchanID )
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


@app.route('/merchants')
def merchants_list():
    merchants_data, file_paths = get_merchant_sell_list()
    return render_template('merchants.html', items=merchants_data, item_resources=file_paths)


# Template filters
@app.template_filter('remove_extension')
def remove_extension(value):
    """Remove file extension from string"""
    return splitext(value)[0]





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
