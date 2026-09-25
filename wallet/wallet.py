import ecdsa
import binascii
import hashlib
import json

class Wallet:
    def __init__(self):
        # توليد مفتاح خاص (Private Key) باستخدام منحنى SECP256k1 (نفس منحنى البيتكوين)
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        # اشتقاق المفتاح العام (Public Key)
        self.public_key = self.private_key.get_verifying_key()

    def get_private_key_hex(self):
        """إرجاع المفتاح الخاص بصيغة نصية (للتخزين)"""
        return binascii.hexlify(self.private_key.to_string()).decode()

    def get_public_key_hex(self):
        """إرجاع المفتاح العام بصيغة نصية"""
        return binascii.hexlify(self.public_key.to_string()).decode()

    def get_address(self):
        """عنوان المحفظة: آخر 40 حرفاً من هاش المفتاح العام"""
        pub_hex = self.get_public_key_hex()
        return hashlib.sha256(pub_hex.encode()).hexdigest()[:40]

    def sign_transaction(self, transaction_data):
        """توقيع المعاملة باستخدام المفتاح الخاص"""
        # تحويل البيانات إلى نص مرتب لضمان التوقيع الصحيح
        message = json.dumps(transaction_data, sort_keys=True).encode()
        signature = self.private_key.sign(message)
        return binascii.hexlify(signature).decode()

# اختبار سريع (يعمل فقط عند تشغيل الملف مباشرة)
if __name__ == "__main__":
    w = Wallet()
    print("=" * 40)
    print("🔐 محفظة جديدة تم إنشاؤها:")
    print("-" * 40)
    print("المفتاح الخاص:", w.get_private_key_hex())
    print("المفتاح العام:", w.get_public_key_hex())
    print("عنوان المحفظة:", w.get_address())
    print("=" * 40)