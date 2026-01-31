import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from auth import require_auth

#Path to JSON data file
DATA_FILE = os.path.join("data", "processed", "transactions.json")

def load_records ():
    """Read all the transactions from the JSON file and return as list"""
    if not os.path.exists(DATA_FILE)
    RETURN []

   with open(DATA_FILE, 'r') as f:
           return json.load(f)

def save_records(records):
    """Write all records to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(records, f, indent=4)

class DeleteTransactionHandler(BaseHTTPRequestHandler):

    def do_DELETE(self):
        #Check Authentification
        if not require_auth(self):
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.send_header()
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        #Expected format of path "/transactions/{id}"
        parts = self.path.strip("/").split("/")

        #Error Handling if path format is incorrect
        if len(parts) != 2 or parts[0] != "transactions":
                    self.send_response(404)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Not Found"}).encode())
                    return

        txn_id = parts[1]

        #Load exsting records
        records = load_records()

        #Find record with matching {id} and delete record

        #Error Handling if there is no record with specified id

        #Save the updated Records

        #Return Success Message







