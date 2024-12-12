import os
from flask import Flask, render_template, request
import pyodbc
from os.path import splitext

app = Flask(__name__)
conn_str = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=FNLParm;UID=sa;PWD=pass'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()


class DT_ITem:
    def __init__(self, IID, IName, IDesc, IWeight, IUseClass, IType, IMaxBeadHoleCount, ITermOfValidity):
        self.IID = IID
        self.IName = IName
        self.IDesc = IDesc
        self.IWeight = IWeight
        self.IUseClass = f"/static/class/{IUseClass}.png"
        self.IType = IType
        self.IMaxBeadHoleCount = IMaxBeadHoleCount
        self.ITermOfValidity = ITermOfValidity



class DT_ItemResource:
    def __init__(self, ROwnerID, RFileName, RPosX, RPosY):
        self.ROwnerID = ROwnerID
        self.RFileName = splitext(RFileName)[0]
        self.RPosX = RPosX
        self.RPosY = RPosY
        self.file_path = f"{self.RFileName}_{self.RPosX}_{self.RPosY}.png"


# Main HTML
@app.route('/')
def home():
    return render_template('home.html')


# All Items
@app.route('/item/<int:item_id>', methods=['GET'])
def item_detail(item_id):
    query = f"SELECT * FROM DT_ITem WHERE IID = {item_id}"
    cursor.execute(query)
    row = cursor.fetchone()
    item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)

    query = f"SELECT * FROM DT_ItemResource WHERE ROwnerID = {item_id} AND RType = 2"
    cursor.execute(query)
    row = cursor.fetchone()
    item_resource = DT_ItemResource(row.ROwnerID, row.RFileName, row.RPosX, row.RPosY)

    file_name = item_resource.RFileName.split('.')[0]
    pos_x = int(item_resource.RPosX)
    pos_y = int(item_resource.RPosY)
    file_path = f"{file_name}_{pos_x}_{pos_y}.png"

    # Item Drop
    qq5 = f"""SELECT
    a.[MID],
    a.[MName] as Имя,
    w.[DDropType] as Автодроп,
    q.[DPercent] as Шанс_Дропа_Группы,
    q.[DGroup] as ID_Drop_Группы,
    w.[DName] as Описание,
    e.[DDrop] as DDropID,
    e.[DPercent] as Шанс_Дропа_Предмета,
    r.[DItem] as ID_Предмета,
    c.[IName] as Имя_Предмета,
    r.[DNumber] as Количество,
    CASE
    WHEN c.IIsEvent = 1 THEN 'Ивентовый (1)'
    WHEN c.IIsEvent = 0 THEN 'Не ивентовый (0)'
    ELSE '[Неизвестно]'
    END AS 'Ивент'
    FROM
    dbo.DT_Monster AS a
    LEFT JOIN FNLParm1602.dbo.TP_MonsterClass AS b ON ( a.[mClass] = b.[MClass] )
    LEFT JOIN FNLParm.dbo.DT_MonsterDrop AS q ON (a.[MID] = q.[MID])
    LEFT JOIN FNLParm.dbo.TP_DropGroup AS w ON (q.[DGroup] = w.[DGroup])
    LEFT JOIN FNLParm.dbo.DT_DropGroup AS e ON (w.[DGroup] = e.[DGroup])
    LEFT JOIN FNLParm.dbo.DT_DropItem AS r ON (e.[DDrop] = r.[DDrop])
    LEFT JOIN dbo.DT_Item AS c ON ( r.[DItem] = c.[IID] )
    WHERE r.[DItem] = {item_id} AND c.IIsEvent = 0 ORDER BY a.[MID]"""
    cursor.execute(qq5)
    mondrop = cursor.fetchall()

    # Сначала соберите все значения из восьмой колонки в список
    values = [str(row[8]) for row in mondrop]

    # Затем вставьте эти значения в строку, разделённые запятой
    values_str = ",".join(values)

    print(values_str)
    if not values_str:
        values_str = 0

    mondropinfo = []
    for row in mondrop:
        row[7] = round(row[7], 2)
        item_path_mon = f"{row[0]}.png"  # Предполагается, что row[0] содержит имя файла картинки
        full_path = os.path.join('static', item_path_mon)
        if os.path.isfile(full_path):
            monpic = item_path_mon
        else:
            monpic = fr"no_monster_image.png"

        record = {"MID": row[0],
                  "MName": row[1],
                  "DDropType": row[2],
                  "DPercentGroup": row[3],
                  "DGroup": row[4],
                  "DName": row[5],
                  "DDrop": row[6],
                  "DPercentItem": row[7],
                  "DItem": row[8],
                  "IName": row[9],
                  "DNumber": row[10],
                  "Pic": monpic  # используем monpic
                  }
        mondropinfo.append(record)

    return render_template('item_detail.html', item=item, file_path=file_path, mondropinfo=mondropinfo)


