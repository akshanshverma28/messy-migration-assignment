app.py
from flask import Flask
from routes.user_routes import register_routes
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('users.db', check_same_thread=False)
conn.row_factory = sqlite3.Row  # Enable dict-style row access
cursor = conn.cursor()

# Register routes
register_routes(app, cursor, conn)

# Global error handler
@app.errorhandler(Exception)
def handle_exception(e):
    return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)

