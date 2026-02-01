import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from auth import require_auth
from urllib.parse import urlparse

# This is the Method PUT which updates an existing transaction/record

DATA_FILE = "data/processed/transactions.json"


class putTransaction(BaseHTTPRequestHandler):

    def do_PUT(self):
        if not require_auth(self):
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Unauthorized"}).encode("utf8"))
            return

        # Parsing the URL

        parsed_url = urlparse(self.path)
        path = parsed_url.path.strip("/").split("/")

        if len(path) != 2 or path[0] != "transactions":
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Not Found"}).encode())
            return

        transaction_id = path[1]

        # Reading the request body
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            updated_fields = json.loads(body)
        except json.JSONDecodeError:
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Invalid JSON"}).encode())
            return

        # Loading transactions from the file plus doing the dictionary lookup
        """
        The dictionary lookup works in that, it converts the list to a dictionary and uses id as the key
        """

        with open(DATA_FILE, "r") as data_file:
            transactions = json.load(data_file)

        transaction_dict = {}
        for transaction in transactions:
            transaction_dict[str(transaction["id"])] = transaction

        if transaction_id not in transaction_dict:
            self.send_response(401)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Transaction not Found"}).encode())
            return

        transaction_dict[transaction_id].update(updated_fields)

        # Saving the updated list back to the file

        with open(DATA_FILE, "w") as data_file:
            json.dump(list(transaction_dict.values()), data_file, indent=4)

        #Success responses
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({
            "message": "Transaction successfully updated",
            "transaction": transaction_dict[transaction_id]
        }).encode())

if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 5000), putTransaction)
    print("PUT server running at http://127.0.0.1:5000/transactions/{id}")
    server.serve_forever()
