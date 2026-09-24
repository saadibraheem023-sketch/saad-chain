import ecdsa
import binascii

def generate_keys():
    private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    public_key = private_key.get_verifying_key()
    return {
        "private_key": binascii.hexlify(private_key.to_string()).decode(),
        "public_key": binascii.hexlify(public_key.to_string()).decode()
    }
def sign_transaction(private_key_hex, transaction):
    private_key = ecdsa.SigningKey.from_string(
        binascii.unhexlify(private_key_hex), curve=ecdsa.SECP256k1
    )
    signature = private_key.sign(str(transaction).encode())
    return binascii.hexlify(signature).decode()