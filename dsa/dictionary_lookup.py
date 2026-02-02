import json
import time

DATA_PATH = "data/processed/transactions.json"


def load_transactions():
    """
    Load transactions from the JSON file.
    """
    with open(DATA_PATH) as json_file:
        return json.load(json_file)


def build_transaction_dict(transactions):
    """
    Build a dictionary which will map transactions by key of transaction id
    Time complexity : O(n) Linear time
    """

    transaction_dict = {}

    for transaction in transactions:
        transaction_id = transaction.get("id")
        if transaction_id is not None:
            transaction_dict[str(transaction_id)] = transaction
    return transaction_dict


# Now the lookup, it uses hashing to access records by key
def dictionary_lookup(transaction_dict, transaction_id):
    """
    Dictionary Lookup
    Time complexity : O(1) it is constant)
    """
    return transaction_dict.get(str(transaction_id))

if __name__ == "__main__":
    transactions = load_transactions()

    transaction_dict = build_transaction_dict(transactions)

    print("Dictionary Lookup for 20 transactions")
    print("")

    for transaction_id in range(1, 21):
        start_time = time.time()
        result = dictionary_lookup(transaction_dict, transaction_id)
        end_time = time.time()

        execution_time = end_time - start_time

        if result:
            print(f"Transaction {transaction_id} found "
                  f"in Execution time of: {execution_time} seconds")

        else:
            print(f"Transaction {transaction_id} not found "
                  f"in Execution time of: {execution_time} seconds")
