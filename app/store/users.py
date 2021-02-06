import sqlite3 as sql
import json
from .sql_helpers import * 

def find_users_sql(params):
    
    conn = sql.connect('github.db')
    conn.row_factory = sql.Row
    
    cur = conn.cursor()
    base_query = "SELECT * FROM users "
    query = add_params_to_query(base_query, params)
    
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    
    return rows


