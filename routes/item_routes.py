from flask import Blueprint, render_template, request
from services.item_service import (
    get_item_by_id, 
    get_item_resource,
    get_items_by_type,
    get_item_model_resource,
    get_specific_proc_item
)
from services.monster_service import get_monster_drop_info
from services.merchant_service import get_merchant_sellers
from services.craft_service import (
    check_base_items_for_craft,
    check_next_craft_item
)
from services.skill_service import get_item_skill
from services.abnormal_service import get_abnormal_in_skill

bp = Blueprint('items', __name__)

@bp.route('/item/<int:item_id>')
def item_detail(item_id: int):
    """Item detail page"""
    item = get_item_by_id(item_id)
    if not item:
        return "Item not found", 404

    use_class = item.IUseClass.split('/')[-1].replace('.png', '')
    use_class = int(use_class)

    item_resource = get_item_resource(item_id)
    if not item_resource:
        return "Item resource not found", 404

    # Get related data
    mondropinfo = get_monster_drop_info(item_id)
    merchant_sellers = get_merchant_sellers(item_id)
    craft_items = check_base_items_for_craft(item_id)
    craft_next_item = check_next_craft_item(item_id)
    skill_data = get_item_skill(item_id)
    
    specificproc_check = get_specific_proc_item(item_id)
    
    itemresource_result = get_item_model_resource(item_id)
    
    # Process skill data
    abnormal_type_data = None
    abnormal_type_pic = None
    
    itemdskill_data = None
    itemskill_pic = None
    
    linked_skills = 0
    linked_skillsaid = 0
    
    transform_list = None
    monster_pic_url = None

    if skill_data:
        # Проверяем, что skill_data возвращает кортеж из 6 элементов
        if isinstance(skill_data, tuple) and len(skill_data) == 6:
            itemdskill_data, itemskill_pic, linked_skills, linked_skillsaid, transform_list, monster_pic_url = skill_data
            
            abnormal_type_data, abnormal_type_pic = get_abnormal_in_skill(linked_skillsaid)

    prefix = None
    item_model_no = None

    if itemresource_result:
        base = f"{int(itemresource_result.RPosX):03}{int(itemresource_result.RPosY):03}"
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
                    item_model_no = final
        
        elif item.IType in [1, 18, 20, 2, 19]:  # Weapons / Shield / Arrows
            prefix = 'i'  # Используем одну букву вместо кортежа
            item_model_no = base
        else:
            prefix = 'i'  # TODO: ЗАГЛУШКА ДЛЯ ОСТАЛЬНОГО!
            item_model_no = base

    print(transform_list, monster_pic_url)
    return render_template(
        'item_core/item_page_detail.html',
        item=item,
        file_path=item_resource.file_path,
        mondropinfo=mondropinfo,
        merchant_sellers=merchant_sellers,
        monstermodelno_result=item_model_no,
        prefix=prefix,
        use_class=use_class,
        craft_result=craft_items,
        craft_next=craft_next_item,
        itemdskill_data=itemdskill_data,
        itemskill_pic=itemskill_pic,
        linked_skills=linked_skills,
        linked_skillsaid=linked_skillsaid,
        abnormal_type_data=abnormal_type_data,
        abnormal_type_pic=abnormal_type_pic,
        specificproc_data=specificproc_check,
        transform_list=transform_list,
        monster_pic_url=monster_pic_url
    )

# Item type routes
@bp.route('/weapon')
def weapon():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([1, 18, 20], search_term)
    return render_template('item/weapon.html', items_wep=items, item_resources=file_paths)

@bp.route('/armor')
def armor():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([3], search_term)
    return render_template('item/armor.html', items_wep=items, item_resources=file_paths)

@bp.route('/gloves')
def gloves():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([7], search_term)
    return render_template('item/gloves.html', items_wep=items, item_resources=file_paths)

@bp.route('/boots')
def boots():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([6], search_term)
    return render_template('item/boots.html', items_wep=items, item_resources=file_paths)

@bp.route('/helmet')
def helmet():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([8], search_term)
    return render_template('item/helmet.html', items_wep=items, item_resources=file_paths)

@bp.route('/shield')
def shield():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([2], search_term)
    return render_template('item/shield.html', items_wep=items, item_resources=file_paths)

@bp.route('/arrows')
def arrows():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([19], search_term)
    return render_template('item/arrows.html', items_wep=items, item_resources=file_paths)

@bp.route('/cloak')
def cloak():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([17], search_term)
    return render_template('item/cloak.html', items_wep=items, item_resources=file_paths)

@bp.route('/materials')
def materials():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([10, 16], search_term)
    return render_template('item/materials.html', items_wep=items, item_resources=file_paths)

@bp.route('/ring')
def ring():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([4], search_term)
    return render_template('item/ring.html', items_wep=items, item_resources=file_paths)

@bp.route('/belt')
def belt():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([9], search_term)
    return render_template('item/belt.html', items_wep=items, item_resources=file_paths)

@bp.route('/necklace')
def necklace():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([5], search_term)
    return render_template('item/necklace.html', items_wep=items, item_resources=file_paths)

@bp.route('/earrings')
def earrings():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([42], search_term)
    return render_template('item/earrings.html', items_wep=items, item_resources=file_paths)

@bp.route('/books')
def books():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([12], search_term)
    return render_template('item/books.html', items_wep=items, item_resources=file_paths)

@bp.route('/potions')
def potions():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([10], search_term)
    return render_template('item/potions.html', items_wep=items, item_resources=file_paths)

@bp.route('/etc')
def etc():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([14, 16, 13, 11], search_term)
    return render_template('item/etc.html', items_wep=items, item_resources=file_paths)

@bp.route('/quest')
def quest():
    """Get quest items"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT mID FROM TblQuestCondition WHERE mType = 1")
        item_ids = [row.mID for row in cursor.fetchall()]

        if not item_ids:
            return render_template('quest.html', items_wep=[], item_resources={})

        items, file_paths = get_items_by_type(item_ids)
        return render_template('item/quest.html', items_wep=items, item_resources=file_paths)

@bp.route('/event')
def event():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([15], search_term)
    return render_template('item/event.html', items_wep=items, item_resources=file_paths)

@bp.route('/sphere')
def sphere():
    search_term = request.args.get('search', '')
    items, file_paths = get_items_by_type([22, 23, 24, 25, 26, 27, 28, 29], search_term)
    return render_template('item/sphere.html', items_wep=items, item_resources=file_paths)