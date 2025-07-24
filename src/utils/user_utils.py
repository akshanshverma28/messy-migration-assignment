# utils.py
def parse_json_request(required_fields):
    import json
    from flask import request

    data = json.loads(request.get_data())
    if not all(field in data for field in required_fields):
        return None, "Missing required fields"
    return data, None
