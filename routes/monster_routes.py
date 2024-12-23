from flask import Blueprint, render_template, current_app
import requests
from services.monster_service import (
    get_monster_by_id,
    get_monster_drops,
    get_monsters_by_class,
    get_monster_resource,
    get_monster_mtick,
    get_monsterabnormalResist_data,
    get_monster_attribute_add_data,
    get_monster_attribute_resist_data,
    get_monster_protect_data,
    get_monster_slain_data
)
from services.utils import get_google_sheets_data
from services.merchant_service import (
    get_merchant_items,
    get_payment_type_name
)
from services.database import execute_query
from config.settings import MONSTER_CLASS_URL, MONSTER_RACE_URL, MONSTER_LOCATION_URL
import pandas as pd

bp = Blueprint('monsters', __name__)



@bp.route('/monster/<int:monster_id>')
def monster_detail(monster_id: int):
    """Страница деталей монстра"""
    # Получение данных монстра
    if not (monster := get_monster_by_id(monster_id)):
        return "Monster not found", 404

    # Получение данных из Google Sheets
    sheets_data = {
        'class': get_google_sheets_data(MONSTER_CLASS_URL),
        'race': get_google_sheets_data(MONSTER_RACE_URL),
        'location': get_google_sheets_data(MONSTER_LOCATION_URL)
    }

    # Получение информации о классе
    class_info = {"MName": ""}
    if not sheets_data['class'].empty:
        class_match = sheets_data['class'][sheets_data['class']['MClass'] == monster['MClass']]
        if not class_match.empty:
            class_info["MName"] = class_match.iloc[0]['MName']

    # Получение информации о расе
    race_info = {"mDesc": None}
    if not sheets_data['race'].empty:
        race_match = sheets_data['race'][sheets_data['race']['MRaceType'] == monster['mRaceType']]
        if not race_match.empty:
            race_info["mDesc"] = race_match.iloc[0]['mDesc']

    # Получение времени респауна
    respawn_time = get_monster_mtick(monster_id)
    respawn_info = {
        "mTick": respawn_time / 1000,
        "mTickms": respawn_time
    }

    # Получение локации монстра
    monster_location = None
    if not sheets_data['location'].empty:
        location_match = sheets_data['location'][sheets_data['location']['MID'] == monster_id]
        if not location_match.empty:
            row = location_match.iloc[0]
            monster_location = {
                "Location": row['Location'],
                "LocationLevel": None if pd.isna(row['LocationLevel']) else row['LocationLevel']
            }

    # Обработка изображений
    file_path = f"{current_app.config['GITHUB_URL']}{monster_id}.png"
    file_path_gif = f"{current_app.config['GITHUB_URL']}gif/{monster_id}_IDLE.gif"
    try:
        if requests.head(file_path_gif).status_code != 200:
            file_path_gif = None
    except:
        file_path_gif = None

    # Получение модели монстра
    prefix = 'm'  # Префикс по умолчанию для всех монстров
    monster_model_no = None
    if model_result := get_monster_resource(monster_id):
        monster_model_no = f"{int(model_result.RFileName):05}"

    # Получение данных о сопротивлении Абнормал
    monster_abnormalResist_data = get_monsterabnormalResist_data(monster_id) or None
    
    monster_attribute_add_data = get_monster_attribute_add_data(monster_id) or None
    monster_attribute_resist_data = get_monster_attribute_resist_data(monster_id) or None
    
    monster_protect_data = get_monster_protect_data(monster_id) or None

    monster_slain_data = get_monster_slain_data(monster_id) or None
    
    return render_template(
        'monster_core/monster_page_detail.html',
        item=monster,
        file_path=file_path,
        file_path_gif=file_path_gif,
        classinfo=class_info,
        raceinfo=race_info,
        respawntimeinfo=respawn_info,
        monlocationinfo=monster_location,
        merchant_items=get_merchant_items(monster_id),
        mondropinfo=get_monster_drops(monster_id),
        monstermodelno_result=monster_model_no,
        monster_abnormalResist_data=monster_abnormalResist_data,
        monster_attribute_add_data=monster_attribute_add_data,
        monster_attribute_resist_data=monster_attribute_resist_data,
        monster_protect_data=monster_protect_data,
        monster_slain_data=monster_slain_data,
        prefix=prefix
    )

@bp.route('/monster_regular')
def monster_regular():
    monsters, file_paths = get_monsters_by_class(
        [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 31, 32, 2]
    )
    return render_template('monster/monster_regular.html', items=monsters, item_resources=file_paths)

@bp.route('/monster_imennoy')
def monster_imennoy():
    monsters, file_paths = get_monsters_by_class([28])
    return render_template('monster/monster_imennoy.html', items=monsters, item_resources=file_paths)

@bp.route('/monster_boss')
def monster_boss():
    monsters, file_paths = get_monsters_by_class([29, 33, 34, 35, 36, 37, 38])
    return render_template('monster/monster_boss.html', items=monsters, item_resources=file_paths)

@bp.route('/monster_raidboss')
def monster_raid_boss():
    monsters, file_paths = get_monsters_by_class([26])
    return render_template('monster/monster_raidboss.html', items=monsters, item_resources=file_paths)

@bp.route('/monster_event')
def monster_event():
    monsters, file_paths = get_monsters_by_class([27])
    return render_template('monster/monster_event.html', items=monsters, item_resources=file_paths)

@bp.route('/monster_npc')
def monster_npc():
    monsters, file_paths = get_monsters_by_class([23, 35])
    return render_template('monster/monster_npc.html', items=monsters, item_resources=file_paths)