
from .block import Block
from .transaction import Transaction  

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 10  # Reward per mined block

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def add_transaction(self, transaction):
        if transaction.is_valid():
            self.pending_transactions.append(transaction)
        else:
            raise Exception("Invalid transaction")

    def add_block(self, data):
        """
        Adds a new block to the chain.
        """
        previous_block = self.chain[-1]
        new_block = Block(len(self.chain), previous_block.hash, data)
        self.chain.append(new_block)

    def mine_pending_transactions(self, miner_public_key):
        self.pending_transactions += [Transaction(None, miner_public_key, self.mining_reward)]
        new_block = Block(len(self.chain), self.chain[-1].hash, self.pending_transactions)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            if self.chain[i].previous_hash != self.chain[i-1].hash:
                return False
        return True
    
    def print_pending_transactions(self):
        for block in self.chain:
            print(f"Block {block.index} transactions:")
            for transaction in block.data:
                print(f"  {transaction}")

    def print_blocks(self):
        for block in self.chain:
            print(block)