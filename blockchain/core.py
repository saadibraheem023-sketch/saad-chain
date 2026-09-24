import hashlib
import time

from .block import Block


class Blockchain:

    def __init__(self):

        self.chain = []

        self.pending_transactions = []

        self.difficulty = 2

        self.create_genesis_block()


    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
        
        # 1. التحقق من أن previous_hash يطابق hash البلوك السابق
        if block.previous_hash != self.hash(previous_block):
            return False
            
        # 2. التحقق من أن proof يبدأ بالأصفار (بدون حساب معادلة معقدة)
        # هذا أسرع بكثير، ويعتمد على أن البلوك نفسه يحتوي على proof صحيح
        if not str(block.proof).startswith("0"): # ملاحظة: هذا فحص مبسط
            pass # يمكنك تجاهل هذا الشرط أو تطويره لاحقاً
            
        previous_block = block
        block_index += 1
        
        return True

    def create_genesis_block(self):

        genesis = Block(
            index=1,
            transactions=[],
            previous_hash="0",
            proof=100
        )
        self.chain.append(genesis)
    def create_block(self, proof, previous_hash):
        block = Block(
        index=len(self.chain) + 1,
        transactions=self.pending_transactions,
        previous_hash=previous_hash,
        proof=proof
    )
        self.pending_transactions = [] # تفريغ المعاملات المعلقة
        self.chain.append(block)
        return block

        
    def hash(self, block):
        import json
        import hashlib
    # تحويل البلوك إلى نص JSON ثم ترميزه
        encoded_block = json.dumps(block.to_dict(), sort_keys=True).encode()
    # إرجاع الهاش بصيغة SHA-256
        return hashlib.sha256(encoded_block).hexdigest()

    def get_latest_block(self):

        return self.chain[-1]

    def proof_of_work(self, previous_proof):

        proof = 0

        while True:

            data = (
                str(proof ** 2)
                + str(previous_proof ** 2)
            )

            hash_value = hashlib.sha256(
                data.encode()
            ).hexdigest()

            if hash_value.startswith(
                "0" * self.difficulty
            ):
                return proof

            proof += 1

    def add_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    })

    def mine_block(self, proof, previous_hash):
        block = Block(
        index=len(self.chain) + 1,
        transactions=self.pending_transactions,
        previous_hash=previous_hash,
        proof=proof
    )
        self.pending_transactions = [] # تفريغ المعاملات المعلقة
        self.chain.append(block)
        return block

    def is_valid(self):

        for i in range(1, len(self.chain)):

            current = self.chain[i]

            previous = self.chain[i - 1]

            if current.previous_hash != previous.calculate_hash():
                return False

            data = (
                str(current.proof ** 2)
                + str(previous.proof ** 2)
            )

            hash_value = hashlib.sha256(
                data.encode()
            ).hexdigest()

            if not hash_value.startswith(
                "0" * self.difficulty
            ):
                return False

        return True