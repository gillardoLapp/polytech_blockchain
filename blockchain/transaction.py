
import ecdsa

class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender  # Public key of the sender
        self.receiver = receiver  # Public key of the receiver
        self.amount = amount
        self.signature = None

    def sign_transaction(self, private_key):
        if not private_key:
            raise Exception("Private key is required to sign the transaction")
        tx_data = f"{self.sender}{self.receiver}{self.amount}"
        self.signature = private_key.sign(tx_data.encode())

    def is_valid(self):
        if not self.signature:
            return False
        tx_data = f"{self.sender}{self.receiver}{self.amount}"
        return self.sender.verify(self.signature, tx_data.encode())
    
    def __str__(self):
        return f"Transaction from {self.sender} to {self.receiver} for {self.amount} units. Signature: {self.signature}"