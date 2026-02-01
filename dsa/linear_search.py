import json
import time

DATA_PATH = "data/processed/transactions.json"


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

    print("Linear Search for 20 transactions\n")

    for transaction_id in range(1, 21):
        start_time = time.time()
        result = linear_search(transactions, transaction_id)
        end_time = time.time()

        execution_time = end_time - start_time

        if result:
            print(
                f"Transaction ID {transaction_id} found"
                f"| Execution Time: {execution_time:.6f} seconds"
            )
        else:
            print(
                f"Transaction ID {transaction_id} not found"
                f"| Execution Time: {execution_time:.6f} seconds"
            )    
