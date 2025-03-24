
import unittest
from blockchain.blockchain import Blockchain
from blockchain.block import Block

class TestBlockchain(unittest.TestCase):
    def test_chain_validity(self):
        blockchain = Blockchain()
        blockchain.add_block("Transaction 1")
        blockchain.add_block("Transaction 2")
        self.assertTrue(blockchain.is_chain_valid())

if __name__ == "__main__":
    unittest.main()
    