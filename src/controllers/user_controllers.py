# controllers.py
from flask import request
from models.user_models import *
from views.user_views import *
from utils.user_utils import parse_json_request
from utils.decorators import handle_exceptions


def home():
    
    return render_home()

@handle_exceptions
def get_all_users(cursor):
    users = fetch_all_users(cursor)
    return render_users(users)

@handle_exceptions
def get_user(cursor, user_id):
    user = fetch_user_by_id(cursor, user_id)
    return render_user(user)

@handle_exceptions
def create_user(cursor, conn):
    data, error = parse_json_request(['name', 'email', 'password'])
    if error:
        return render_invalid_data()
    if not insert_user(cursor, conn, data['name'], data['email'], data['password']):
        return render_server_error()
    return render_user_created()

@handle_exceptions
def update_user(cursor, conn, user_id):
    data, error = parse_json_request(['name', 'email'])
    if error:
        return render_invalid_data()
    if not update_user_by_id(cursor, conn, user_id, data['name'], data['email']):
        return render_server_error()
    return render_user_updated()

@handle_exceptions
def delete_user(cursor, conn, user_id):
    if not delete_user_by_id(cursor, conn, user_id):
        return render_server_error()
    return render_user_deleted(user_id)

@handle_exceptions
def search_users(cursor):
    name = request.args.get('name')
    if not name:
        return render_missing_name()
    users = search_users_by_name(cursor, name)
    return render_users(users)

@handle_exceptions
def login(cursor):
    data, error = parse_json_request(['email', 'password'])
    if error:
        return render_invalid_data()
    user = verify_user_login(cursor, data['email'], data['password'])
    return render_login_response(user)
