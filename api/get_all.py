import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from auth import require_auth

with open("data/processed/transactions.json") as f:
    sms_records = json.load(f)

class getall(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.rstrip("/") == "/transactions":
            if not require_auth(self):
                # Output incase of invalid authentication credentials
                self.send_response(401)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response = {"error": "Unauthorized"}
                self.wfile.write(json.dumps(response).encode())
                return
            
            #  for valid user credentials
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(sms_records, indent=4).encode())
        
        else:
            # Output for client side error
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"error": "Not Found"}
            self.wfile.write(json.dumps(response).encode())

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), getall)
    print("Server running at http://127.0.0.1:5000/transactions")
    server.serve_forever()