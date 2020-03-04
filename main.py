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

    blockChain = BlockChain.BlockChain(minor.address)

    for i in range(10):
        blockChain.add_transaction(usr1.address, usr2.address, 30)
        blockChain.add_transaction(usr2.address, usr3.address, 10)
        blockChain.add_transaction(usr3.address, usr1.address, 10)

        blockChain.mining()

    pprint.pprint(blockChain.chain)


if __name__ == '__main__':
    main()
