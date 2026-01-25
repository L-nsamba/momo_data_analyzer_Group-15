import json
from flask import Flask, jsonify
from auth import require_auth

app = Flask(__name__)


with open("dsa/logs/sms_records.json") as f:
    sms_records = json.load(f)

#Accessing the file path in which the json file is stored and executing GET
@app.route('/sms_records', methods=['GET'])
@require_auth
def get_records():
    return jsonify(sms_records)

print(f"Link to JSON: http://127.0.0.1:5000/sms_records ")

if __name__ == '__main__':
    app.run(debug=True)