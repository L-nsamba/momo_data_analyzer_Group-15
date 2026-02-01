<h1 align="center"> 📝 API DOCUMENTATION </h1>

### 1. GET /transactions
<li>Description - Retrieves and lists all SMS transaction records from transactions.json </li>
<li>CURL Request - curl -X GET http://127.0.0.1:5000/transactions </li>
<br>
<img src="../screenshots/get_all_http.png" width=700/>
<br>
<li>Status Codes</li>
i. 404 - No records exist or endpoint incorrect
ii. 401 - Missing or invalid credentials
iii. 200 - OK
