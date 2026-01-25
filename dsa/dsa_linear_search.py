transactions = [
    {
        "id": 1,
        "address": "M-Money",
        "date": "10 May 2024 4:30:58 PM",
        "body": "You have received 2000 RWF from Jane Smith (*********013) on your mobile money account at 2024-05-10 16:30:51. Message from sender: . Your new balance:2000 RWF. Financial Transaction Id: 76662021700."
    },
    {
        "id": 2,
        "address": "M-Money",
        "date": "10 May 2024 4:31:46 PM",
        "body": "TxId: 73214484437. Your payment of 1,000 RWF to Jane Smith 12845 has been completed at 2024-05-10 16:31:39. Your new balance: 1,000 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    },
    {
        "id": 3,
        "address": "M-Money",
        "date": "10 May 2024 9:32:40 PM",
        "body": "TxId: 51732411227. Your payment of 600 RWF to Samuel Carter 95464 has been completed at 2024-05-10 21:32:32. Your new balance: 400 RWF. Fee was 0 RWF.Kanda*182*16# wiyandikishe muri poromosiyo ya BivaMoMotima, ugire amahirwe yo gutsindira ibihembo bishimishije."
    }
]

# Linear search function
def linear_search(transactions, transaction_id):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            return transaction
    return None

# Example test 
result = linear_search(transactions, 2)

if result:
    print("Transaction Found:")
    print(result)
else:
    print("Transaction not found")
