# from flask import Flask, request, jsonify
# from auth import require_auth
# import json
# import os

# app = Flask(__name__)

# # Find the JSON file relative to this script
# DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'processed', 'transactions.json')

# # Make sure the folder exists
# os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

# def get_records():
#     """Read all records from file, or return empty list if file doesn't exist"""
#     if not os.path.exists(DATA_FILE):
#         return []
    
#     with open(DATA_FILE, 'r') as f:
#         return json.load(f)

# def save_records(records):
#     """Write all records to file"""
#     with open(DATA_FILE, 'w') as f:
#         json.dump(records, f, indent=4)

# @app.route('/transactions', methods=['POST'])
# @require_auth
# def add_transaction():
#     # Get the data from the request
#     new_record = request.get_json()
    
#     if not new_record:
#         return jsonify({"error": "No data provided"}), 400
    
#     # Add to existing records and save
#     records = get_records()
#     records.append(new_record)
#     save_records(records)
    
#     return jsonify({"message": "Transaction added!", "record": new_record}), 201

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)