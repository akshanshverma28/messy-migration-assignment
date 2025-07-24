# tests/test_utils.py
from utils.user_utils import parse_json_request
from flask import Flask
import pytest

app = Flask(__name__)


def test_parse_json_request_valid():
    with app.test_request_context(data='{"name": "A", "email": "a@x.com", "password": "x"}'):
        data, error = parse_json_request(['name', 'email', 'password'])
        assert error is None
        assert data['name'] == "A"


def test_parse_json_request_missing_field():
    with app.test_request_context(data='{"name": "Only Name"}'):
        data, error = parse_json_request(['name', 'email'])
        assert data is None
        assert error is not None
