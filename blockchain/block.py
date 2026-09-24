import hashlib
import json
import time


class Block:

    def __init__(
        self,
        index,
        transactions,
        previous_hash,
        proof
    ):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.proof = proof

    def to_dict(self):

        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": self.transactions,
            "previous_hash": self.previous_hash,
            "proof": self.proof
        }

    def calculate_hash(self):

        block_data = json.dumps(
            self.to_dict(),
            sort_keys=True
        ).encode()

        return hashlib.sha256(
            block_data
        ).hexdigest()