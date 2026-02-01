import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from auth import require_auth

#Path to JSON data file
DATA_FILE = os.path.join("data", "processed", "transactions.json")

def load_transactions ():
    """Read all the transactions from the JSON file and return as list"""
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, 'r', encoding="utf-8") as file:
        return json.load(file)

def save_transactions(transactions):
    """Write all transactions to file"""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(transactions, file, indent=4)

class DeleteHandler(BaseHTTPRequestHandler):

    def do_DELETE(self):
        #Check Authentification
        if not require_auth(self.headers):
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode())
            return

        #Validate path format to be /transactions/{id}
        if not self.path.startswith("/transactions/"):
                    self.send_response(404)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Not Found"}).encode())
                    return

        #Parse the transaction id into an integer
        try:
            transaction_id = int(self.path.split("/")[-1])
        except ValueError:
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid transaction id"}).encode())
            return

        #Load exsting transactions
        transactions = load_transactions()

        #Find transaction with matching {id} and delete transaction
        new_transactions = []
        deleted = False

        for tx in transactions:
            if tx.get("id") == transaction_id:
                deleted = True
            else:
                new_transactions.append(tx)

        #Error Handling if there is no transaction with specified id
        if not deleted:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Transaction not found"}).encode())
            return

        #Save the updated Transactions
        save_transactions(new_transactions)

        #Return Success Message
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "message": "Transaction deleted successfully",
            "deleted_id": transactions
        }).encode())

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), DeleteHandler)
    print("DELETE server running at http://127.0.0.1:5000/transactions/{id}")
    server.serve_forever()






