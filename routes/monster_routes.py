from flask import Blueprint, render_template, current_app
import requests
from services.monster_service import (
    get_monster_by_id,
    get_monster_drops,
    get_monsters_by_class,
    get_monster_resource,
    get_monster_mtick,
    get_monsterabnormalResist_data
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
    """Monster detail page"""
    monster = get_monster_by_id(monster_id)
    if not monster:
        return "Monster not found", 404

    # Fetch data from Google Sheets
    monster_class_df = get_google_sheets_data(MONSTER_CLASS_URL)
    monster_race_df = get_google_sheets_data(MONSTER_RACE_URL)
    monster_location_df = get_google_sheets_data(MONSTER_LOCATION_URL)

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
    respawn_time = get_monster_mtick(monster_id)
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
            if pd.isna(location_level):
                location_level = None
            monster_location = {
                "Location": location_match.iloc[0]['Location'],
                "LocationLevel": location_level
            }

    # Handle images
    file_path = f"{current_app.config['GITHUB_URL']}{monster_id}.png"
    file_path_gif = f"{current_app.config['GITHUB_URL']}gif/{monster_id}_IDLE.gif"
    try:
        response = requests.head(file_path_gif)
        if response.status_code != 200:
            file_path_gif = None
    except:
        file_path_gif = None

    # Get merchant items
    merchant_items = get_merchant_items(monster_id)

    # Get monster model number
    model_result = get_monster_resource(monster_id)
    monster_model_no = None
    prefix = 'm'  # Default prefix for all monsters

    if model_result:
        monster_model_no = f"{int(model_result.RFileName):05}"

    # DT_MonsterAbnormalResist Check
    monster_abnormalResist_data = get_monsterabnormalResist_data(monster_id)
    if monster_abnormalResist_data:
        monster_abnormalResist_data = monster_abnormalResist_data
    else:
        monster_abnormalResist_data = None
    
    
    
    
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
        monster_abnormalResist_data=monster_abnormalResist_data,
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