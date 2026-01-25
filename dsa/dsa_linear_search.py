import json
import time

DATA_PATH = "dsa/logs/sms_records.json"


def load_transactions():
    """Load transactions from existing JSON file"""
    with open(DATA_PATH, "r") as file:
        return json.load(file)


def linear_search(transactions, transaction_id):
    """
    Linear Search Algorithm
    Time Complexity: O(n)
    """
    for transaction in transactions:
        if transaction.get("id") == transaction_id:
            return transaction
    return None


if __name__ == "__main__":
    transactions = load_transactions()

    start_time = time.time()
    result = linear_search(transactions, 20)
    end_time = time.time()

    if result:
        print("Transaction found:")
        print(result)
    else:
        print("Transaction not found")

    print("Execution time:", end_time - start_time, "seconds")

