
import unittest
import ecdsa
from blockchain.transaction import Transaction
from blockchain.util import generate_keys

class TestTransaction(unittest.TestCase):
    def test_transaction_signature(self):
        private_key, public_key = generate_keys()
        tx = Transaction(public_key, "Receiver", 10)
        tx.sign_transaction(private_key)
        self.assertTrue(tx.is_valid())

if __name__ == "__main__":
    unittest.main()
    