# All Monsters
@app.route('/monster/<int:monster_id>', methods=['GET'])
def monster_detail(monster_id):
    query = f"SELECT MID, MName, MClass, MLevel, MHP, MMP, MExp, mRaceType, mIsShowHp, MChaotic, mDetectTransF, mDetectTransP, mDetectChao, mIsResistTransF FROM DT_Monster WHERE MID = {monster_id}"
    cursor.execute(query)
    row = cursor.fetchone()

    if row[8] is True:
        row[8] = 'Да'
    else:
        row[8] = 'Нет'

    if row[13] is True:
        row[13] = 'Да'
    else:
        row[13] = 'Нет'

    if row[10] == 1:
        row[10] = 'Да'
    else:
        row[10] = 'Нет'

    if row[11] == 1:
        row[11] = 'Да'
    else:
        row[11] = 'Нет'

    item = {
        "MID": row[0],
        "MName": row[1],
        "MClass": row[2],
        "MLevel": row[3],
        "MHP": row[4],
        "MMP": row[5],
        "mExp": row[6],
        "mRaceType": row[7],
        "mIsShowHp": row[8],
        "MChaotic": row[9],
        "mDetectTransF": row[10],
        "mDetectTransP": row[11],
        "mDetectChao": row[12],
        "mIsResistTransF": row[13]
    }

    # Class Type
    qq1 = f"SELECT MName FROM FNLParm1602.dbo.TP_MonsterClass WHERE MClass = {row[2]}"
    cursor.execute(qq1)
    classinf = cursor.fetchone()
    classinfo = {"MName": classinf[0]}

    # Race Type
    qq2 = f"SELECT mDesc FROM FNLParm1602.dbo.TP_MonsterRaceType WHERE MRaceType = {row[7]}"
    cursor.execute(qq2)
    raceinf = cursor.fetchone()
    if raceinf is None:
        raceinf = 0
    raceinfo = {"mDesc": raceinf[0]}

    # Respawn Time
    qq3 = f"SELECT mTick FROM FNLParm.dbo.TblMonsterSpot WHERE mMID = {row[0]}"
    cursor.execute(qq3)
    respawntime = cursor.fetchone()
    if respawntime is None:
        respawntime = 1

    if isinstance(respawntime, int):
        respawntime_sec = respawntime / 1000
        respawntimeinfo = {"mTick": respawntime_sec, "mTickms": respawntime}
    else:
        respawntime_sec = respawntime[0] / 1000
        respawntimeinfo = {"mTick": respawntime_sec, "mTickms": respawntime[0]}

    # Monster Location
    qq4 = f"SELECT Location, LocationLevel FROM FNLParm1602.dbo.DT_MonsterLocation WHERE MID = {row[0]}"
    cursor.execute(qq4)
    monloc = cursor.fetchone()
    monlocationinfo = None
    if monloc is not None:
        monlocationinfo = {"Location": monloc[0],
                        "LocationLevel": monloc[1]}



    # Monster Drop
    qq5 = f"""
    SELECT
    a.[MID],
    a.[MName] as Имя,
    w.[DDropType] as Автодроп,
    q.[DPercent] as Шанс_Дропа_Группы,
    q.[DGroup] as ID_Drop_Группы,
    w.[DName] as Описание,
    e.[DDrop] as DDropID,
    e.[DPercent] as Шанс_Дропа_Предмета,
    r.[DItem] as ID_Предмета,
    c.[IName] as Имя_Предмета,
    r.[DNumber] as Количество,
    CASE
    WHEN c.IIsEvent = 1 THEN 'Ивентовый (1)'
    WHEN c.IIsEvent = 0 THEN 'Не ивентовый (0)'
    ELSE '[Неизвестно]'
    END AS 'Ивент',
    i.RFileName, 
    i.RPosX, 
    i.RPosY
    FROM
    dbo.DT_Monster AS a
    LEFT JOIN FNLParm1602.dbo.TP_MonsterClass AS b ON ( a.[mClass] = b.[MClass] )
    LEFT JOIN FNLParm.dbo.DT_MonsterDrop AS q ON (a.[MID] = q.[MID])
    LEFT JOIN FNLParm.dbo.TP_DropGroup AS w ON (q.[DGroup] = w.[DGroup])
    LEFT JOIN FNLParm.dbo.DT_DropGroup AS e ON (w.[DGroup] = e.[DGroup])
    LEFT JOIN FNLParm.dbo.DT_DropItem AS r ON (e.[DDrop] = r.[DDrop])
    LEFT JOIN dbo.DT_Item AS c ON ( r.[DItem] = c.[IID] )
    LEFT JOIN dbo.DT_ItemResource AS i ON (c.[IID] = i.ROwnerID AND i.RType = 2)
    WHERE a.[MID] = {row[0]} AND c.IIsEvent = 0 ORDER BY r.[DItem]
    """
    cursor.execute(qq5)
    results = cursor.fetchall()

    mondropinfo = []
    for row in results:
        row[7] = round(row[7], 2)
        pic = f"{row[12].split('.')[0]}_{row[13]}_{row[14]}.png"
        record = {"MID": row[0],
                  "MName": row[1],
                  "DDropType": row[2],
                  "DPercentGroup": row[3],
                  "DGroup": row[4],
                  "DName": row[5],
                  "DDrop": row[6],
                  "DPercentItem": row[7],
                  "DItem": row[8],
                  "IName": row[9],
                  "DNumber": row[10],
                  "Pic": pic
                  }
        mondropinfo.append(record)

    file_path = f"{item['MID']}.png"
    full_path = os.path.join('static', file_path)
    if not os.path.isfile(full_path):
        file_path = fr"no_monster_image.png"


    file_path_gif = f"{item['MID']}_IDLE.gif"
    full_path_gif = os.path.join('static', 'gif', file_path_gif)
    if not os.path.isfile(full_path_gif):
        file_path_gif = None

    return render_template('monster_detail.html', item=item, file_path=file_path, file_path_gif=file_path_gif,
                           classinfo=classinfo, raceinfo=raceinfo, respawntimeinfo=respawntimeinfo, monlocationinfo=monlocationinfo, mondropinfo=mondropinfo)


