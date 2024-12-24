import pyodbc
from contextlib import contextmanager
from flask import current_app

@contextmanager
def get_db_connection():
    """Context manager for database connections"""
    conn_str = ';'.join(f'{k}={v}' for k, v in current_app.config['DATABASE_CONFIG'].items())
    conn = pyodbc.connect(conn_str)
    try:
        yield conn
    finally:
        conn.close()

def execute_query(query, params=None, fetch_one=False):
    """Execute a database query and return results"""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        if fetch_one:
            return cursor.fetchone()
        return cursor.fetchall()
    
