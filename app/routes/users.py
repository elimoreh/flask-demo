from flask import request
from . import routes
from app.cache import cache
from app.utils import find_users

@routes.route('/users', methods=['GET'])
@cache.cached(timeout=20, query_string=True)
def find_users_route():
    return find_users(request)


