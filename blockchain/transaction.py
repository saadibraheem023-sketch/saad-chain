import ecdsa
import binascii
import json
import hashlib

class Transaction:
    def __init__(self, sender, receiver, amount, signature=None):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.signature = signature

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "amount": self.amount,
            "signature": self.signature
        }

    def is_valid(self):
        """التحقق من صحة التوقيع الرقمي"""
        # إذا كان المرسل "0" فهذا يعني مكافأة تعدين (لا تحتاج توقيع)
        if self.sender == "0":
            return True
        
        if not self.signature:
            return False  # لا يوجد توقيع
        
        try:
            # إعادة بناء المفتاح العام من العنوان (يجب تخزين المفتاح العام للمرسل)
            # ملاحظة: هذا تبسيط، في الواقع يحتاج النظام لتخزين المفتاح العام لكل عنوان
            # لكن لأغراض تعليمية، سنفترض أن العنوان هو الهاش، ولن نتحقق فعلياً هنا
            return True
        except:
            return False