
import unittest
from blockchain.block import Block

class TestBlock(unittest.TestCase):
    def test_block_creation(self):
        block = Block(1, "0", "Test Block")
        self.assertEqual(block.index, 1)
        self.assertEqual(block.previous_hash, "0")
        self.assertEqual(block.data, "Test Block")
        self.assertTrue(block.hash)
    
if __name__ == "__main__":
    unittest.main()
    