# MONSTER REGULAR
@app.route('/monster_regular', methods=['GET'])
def monster_regular():
    query = f"SELECT MID, MName, MClass FROM DT_Monster WHERE MClass IN (1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 31, 32, 2) ORDER BY MID"
    cursor.execute(query)

    items = []
    for row in cursor.fetchall():
        MID = row[0]
        MName = row[1]
        MClass = row[2]

        item = MID, MName, MClass
        items.append(item)

    file_path = {}  # We are going to store file paths in a dictionary
    for item in items:
        item_path = f"{item[0]}.png"
        full_path = os.path.join('static', item_path)
        if os.path.isfile(full_path):
            file_path[item[0]] = item_path
        else:
            file_path[item[0]] = fr"no_monster_image.png"

    return render_template('monster_regular.html', items=items, item_resources=file_path)


# MONSTER IMENNOY
@app.route('/monster_imennoy', methods=['GET'])
def monster_imennoy():
    query = f"SELECT MID, MName, MClass FROM DT_Monster WHERE MClass IN (28) ORDER BY MID"
    cursor.execute(query)

    items = []
    for row in cursor.fetchall():
        MID = row[0]
        MName = row[1]
        MClass = row[2]

        item = MID, MName, MClass
        items.append(item)

    file_path = {}  # We are going to store file paths in a dictionary
    for item in items:
        item_path = f"{item[0]}.png"
        full_path = os.path.join('static', item_path)
        if os.path.isfile(full_path):
            file_path[item[0]] = item_path
        else:
            file_path[item[0]] = fr"no_monster_image.png"

    return render_template('monster_imennoy.html', items=items, item_resources=file_path)


