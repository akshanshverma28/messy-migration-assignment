from functools import wraps
from views.user_views import render_exception

def handle_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return render_exception(e)
    return wrapper
