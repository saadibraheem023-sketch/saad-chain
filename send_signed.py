import requests
import json
from wallet.wallet import Wallet

# 1. أنشئ محفظة جديدة (أو استخدم محفظتك الحالية)
wallet = Wallet()
print(f"عنوان المحفظة: {wallet.get_address()}")
print(f"المفتاح الخاص: {wallet.get_private_key_hex()}")
print(f"المفتاح العام: {wallet.get_public_key_hex()}")

# 2. بيانات المعاملة
transaction_data = {
    "sender": wallet.get_address(),
    "receiver": "عنوان_المستقبل_هنا",  # استبدل هذا بعنوان محفظة أخرى
    "amount": 10
}

# 3. توقيع المعاملة
signature = wallet.sign_transaction(transaction_data)

# 4. إرسال المعاملة إلى السيرفر
payload = {
    "sender": transaction_data["sender"],
    "receiver": transaction_data["receiver"],
    "amount": transaction_data["amount"],
    "signature": signature,
    "public_key": wallet.get_public_key_hex()
}

response = requests.post('http://127.0.0.1:5005/transaction', json=payload)
print(f"رد السيرفر: {response.json()}")