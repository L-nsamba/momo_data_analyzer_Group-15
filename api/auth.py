import base64
import json

# Credentials for multiple users (group members)
USERS = {
    "michael": "mich129",
    "leon": "leon@password",
    "mitchell": "mitchell_password",
    "queen": "view1238",
    "mufaro": "mufaro@$13"
}

def require_auth(handler):
    auth_header = handler.headers.get("Authorization")
    if not auth_header:
        return False
    
    try:
        #Receiving headers from user credential input
        auth_type, encoded = auth_header.split(" ", 1)
        if auth_type.lower() != "basic":
            return False
        
        #Decoding base64 password and username
        decoded = base64.b64decode(encoded).decode("utf-8")
        username, password = decoded.split(":", 1)

        #Validating to see if the usernames correspond to passwords
        if username in USERS and USERS[username] == password:
            return True
        return False
    
    except Exception: 
        return False