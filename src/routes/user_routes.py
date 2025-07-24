# routes/routes.py

from controllers.user_controllers import *


def register_routes(app, cursor, conn):
    @app.route('/', methods=['GET'])
    def home_view():
        return home()

    @app.route('/users', methods=['GET'])
    def list_users():
        return get_all_users(cursor)

    @app.route('/user/<user_id>', methods=['GET'])
    def get_user_view(user_id):
        return get_user(cursor, user_id)

    @app.route('/users', methods=['POST'])
    def create_user_view():
        return create_user(cursor, conn)

    @app.route('/user/<user_id>', methods=['PUT'])
    def update_user_view(user_id):
        return update_user(cursor, conn, user_id)

    @app.route('/user/<user_id>', methods=['DELETE'])
    def delete_user_view(user_id):
        return delete_user(cursor, conn, user_id)

    @app.route('/search', methods=['GET'])
    def search_view():
        return search_users(cursor)

    @app.route('/login', methods=['POST'])
    def login_view():
        return login(cursor)
