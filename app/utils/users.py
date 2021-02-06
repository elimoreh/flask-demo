import json
from flask import render_template, url_for
from app.store import find_users_sql, check_if_column_exists

def find_users(req): 
    args = req.args
    query_params = {
        "filters": {},
        "order_by": "id",
        "pagination" : 25,
        "page_number": 1,
    }
    for key in args:
        if key == 'order_by':
            query_params['order_by'] = args[key]
        elif key == 'pagination':
            query_params['pagination'] = int(args[key])
        elif key == 'page_number':
            query_params['page_number'] = int(args[key])
        elif check_if_column_exists('users', key):
            query_params['filters'][key] = args[key]
    users = find_users_sql(query_params)
    next_page = create_next_page(req.url_root, query_params)
    return render_template("users.html", users=users, next_page=next_page)

def create_next_page(base, params):
    params['page_number'] += 1
    for key in params['filters']:
        params[key] = params['filters'][key]
    del params['filters']
    return base[:-1] + url_for('routes.find_users_route', **params)