# MONSTER BOSS
@app.route('/monster_boss', methods=['GET'])
def monster_boss():
    query = f"SELECT MID, MName, MClass FROM DT_Monster WHERE MClass IN (29, 33, 34, 35, 36, 37, 38) ORDER BY MID"
    cursor.execute(query)

    items = []
    for row in cursor.fetchall():
        MID = row[0]
        MName = row[1]
        MClass = row[2]

        item = MID, MName, MClass
        items.append(item)

    file_path = {}  # We are going to store file paths in a dictionary
    for item in items:
        item_path = f"{item[0]}.png"
        full_path = os.path.join('static', item_path)
        if os.path.isfile(full_path):
            file_path[item[0]] = item_path
        else:
            file_path[item[0]] = fr"no_monster_image.png"

    return render_template('monster_boss.html', items=items, item_resources=file_path)


# MONSTER RAID BOSS
@app.route('/monster_raidboss', methods=['GET'])
def monster_raid_boss():
    query = f"SELECT MID, MName, MClass FROM DT_Monster WHERE MClass IN (26) ORDER BY MID"
    cursor.execute(query)

    items = []
    for row in cursor.fetchall():
        MID = row[0]
        MName = row[1]
        MClass = row[2]

        item = MID, MName, MClass
        items.append(item)

    file_path = {}  # We are going to store file paths in a dictionary
    for item in items:
        item_path = f"{item[0]}.png"
        full_path = os.path.join('static', item_path)
        if os.path.isfile(full_path):
            file_path[item[0]] = item_path
        else:
            file_path[item[0]] = fr"no_monster_image.png"

    return render_template('monster_raidboss.html', items=items, item_resources=file_path)


# MONSTER EVENT
@app.route('/monster_event', methods=['GET'])
def monster_event():
    query = f"SELECT MID, MName, MClass FROM DT_Monster WHERE MClass IN (27) ORDER BY MID"
    cursor.execute(query)

    items = []
    for row in cursor.fetchall():
        MID = row[0]
        MName = row[1]
        MClass = row[2]

        item = MID, MName, MClass
        items.append(item)

    file_path = {}  # We are going to store file paths in a dictionary
    for item in items:
        item_path = f"{item[0]}.png"
        full_path = os.path.join('static', item_path)
        if os.path.isfile(full_path):
            file_path[item[0]] = item_path
        else:
            file_path[item[0]] = fr"no_monster_image.png"

    return render_template('monster_event.html', items=items, item_resources=file_path)


# MONSTER NPC
@app.route('/monster_npc', methods=['GET'])
def monster_npc():
    query = f"SELECT MID, MName, MClass FROM DT_Monster WHERE MClass IN (23, 35) ORDER BY MID"
    cursor.execute(query)

    items = []
    for row in cursor.fetchall():
        MID = row[0]
        MName = row[1]
        MClass = row[2]

        item = MID, MName, MClass
        items.append(item)

    file_path = {}  # We are going to store file paths in a dictionary
    for item in items:
        item_path = f"{item[0]}.png"
        full_path = os.path.join('static', item_path)
        if os.path.isfile(full_path):
            file_path[item[0]] = item_path
        else:
            file_path[item[0]] = fr"no_monster_image.png"

    return render_template('monster_npc.html', items=items, item_resources=file_path)


# ARMOR
@app.route('/armor', methods=['GET'])
def armor():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (3) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('armor.html', items_wep=items_wep, item_resources=file_paths)


# WEAPONS
@app.route('/weapon', methods=['GET'])
def weapon():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (1, 18, 20) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('weapon.html', items_wep=items_wep, item_resources=file_paths)


# GLOVES
@app.route('/gloves', methods=['GET'])
def gloves():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (7) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('gloves.html', items_wep=items_wep, item_resources=file_paths)


# BOOTS
@app.route('/boots', methods=['GET'])
def boots():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (6) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('boots.html', items_wep=items_wep, item_resources=file_paths)


