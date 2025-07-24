

from flask import jsonify

def render_home():
    print(" render_home() was called")
    return "User Management System"

def render_users(users):
    # users is expected to be a list of sqlite3.Row
    return jsonify([dict(user) for user in users])  

def render_user(user):
    if user:
        return jsonify(dict(user))  
    else:
        return "User not found", 404

def render_invalid_data():
    return "Invalid data", 400

def render_user_created():
    return "User created", 201

def render_user_updated():
    return "User updated"

def render_user_deleted(user_id):
    return f"User {user_id} deleted"

def render_missing_name():
    return "Please provide a name to search", 400

def render_login_response(user):
    if user:
        # user is a Row — convert to dict for clarity or index safely
        return jsonify({"status": "success", "user_id": user["id"]})
    else:
        return jsonify({"status": "failed"}), 401

def render_exception(e):
    print(f" Exception occurred: {e}")
    return jsonify({"error": str(e)}), 500

def render_server_error():
    return "Internal server error", 500
