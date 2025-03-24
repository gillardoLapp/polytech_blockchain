import unittest
from blockchain.block import Block

class TestBlock(unittest.TestCase):
    def setUp(self):
        self.block = Block(0, "0", ["Genesis Block"])

    def test_block_creation(self):
        self.assertEqual(self.block.index, 0)
        self.assertEqual(self.block.previous_hash, "0")
        self.assertEqual(self.block.data, ["Genesis Block"])

    def test_block_hash(self):
        self.assertIsNotNone(self.block.hash)

    def test_block_str(self):
        block_str = str(self.block)
        self.assertIn("Block", block_str)
        self.assertIn("Previous Hash: 0", block_str)
        self.assertIn("Genesis Block", block_str)

if __name__ == '__main__':
    unittest.main()