# HELMET
@app.route('/helmet', methods=['GET'])
def helmet():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (8) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('helmet.html', items_wep=items_wep, item_resources=file_paths)


# SHIELD
@app.route('/shield', methods=['GET'])
def shield():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (2) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('shield.html', items_wep=items_wep, item_resources=file_paths)


# ARROWS
@app.route('/arrows', methods=['GET'])
def arrows():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (19) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('arrows.html', items_wep=items_wep, item_resources=file_paths)


# CLOAK
@app.route('/cloak', methods=['GET'])
def cloak():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (17) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('cloak.html', items_wep=items_wep, item_resources=file_paths)


# MATERIALS
@app.route('/materials', methods=['GET'])
def materials():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (10, 16) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('materials.html', items_wep=items_wep, item_resources=file_paths)


# RING
@app.route('/ring', methods=['GET'])
def ring():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (4) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('ring.html', items_wep=items_wep, item_resources=file_paths)


# BELT
@app.route('/belt', methods=['GET'])
def belt():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (9) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('belt.html', items_wep=items_wep, item_resources=file_paths)


# NECKLACE
@app.route('/necklace', methods=['GET'])
def necklace():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (5) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('necklace.html', items_wep=items_wep, item_resources=file_paths)


# EARRINGS
@app.route('/earrings', methods=['GET'])
def earrings():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (42) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('earrings.html', items_wep=items_wep, item_resources=file_paths)


# BOOKS
@app.route('/books', methods=['GET'])
def books():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (12) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('books.html', items_wep=items_wep, item_resources=file_paths)


# POTIONS
@app.route('/potions', methods=['GET'])
def potions():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (10) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('potions.html', items_wep=items_wep, item_resources=file_paths)


# ETC
@app.route('/etc', methods=['GET'])
def etc():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (14, 16, 13, 11) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('etc.html', items_wep=items_wep, item_resources=file_paths)


# QUEST
@app.route('/quest', methods=['GET'])
def quest():
    qq = f"SELECT mID FROM TblQuestCondition WHERE mType = 1"
    cursor.execute(qq)
    item_ids_wep = []
    cursor.execute(qq)
    for row in cursor.fetchall():
        item_ids_wep.append(row.mID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('quest.html', items_wep=items_wep, item_resources=file_paths)


# EVENT
@app.route('/event', methods=['GET'])
def event():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (15) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('event.html', items_wep=items_wep, item_resources=file_paths)


# SPHERE
@app.route('/sphere', methods=['GET'])
def sphere():
    search_term_wep = request.args.get('search', '')
    query = f"SELECT IID FROM DT_ITem WHERE IType IN (22, 23, 24, 25, 26, 27, 28, 29) AND IName LIKE '%{search_term_wep}%' ORDER BY IID"
    item_ids_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item_ids_wep.append(row.IID)

    item_ids_str = ', '.join(str(i) for i in item_ids_wep)
    query = f"SELECT RFileName, RPosX, RPosY, ROwnerID FROM DT_ItemResource WHERE ROwnerID IN ({item_ids_str}) AND RType = 2"
    item_resources_wep = []
    cursor.execute(query)
    file_paths = {}
    for row in cursor.fetchall():
        file_name = row[0]
        file_name = file_name.split('.')[0]
        posx = row[1]
        posy = row[2]
        owner_id = row[3]
        file_path = f"{file_name}_{posx}_{posy}.png"
        file_paths[owner_id] = file_path

    query = f"SELECT * FROM DT_ITem WHERE IID IN ({item_ids_str})"
    items_wep = []
    cursor.execute(query)
    for row in cursor.fetchall():
        item = DT_ITem(row.IID, row.IName, row.IDesc, row.IWeight, row.IUseClass, row.IType, row.IMaxBeadHoleCount, row.ITermOfValidity)
        items_wep.append(item)

    return render_template('sphere.html', items_wep=items_wep, item_resources=file_paths)


def remove_extension(value):
    base_name, _ = splitext(value)
    return base_name


app.jinja_env.filters['remove_extension'] = remove_extension

if __name__ == '__main__':
    #app.run(host='104.174.72.104', port=5000)
    app.run(host='0.0.0.0')


    #Debug Mode
    #app.run(debug=True)
