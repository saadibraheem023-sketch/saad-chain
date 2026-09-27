import ecdsa
import binascii
import json
import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount, signature=None, public_key=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature
        self.public_key = public_key  # نضيف المفتاح العام للتحقق

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "signature": self.signature,
            "public_key": self.public_key
        }

    def is_valid(self):
        """التحقق من صحة التوقيع الرقمي"""
        # إذا كان المرسل "0" فهذا يعني مكافأة تعدين (لا تحتاج توقيع)
        if self.sender == "0":
            return True

        if not self.signature or not self.public_key:
            return False  # لا يوجد توقيع أو مفتاح عام

        try:
            # 1. إعادة بناء المفتاح العام من النص
            public_key_bytes = binascii.unhexlify(self.public_key)
            verifying_key = ecdsa.VerifyingKey.from_string(public_key_bytes, curve=ecdsa.SECP256k1)
            
            # 2. إعادة بناء البيانات التي تم توقيعها
            transaction_data = {
                "sender": self.sender,
                "receiver": self.receiver,
                "amount": self.amount
            }
            message = json.dumps(transaction_data, sort_keys=True).encode()
            
            # 3. التحقق من التوقيع
            signature_bytes = binascii.unhexlify(self.signature)
            return verifying_key.verify(signature_bytes, message)
        except Exception as e:
            print(f"خطأ في التحقق: {e}")
            return False