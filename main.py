import pandas as pd
import hashlib
import pprint
import BlockChain
import Transaction
import GenAddress


def main():
    usr1 = GenAddress.GenAddress()
    usr2 = GenAddress.GenAddress()
    usr3 = GenAddress.GenAddress()
    minor = GenAddress.GenAddress()

    blockChain = BlockChain.BlockChain()

    # usr1がトランザクションを生成
    transaction = {
        'sender_blockchain_address': usr1.address,
        'recipient_blockchain_address': usr2.address,
        'value': float(30)
    }
    signature = Transaction.VerifyTransaction(
    ).generate_signature(usr1.privkey, transaction)

    blockChain.add_transaction(transaction, signature, usr1.pubkey)

    # usr2がトランザクションを生成
    transaction = {
        'sender_blockchain_address': usr2.address,
        'recipient_blockchain_address': usr3.address,
        'value': float(10)
    }
    signature = Transaction.VerifyTransaction(
    ).generate_signature(usr2.privkey, transaction)

    blockChain.add_transaction(transaction, signature, usr2.pubkey)

    # usr3がトランザクションを生成
    transaction = {
        'sender_blockchain_address': usr3.address,
        'recipient_blockchain_address': usr1.address,
        'value': float(10)
    }
    signature = Transaction.VerifyTransaction(
    ).generate_signature(usr3.privkey, transaction)

    blockChain.add_transaction(transaction, signature, usr3.pubkey)


    # minorがトランザクションをblockに格納
    if blockChain.mining(minor.address):
        pprint.pprint(blockChain.chain)
    else:
        print("マイニング失敗")


if __name__ == '__main__':
    main()
