from blockchain.core import Blockchain
from blockchain.transaction import Transaction


chain = Blockchain()

print("Genesis Block:")
print(chain.get_latest_block().to_dict())


transaction = Transaction(
    "Ahmed",
    "Saad",
    10
)

chain.add_transaction(transaction)

print("\nMining...")

block = chain.mine_block()

print("\nNew Block:")
print(block.to_dict())

print("\nBlockchain Valid:")
print(chain.is_valid())