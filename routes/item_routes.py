from flask import Blueprint, render_template, jsonify, request, render_template
from services.item_service import (
    apply_filters,
    item_to_dict,
    get_item_by_id, 
    get_item_resource,
    get_items_by_type,
    get_item_model_resource,
    get_specific_proc_item,
    get_itemabnormalResist_data,
    get_rune_bead_data,
    get_item_bead_module_data,
    get_item_bead_holeprob_data,
    get_item_attribute_add_data,
    get_item_attribute_resist_data,
    get_item_protect_data,
    get_item_slain_data,
    get_item_panalty_data
)
from services.monster_service import get_monster_drop_info
from services.merchant_service import get_merchant_sellers
from services.craft_service import (
    check_base_items_for_craft,
    check_next_craft_item
)
from services.skill_service import get_item_skill, get_sid_by_spid
from services.abnormal_service import get_abnormal_in_skill
from functools import wraps

bp = Blueprint('items', __name__)



# TODO: Это тест фильтр, нужно доделать. Очень долго грузит отфильтрованные данные, Под каждую страницу свои фильтры. Сделать фильтры для: Монстров, Абнормал и Скиллов (всего остального)
# ! Работает только /weapon --> @with_filters([1, 18, 20]) | Далее смотреть item_service.py --> apply_filters / item_to_dict | Далее все скрипты, css и остальное от фильтров в item_page_table_filter.html
def with_filters(allowed_types):
    """Enhanced decorator for filtering with pagination and type restrictions"""
    def decorator(original_route):
        @wraps(original_route)
        def wrapped_route(*args, **kwargs):
            try:
                # Get search term
                search_term = request.args.get('search', '')
                
                # Get initial data for allowed types
                items = []
                file_paths = {}
                
                for item_type in allowed_types:
                    type_items, type_paths = get_items_by_type([item_type], search_term)
                    items.extend(type_items)
                    file_paths.update(type_paths)

                # If it's an AJAX request, handle filtering
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    filters = request.args.to_dict()
                    
                    # Apply filters
                    filtered_items = apply_filters(items, filters)
                    
                    # Get pagination parameters
                    page = request.args.get('page', 1, type=int)
                    per_page = request.args.get('per_page', 25000, type=int) # ! PP LIMIT
                    
                    # Apply pagination
                    start_idx = (page - 1) * per_page
                    end_idx = start_idx + per_page
                    paginated_items = filtered_items[start_idx:end_idx]
                    
                    # Convert to dict for response
                    items_dict = [item_to_dict(item) for item in paginated_items]
                    
                    return jsonify({
                        'items': items_dict,
                        'resources': file_paths,
                        'total': len(filtered_items),
                        'pages': (len(filtered_items) + per_page - 1) // per_page
                    })
                
                # For normal request, pass data to route
                return original_route(items_wep=items, item_resources=file_paths, *args, **kwargs)
                
            except Exception as e:
                print(f"Error in route: {str(e)}")
                import traceback
                traceback.print_exc()
                return jsonify({'error': str(e)}), 500
                
        return wrapped_route
    return decorator



@bp.route('/item/<int:item_id>')
def item_detail(item_id: int):
    """Страница деталей предмета"""
    # Проверка основных данных
    if not (item := get_item_by_id(item_id)):
        return "Item not found", 404

    if not (item_resource := get_item_resource(item_id)):
        return "Item resource not found", 404

    # Обработка класса использования
    use_class = int(item.IUseClass.split('/')[-1].replace('.png', ''))

    # Получение связанных данных
    mondropinfo = get_monster_drop_info(item_id)
    merchant_sellers = get_merchant_sellers(item_id)
    craft_items = check_base_items_for_craft(item_id)
    craft_next_item = check_next_craft_item(item_id)
    skill_data = get_item_skill(item_id)
    specificproc_check = get_specific_proc_item(item_id)
    
    # Обработка данных навыков
    abnormal_type_data = abnormal_type_pic = None
    itemdskill_data = itemskill_pic = None
    linked_skills = linked_skillsaid = 0
    transform_list = monster_pic_url = None

    if skill_data and isinstance(skill_data, tuple) and len(skill_data) == 6:
        itemdskill_data, itemskill_pic, linked_skills, linked_skillsaid, transform_list, monster_pic_url = skill_data
        abnormal_type_data, abnormal_type_pic = get_abnormal_in_skill(linked_skillsaid)

    # Обработка модели предмета
    prefix = item_model_no = None
    if itemresource_result := get_item_model_resource(item_id):
        base = f"{int(itemresource_result.RPosX):03}{int(itemresource_result.RPosY):03}"
        prefix = 'i'
        item_model_no = base

        if item.IType == 3:  # Доспехи
            prefix = 'p'
            replace_dict = {
                1: [0, 1], 
                2: [2, 3], 
                4: [4, 5], 
                5: [0, 1, 4, 5],
                7: [4, 5, 0, 1, 2, 3], 
                8: [6, 7], 
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
                    item_model_no = f"0{index}0{base[3:]}"
        elif item.IType not in [1, 18, 20, 2, 19]:  # Не оружие/щит/стрелы
            prefix = 'i'  # TODO: ЗАГЛУШКА ДЛЯ ОСТАЛЬНОГО!

    # Проверка DT_ItemAbnormalResist
    item_abnormalResist_data = get_itemabnormalResist_data(item_id) or None
    
    # Проверка DT_Bead и активации навыков
    rune_bead_data = activation_bead_data = activation_bead_pic = None
    if item.IName.startswith('Руна'):
        if (rune_bead_data := get_rune_bead_data(item_id)) and rune_bead_data.mBeadType == 2:
            activation_bead_data, activation_bead_pic = get_sid_by_spid(rune_bead_data.mParamA)
    
    # Получение дополнительных данных предмета
    item_bead_module_data = get_item_bead_module_data(item_id) or None
    item_bead_holeprob_data = get_item_bead_holeprob_data(item_id) or None
    
    item_attribute_add_data = get_item_attribute_add_data(item_id) or None
    item_attribute_resist_data = get_item_attribute_resist_data(item_id) or None
    
    item_protect_data = get_item_protect_data(item_id) or None

    item_slain_data = get_item_slain_data(item_id) or None
    
    item_panalty_data = get_item_panalty_data(item_id) or None
    

    
    # Рендеринг шаблона с данными
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
        monster_pic_url=monster_pic_url,
        item_abnormalResist_data=item_abnormalResist_data,
        rune_bead_data=rune_bead_data,
        activation_bead_data=activation_bead_data,
        activation_bead_pic=activation_bead_pic,
        item_bead_module_data=item_bead_module_data,
        item_bead_holeprob_data=item_bead_holeprob_data,
        item_attribute_add_data=item_attribute_add_data,
        item_attribute_resist_data=item_attribute_resist_data,
        item_protect_data=item_protect_data,
        item_slain_data=item_slain_data,
        item_panalty_data=item_panalty_data
    )



