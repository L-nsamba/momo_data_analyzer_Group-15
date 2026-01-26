from flask import request, jsonify
from functools import wraps

# Credentials for multiple users (group members)
USERS = {
    "michael": "mich129",
    "leon": "leon@password",
    "mitchell": "mitchell_password",
    "queen": "view1238",
    "mufaro": "mufaro@$13"
}


def require_auth(f):
    """Decorator to protect routes with basic authentication"""

    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth = request.authorization

        # Check if credentials were provided
        if not auth:
            return jsonify({"error": "Authentication required"}), 401

        # Check if username exists and password matches
        if auth.username not in USERS or USERS[auth.username] != auth.password:
            return jsonify({"error": "Invalid credentials"}), 401

        return f(*args, **kwargs)

    return decorated_function
