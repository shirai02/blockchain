import secrets
import ecdsa
import hashlib
import base58


class GenAddress(object):
    def __init__(self):
        p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
        self.privkey = self.new_privkey(p)
        self.pubkey = self.new_pubkey(self.privkey)
        self.address = self.new_address(bytes.fromhex("00"), self.pubkey)

    def new_privkey(self, p):
        privkey = secrets.randbelow(p)
        privkey = format(privkey, 'x')
        # print("PrivateKey = " + privkey)
        return privkey

    def new_pubkey(self, privkey):
        bin_privkey = bytes.fromhex(privkey)
        signing_key = ecdsa.SigningKey.from_string(
            bin_privkey, curve=ecdsa.SECP256k1)
        verifying_key = signing_key.get_verifying_key()
        pubkey = bytes.fromhex("04") + verifying_key.to_string()
        pubkey = pubkey.hex()
        # print("PublicKey = " + pubkey)
        return pubkey

    def new_address(self, version, pubkey):
        ba = bytes.fromhex(pubkey)
        digest = hashlib.sha256(ba).digest()
        new_digest = hashlib.new('ripemd160')
        new_digest.update(digest)
        pubkey_hash = new_digest.digest()

        pre_address = version + pubkey_hash
        address = hashlib.sha256(pre_address).digest()
        address = hashlib.sha256(address).digest()
        checksum = address[:4]
        address = pre_address + checksum
        address = base58.b58encode(address)
        address = address.decode()
        # print("Address = " + address + "\n")
        return address

if __name__ == '__main__':
    newAddress = GenAddress()
