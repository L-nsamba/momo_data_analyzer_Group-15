from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import base64

raw_sms_data = [
    {
        "address": "M-Money",
        "date": "10 May 2024 4:30:58 PM",
        "body": "You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700."
    },
    {
        "address": "M-Money",
        "date": "10 May 2024 4:31:46 PM",
        "body": "TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "10 May 2024 9:32:40 PM",
        "body": "TxId: 51732411227. Your payment of 600 RWF to Samuel Carter 95464 has been completed at 2024-05-10 21:32:32. Your new balance: 400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "11 May 2024 6:45:36 PM",
        "body": "*113*R*A bank deposit of 40000 RWF has been added to your mobile money account at 2024-05-11 18:43:49. Your NEW BALANCE :40400 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    {
        "address": "M-Money",
        "date": "11 May 2024 6:48:49 PM",
        "body": "TxId: 17818959211. Your payment of 2,000 RWF to Samuel Carter 14965 has been completed at 2024-05-11 18:48:42. Your new balance: 38,400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "11 May 2024 8:34:55 PM",
        "body": "*165*S*10000 RWF transferred to Samuel Carter (250791666666) from 36521838 at 2024-05-11 20:34:47 . Fee was: 100 RWF. New balance: 28300 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 3:47:40 AM",
        "body": "*165*S*1000 RWF transferred to Samuel Carter (250790777777) from 36521838 at 2024-05-12 03:47:33 . Fee was: 20 RWF. New balance: 27280 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 11:41:35 AM",
        "body": "*162*TxId:13913173274*S*Your payment of 2000 RWF to Airtime with token  has been completed at 2024-05-12 11:41:28. Fee was 0 RWF. Your new balance: 25280 RWF . Message: - -. *EN#"
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 1:26:20 PM",
        "body": "TxId: 45434420466. Your payment of 10,900 RWF to Jane Smith 59543 has been completed at 2024-05-12 13:26:13. Your new balance: 14,380 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 1:34:32 PM",
        "body": "TxId: 82113964658. Your payment of 3,500 RWF to Alex Doe 43810 has been completed at 2024-05-12 13:34:25. Your new balance: 10,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 5:58:34 PM",
        "body": "TxId: 26614842768. Your payment of 1,000 RWF to Robert Brown 41193 has been completed at 2024-05-12 17:58:15. Your new balance: 9,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 6:09:05 PM",
        "body": "TxId: 70497610538. Your payment of 5,000 RWF to Linda Green 75028 has been completed at 2024-05-12 18:08:58. Your new balance: 4,880 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 7:23:57 PM",
        "body": "*165*S*1700 RWF transferred to Samuel Carter (250788999999) from 36521838 at 2024-05-12 19:23:50 . Fee was: 100 RWF. New balance: 3080 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "12 May 2024 8:49:37 PM",
        "body": "*165*S*2000 RWF transferred to Alex Doe (250791666666) from 36521838 at 2024-05-12 20:49:30 . Fee was: 100 RWF. New balance: 980 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 9:10:36 AM",
        "body": "*113*R*A bank deposit of 5000 RWF has been added to your mobile money account at 2024-05-14 09:10:29. Your NEW BALANCE :5980 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 9:12:08 AM",
        "body": "*165*S*1800 RWF transferred to Robert Brown (250788999999) from 36521838 at 2024-05-14 09:11:32 . Fee was: 100 RWF. New balance: 4080 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 9:27:46 AM",
        "body": "*165*S*2500 RWF transferred to Jane Smith (250791666666) from 36521838 at 2024-05-14 09:27:40 . Fee was: 100 RWF. New balance: 1480 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 2:02:06 PM",
        "body": "*165*S*500 RWF transferred to Samuel Carter (250790777777) from 36521838 at 2024-05-14 14:01:57 . Fee was: 20 RWF. New balance: 960 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 7:06:35 PM",
        "body": "*113*R*A bank deposit of 5000 RWF has been added to your mobile money account at 2024-05-14 19:06:03. Your NEW BALANCE :5960 RWF. Cash Deposit::CASH::::0::250795963036.Thank you for using MTN MobileMoney.*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 7:21:24 PM",
        "body": "*165*S*1800 RWF transferred to Alex Doe (250791666666) from 36521838 at 2024-05-14 19:21:16 . Fee was: 100 RWF. New balance: 4060 RWF. Kugura ama inite cg interineti kuri MoMo, Kanda *182*2*1# .*EN#"
    },
    {
        "address": "M-Money",
        "date": "14 May 2024 8:58:35 PM",
        "body": "You have received 25000 RWF from Samuel Carter (*********013) on your mobile money account at 2024-05-14 20:57:36. Message from sender: . Your new balance:29060 RWF. Financial Transaction Id: 43668074924."
    }
    
]

# Adding IDs to the transactions

transactions = []
for i, sms in enumerate(raw_sms_data, start=1):
    transactions.append({
        "id": i,
        "address": sms["address"],
        "date": sms["date"],
        "body": sms["body"]
    }
)
    
# Basic autentication credentials

USERNAME = "admin"
PASSWORD = "password"

def is_authenticated(headers):
    auth = headers.get("Authorization")
    if not auth:
        return False
    try:
        encoded = auth.split(" ")[1]
        decoded = base64.b64decode(encoded).decode()
        username, password = decoded.split(":", 1)
        return username == USERNAME and password == PASSWORD
    except:
        return False

class RequestHandler(BaseHTTPRequestHandler):

    def authenticate(self):
        if not is_authenticated(self.headers):
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="Secure API"')
            self.end_headers()
            return False
        return True

    def do_GET(self):
        if not self.authenticate():
            return

        if self.path == "/transactions":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(transactions, indent=2).encode())
            return

        if self.path.startswith("/transactions/"):
            try:
                tid = int(self.path.split("/")[-1])
            except ValueError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b"Invalid ID")
                return
            
            for transaction in transactions:
                if transaction["id"] == tid:
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps(transaction, indent=2).encode())
                    return


            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Transaction not found")
            return

        
        self.send_response(404)
        self.end_headers()
       

if __name__ == "__main__":
    server = HTTPServer(("localhost", 8080), RequestHandler)
    print("Server running at http://localhost:8080")
    server.serve_forever()            
            
            
