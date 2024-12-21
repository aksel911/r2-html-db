from typing import List, Dict, Optional, Tuple
from os.path import splitext
from functools import lru_cache
from flask import current_app
from models.item import DT_Item, DT_ItemResource
from services.database import execute_query, get_db_connection

@lru_cache(maxsize=1000)
def get_item_by_id(item_id: int) -> Optional[DT_Item]:
    """Get item by ID with caching"""
    query = "SELECT * FROM DT_ITem WHERE IID = ?"
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_Item(
            row.IID,
            row.IName,
            row.IDesc.replace('\\n', ' ⭑ ') if row.IDesc else '',
            row.IWeight,
            row.IUseClass,
            row.IType,
            row.IMaxBeadHoleCount,
            row.ITermOfValidity
        )
    return None

@lru_cache(maxsize=1000)
def get_item_resource(item_id: int) -> Optional[DT_ItemResource]:
    """Get item resource by ID with caching"""
    query = "SELECT * FROM DT_ItemResource WHERE ROwnerID = ? AND RType = 2"
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemResource(
            row.ROwnerID,
            row.RFileName,
            row.RPosX,
            row.RPosY
        )
    return None

@lru_cache(maxsize=1000)
def get_item_model_resource(item_id: int) -> Optional[DT_ItemResource]:
    """Get item resource by ID with caching"""
    query = "SELECT * FROM DT_ItemResource WHERE ROwnerID = ? AND RType = 0"
    row = execute_query(query, (item_id,), fetch_one=True)
    
    if row:
        return DT_ItemResource(
            row.ROwnerID,
            row.RFileName,
            row.RPosX,
            row.RPosY
        )
    return None


def get_items_by_type(item_types: List[int], search_term: str = '') -> Tuple[List[DT_Item], Dict[int, str]]:
    """Generic function to fetch items by type with optional search"""
    type_str = ','.join(str(t) for t in item_types)
    
    # Get item IDs
    query = f"""
    SELECT IID 
    FROM DT_ITem 
    WHERE IType IN ({type_str}) 
    AND IName LIKE ? 
    ORDER BY IID
    """
    rows = execute_query(query, (f'%{search_term}%',))
    item_ids = [row.IID for row in rows]

    if not item_ids:
        return [], {}

    # Get items and their resources
    items = []
    file_paths = {}
    
    for item_id in item_ids:
        item = get_item_by_id(item_id)
        if item:
            items.append(item)
            
            resource = get_item_resource(item_id)
            if resource:
                file_paths[item_id] = resource.file_path
            else:
                file_paths[item_id] = f"{current_app.config['GITHUB_URL']}no_item_image.png"

    return items, file_paths