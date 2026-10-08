import json

def load_transactions():
    with open('data/transactions.json', 'r') as file:
        transactions = json.load(file)
    return transactions

transactions = load_transactions()

for transaction in transactions:
    print(transaction["id"], transaction["amount"])