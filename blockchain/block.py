
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.timestamp = timestamp or time.time()
        self.nonce = 0  # Used for mining
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.data}{self.timestamp}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        return 

    def __str__(self):
        transactions_str = ''.join(str(tx) for tx in self.data)
        return (f"\n Block #{self.index} [Previous Hash: {self.previous_hash}, "
                f"Hash: {self.hash}, Transactions:\n  {transactions_str}, "
                f"Timestamp: {self.timestamp}, Nonce: {self.nonce}]")