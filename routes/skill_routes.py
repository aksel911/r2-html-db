from flask import Blueprint, render_template, current_app
from services.skill_service import (
    get_skill_detail,
    get_skills_list,
    get_skill_use_by_spid_items,
    get_skill_use_by_sid,
    get_monster_reget_skill_pic_icon_datasource
)
from services.utils import get_google_sheets_data
from config.settings import SKILLAPPLYRACE_LOCATION_URL
from services.database import execute_query
from services.utils import get_skill_icon_path, clean_dict

bp = Blueprint('skills', __name__)

@bp.route('/skill/<int:skill_id>')
def skill_detail(skill_id: int):
    """Skill detail page"""
    skills = get_skill_detail(skill_id)
    if not skills:
        return "Skill not found", 404

    # Берем первый скилл для основной информации
    skill = skills[0]
    
    spid_id = skill.skill_pack_id

    # Get related skill data for items
    skill_for_item = get_skill_use_by_spid_items(spid_id)
    if skill_for_item:
        skill_for_item_data, skill_for_item_pic = skill_for_item
    else:
        skill_for_item_data, skill_for_item_pic = None, None

    # Get related skill data for skills
    skill_for_skill = get_skill_use_by_sid(spid_id)
    if skill_for_skill:
        skill_for_skill_data, skill_for_skill_pic = skill_for_skill
    else:
        skill_for_skill_data, skill_for_skill_pic = None, None

    # Get use class information
    use_class = None
    if skill.item_use_class:
        try:
            use_class = int(skill.item_use_class.split('/')[-1].replace('.png', ''))
        except (ValueError, AttributeError):
            pass

    # Get race information from Google Sheets
    skill_apply_race_df = get_google_sheets_data(SKILLAPPLYRACE_LOCATION_URL)
    race_info = None
    if not skill_apply_race_df.empty and skill.apply_race is not None:
        race_match = skill_apply_race_df[skill_apply_race_df['mApplyRace'] == skill.apply_race]
        if not race_match.empty:
            race_info = race_match.iloc[0]['mDesc']

    # Get skill icon
    skill_icon = None
    # query = """
    #     SELECT mSpriteFile, mSpriteX, mSpriteY 
    #     FROM DT_SkillPack a
    #     LEFT JOIN DT_SkillPackSkill b ON (a.mSPID = b.mSPID)
    #     WHERE b.mSID = ?
    # """
    # icon_data = execute_query(query, (skill_id,), fetch_one=True)
    
    icon_data = get_monster_reget_skill_pic_icon_datasource(skill_id)
    
    if icon_data:
        skill_icon = get_skill_icon_path(
            icon_data.mSpriteFile,
            icon_data.mSpriteX,
            icon_data.mSpriteY
        )
    
    return render_template(
        'skill_core/skill_page_detail.html',
        skill=skill,
        skills=skills,  # Передаем весь список скиллов
        use_class=use_class,
        race_info=race_info,
        skill_icon=skill_icon,
        skill_for_item_data=skill_for_item_data,
        skill_for_item_pic=skill_for_item_pic,
        skill_for_skill_data=skill_for_skill_data,
        skill_for_skill_pic=skill_for_skill_pic
    )

@bp.route('/skills')
def skills_list():
    """List all skills"""
    skills_data, file_paths = get_skills_list()
    return render_template(
        'skill/skills.html',
        skills=skills_data,
        item_resources=file_paths
    )