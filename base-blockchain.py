import hashlib
import json

class Transaction:
    def __init__(self, data):
        self.data = data
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_string = json.dumps(self.data, sort_keys=True).encode()
        return hashlib.sha256(data_string).hexdigest()

# Functions based on crypto blockchain


class Block:
    def __init__(self, transactions, previous_hash):
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

def calculate_hash(self):
        transaction_hashes = [tx.hash for tx in self.transactions]
        block_string = json.dumps(transaction_hashes, sort_keys=True).encode() + self.previous_hash.encode()
        return hashlib.sha256(block_string).hexdigest()
# Create transactions
transaction1 = Transaction("Alice sends $100 to Bob")
transaction2 = Transaction("Bob sends $50 to Charlie")
transaction3 = Transaction("Charlie sends $30 to Alice")

# Create a block containing the transactions
transactions = [transaction1, transaction2, transaction3]
previous_hash = "00000000000000000000000000000000"  # Genesis block
block = Block(transactions, previous_hash)

# Print the block's hash
print("Block Hash:", block.hash)
