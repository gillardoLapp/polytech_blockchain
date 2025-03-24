
from blockchain.util import generate_keys
from blockchain.transaction import Transaction

def create_transaction():
    private_key_sender, public_key_sender = generate_keys()
    private_key_reveiver, public_key_receiver = generate_keys()
    transaction = Transaction(public_key_sender, public_key_receiver, 10)
    transaction.sign_transaction(private_key_sender)
    return transaction

if __name__ == "__main__":
    transaction = create_transaction()
    print(f"Transaction: {transaction.amount} BTC from {transaction.sender} to {transaction.receiver}")
    