# views.py
from flask import jsonify

def render_home():
    print("✅ render_home() was called")
    return "User Management System"

def render_users(users):
    return jsonify(users)

def render_user(user):
    if user:
        return jsonify(user)
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
        return jsonify({"status": "success", "user_id": user[0]})
    else:
        return jsonify({"status": "failed"}), 401

def render_exception(e):
    return jsonify({"error": str(e)}), 500

def render_server_error():
    return "Internal server error", 500
