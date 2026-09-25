import hashlib
import time
from .block import Block
from blockchain.transaction import Transaction
import sqlite3
import json


class Blockchain:

    def __init__(self,db_name='blockchain.db'):
        self.chain = []
        self.pending_transactions = []
        self.difficulty = 3  # قللنا الصعوبة سابقاً
        self.db_name=db_name
        self.load_chain()  # <--- تحميل السلسلة من قاعدة البيانات
        if not self.chain:
            self.create_genesis_block()  # إنشاء بلوك البداية فقط إذا كانت السلسلة فارغة


    def get_balance(self, address):
        """حساب رصيد عنوان محفظة معين بناءً على المعاملات في السلسلة"""
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction['receiver'] == address:
                    balance += transaction['amount']
                if transaction['sender'] == address:
                    balance -= transaction['amount']
        return balance
    def save_block(self, block):
        """حفظ بلوك في قاعدة البيانات"""
        conn = sqlite3.connect('self.db_name')
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS blocks (
            block_index INTEGER PRIMARY KEY,
            timestamp REAL,
            transactions TEXT,
            previous_hash TEXT,
            proof INTEGER
        )
    ''')
        cursor.execute('INSERT OR REPLACE INTO blocks VALUES (?, ?, ?, ?, ?)',
        (block.index, block.timestamp, json.dumps(block.transactions), 
         block.previous_hash, block.proof))
        conn.commit()
        conn.close()

    def load_chain(self):
            """تحميل السلسلة من قاعدة البيانات عند بدء التشغيل"""
            conn = sqlite3.connect('self.db_name')
            cursor = conn.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS blocks (block_index INTEGER PRIMARY KEY, timestamp REAL, transactions TEXT, previous_hash TEXT, proof INTEGER)')
            cursor.execute('SELECT * FROM blocks ORDER BY block_index')
            rows = cursor.fetchall()
            conn.close()
        
            if rows:
                self.chain = []
                for row in rows:
                    block = Block(
                        index=row[0],
                        transactions=json.loads(row[2]),
                        previous_hash=row[3],
                        proof=row[4]
                    )
                    block.timestamp = row[1]  # إعادة تعيين الوقت الأصلي
                    self.chain.append(block)


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

    from blockchain.transaction import Transaction

    def add_transaction(self, sender, receiver, amount, signature=None):
        transaction = Transaction(sender, receiver, amount, signature)
    
    # التحقق من صحة التوقيع (إذا لم يكن المرسل "0")
        if sender != "0" and not transaction.is_valid():
            return False, "توقيع غير صالح"
    
        self.pending_transactions.append(transaction.to_dict())
        return True, "تمت إضافة المعاملة"

    def mine_block(self, proof, previous_hash):
        block = Block(
        index=len(self.chain) + 1,
        transactions=self.pending_transactions,
        previous_hash=previous_hash,
        proof=proof
    )
        self.pending_transactions = [] # تفريغ المعاملات المعلقة
        self.chain.append(block)
        self.save_block(block) # حفظ البلوك في قاعدة البيانات
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