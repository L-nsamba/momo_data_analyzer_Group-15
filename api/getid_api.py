from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from auth.auth import is_authenticated # import existing auth

DATA_PATH = "dsa/logs/sms_records.json"

def load_transactions():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if not is_authenticated(self.headers):
            self.send_response(401)
            self.end_headers()
            return

        if not self.path.startswith("/transactions/"):
            self.send_response(404)
            self.end_headers()
            return

        try: 
            transaction_id = int(self.path.split("/")[-1])
        except ValueError:
            self.send_response(400)
            self.end_headers()
            return

        transactions = load_transactions()

        for tx in transactions:
            if tx.get("id") == transaction_id:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(tx).encode())
                return
        
        self.send_response(404)
        self.end_headers()
        

        
