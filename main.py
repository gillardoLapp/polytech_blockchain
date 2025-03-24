
from blockchain.blockchain import Blockchain, Transaction
from scripts.create_transaction import create_transaction
from blockchain.util import generate_keys  




def main():
    private_key_miner, public_key_miner = generate_keys()
    reward = 10
    blockchain = Blockchain()
    blockchain.add_transaction(create_transaction())
    blockchain.add_transaction(create_transaction())
    blockchain.mine_pending_transactions("public_key_miner")
    #print(f"Blockchain valid: {blockchain.is_chain_valid()}")
    #blockchain.print_pending_transactions()
    blockchain.print_blocks()

if __name__ == "__main__":
    main()
    