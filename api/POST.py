import json
import os
from auth import require_auth

# Find the JSON file
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'transactions.json')
os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

def get_records():
    """Read all records from file"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_records(records):
    """Write all records to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(records, f, indent=4)

def handle_post(handler):
    """Handle POST requests for /transactions"""
    # Check authentication
    if not require_auth(handler):
        print(" Authentication failed")
        handler.send_response(401)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps({"error": "Authentication required"}).encode())
        return
    
    print(" Authentication successful")
    
    # Read the request body
    content_length = int(handler.headers.get('Content-Length', 0))
    body = handler.rfile.read(content_length)
    
    # Parse JSON
    try:
        new_record = json.loads(body.decode())
        print(f" Received transaction: {new_record}")
    except json.JSONDecodeError:
        print(" Invalid JSON")
        handler.send_response(400)
        handler.send_header('Content-type', 'application/json')
        handler.end_headers()
        handler.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
        return
    
    # Add to records
    records = get_records()
    records.append(new_record)
    save_records(records)
    print(f" Transaction saved! Total records: {len(records)}")
    
    # Send success response
    handler.send_response(201)
    handler.send_header('Content-type', 'application/json')
    handler.end_headers()
    response = {"message": "Transaction added!", "record": new_record}
    handler.wfile.write(json.dumps(response).encode())