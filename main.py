
from blockchain.blockchain import Blockchain, Transaction
from scripts.create_transaction import create_transaction
from blockchain.util import generate_keys  




def main():
    
    blockchain = Blockchain()
    blockchain.add_block("Transaction 1")
    blockchain.add_block("Transaction 2")
    blockchain.print_blocks()
    #blockchain.add_transaction(create_transaction())
    #blockchain.add_transaction(create_transaction())
    #blockchain.mine_pending_transactions("miner")
    #blockchain.print_blocks()

if __name__ == "__main__":
    main()
    