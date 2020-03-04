import GenAddress
import hashlib
import ecdsa


class VerifyTransaction(object):

    def generate_signature(self, sender_private_key, transaction):
        sha256 = hashlib.sha256()
        sha256.update(str(transaction).encode('utf-8'))
        message = sha256.digest()
        private_key = ecdsa.SigningKey.from_string(
            bytes().fromhex(sender_private_key), curve=ecdsa.SECP256k1)
        private_key_sign = private_key.sign(message)
        signature = private_key_sign.hex()
        return signature

    def verify_transaction_signature(self, sender_public_key, signature, transaction):
        sha256 = hashlib.sha256()
        sha256.update(str(transaction).encode('utf-8'))
        message = sha256.digest()
        signature_bytes = bytes().fromhex(signature)
        verifying_key = ecdsa.VerifyingKey.from_string(
            bytes().fromhex(sender_public_key), curve=ecdsa.SECP256k1)
        verified_key = verifying_key.verify(signature_bytes, message)
        return verified_key


if __name__ == '__main__':
    sender = GenAddress.GenAddress()
    receiver = GenAddress.GenAddress()

    transaction = {
        'sender_blockchain_address': sender.address,
        'recipient_blockchain_address': receiver.address,
        'value': float(10)
    }

    verifyTransaction = VerifyTransaction()
    signature = verifyTransaction.generate_signature(sender.privkey, transaction)
    print("signature = "+signature)

    print(verifyTransaction.verify_transaction_signature(sender.pubkey,signature,transaction))
