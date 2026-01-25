import json
from flask import Flask, jsonify, request

app = Flask(__name__)

with open("sms_records.json") as f:
    sms_records = json.load(f)

#To get items
@app.route('/sms_records', methods=['GET'])
def get_records():
    return jsonify(sms_records)

if __name__ == '__main__':
    app.run(debug=True)