# Item type routes

@bp.route('/all_items')
@with_filters(list(range(43)))
def all_items(items_wep=None, item_resources=None):
    """Weapon items route"""
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type(list(range(43)), search_term)
        
    return render_template('item/all_items.html', items_wep=items_wep, item_resources=item_resources)


@bp.route('/weapon')
@with_filters([1, 18, 20])
def weapon(items_wep=None, item_resources=None):
    """Weapon items route"""
    if items_wep is None:
        # Get initial data
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([1, 18, 20], search_term)
        
    return render_template('item/weapon.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/armor')
@with_filters([3])
def armor(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([3], search_term)
        
    return render_template('item/armor.html', items_wep=items_wep, item_resources=item_resources)
    


@bp.route('/gloves')
@with_filters([7])
def gloves(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([7], search_term)
    return render_template('item/gloves.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/boots')
@with_filters([6])
def boots(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([6], search_term)
    return render_template('item/boots.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/helmet')
@with_filters([8])
def helmet(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([8], search_term)
    return render_template('item/helmet.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/shield')
@with_filters([2])
def shield(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([2], search_term)
    return render_template('item/shield.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/arrows')
@with_filters([19])
def arrows(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([19], search_term)
    return render_template('item/arrows.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/cloak')
@with_filters([17])
def cloak(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([17], search_term)
    return render_template('item/cloak.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/materials')
@with_filters([10, 16])
def materials(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([10, 16], search_term)
    return render_template('item/materials.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/ring')
@with_filters([4])
def ring(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([4], search_term)
    return render_template('item/ring.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/belt')
@with_filters([9])
def belt(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([9], search_term)
    return render_template('item/belt.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/necklace')
@with_filters([5])
def necklace(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([5], search_term)
    return render_template('item/necklace.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/earrings')
@with_filters([42])
def earrings(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([42], search_term)
    return render_template('item/earrings.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/books')
@with_filters([12])
def books(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([12], search_term)
    return render_template('item/books.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/potions')
@with_filters([10])
def potions(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([10], search_term)
    return render_template('item/potions.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/etc')
@with_filters([14, 16, 13, 11])
def etc(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([14, 16, 13, 11], search_term)
    return render_template('item/etc.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/quest')
@with_filters([1])
def quest(items_wep=None, item_resources=None):
    if items_wep is None:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT mID FROM TblQuestCondition WHERE mType = 1")
            item_ids = [row.mID for row in cursor.fetchall()]

            if not item_ids:
                return render_template('item/quest.html', items_wep=[], item_resources={})

            items_wep, item_resources = get_items_by_type(item_ids)
    return render_template('item/quest.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/event')
@with_filters([15])
def event(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([15], search_term)
    return render_template('item/event.html', items_wep=items_wep, item_resources=item_resources)

@bp.route('/sphere')
@with_filters([22, 23, 24, 25, 26, 27, 28, 29])
def sphere(items_wep=None, item_resources=None):
    if items_wep is None:
        search_term = request.args.get('search', '')
        items_wep, item_resources = get_items_by_type([22, 23, 24, 25, 26, 27, 28, 29], search_term)
    return render_template('item/sphere.html', items_wep=items_wep, item_resources=item_resources)
