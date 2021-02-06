import json
import sqlite3 as sql

def add_params_to_query(query, params):
    if 'filters' in params and params['filters'] != {}:
        where_string = 'WHERE '
        filters = params['filters']
        first = True
        for key in filters:
            sql_filter = f"{key} = \"{filters[key]}\""
            if first:
                first = False
            else:
                sql_filter = 'AND ' + sql_filter
            where_string += sql_filter
        query += where_string
    if 'order_by' in params:
        query += f"ORDER BY {params['order_by']} "
    if 'pagination' in params:
        query += f"LIMIT {params['pagination']} "
    if 'page_number' in params:
        offset = params['pagination'] * (params['page_number'] - 1)
        query += f"OFFSET {offset} "
    return query

def check_if_column_exists(table, column):
    conn = sql.connect('github.db')
    cur = conn.cursor()
    query = 'PRAGMA table_info({})'.format(table)
    columns = [i[1] for i in cur.execute(query)]
    return column in columns

def results_to_json(rows):
    return json.dumps([dict(x) for x in rows])