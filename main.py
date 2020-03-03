import pandas as pd
import hashlib
import pprint
import BlockChain


def main():
    usr1 = "a"
    usr2 = "b"
    usr3 = "c"

    blockChain = BlockChain.BlockChain("minor")

    for i in range(10):
        blockChain.add_transaction(usr1, usr2, 30)
        blockChain.add_transaction(usr2, usr3, 10)
        blockChain.add_transaction(usr3, usr1, 10)

        blockChain.mining()

    pprint.pprint(blockChain.chain)


if __name__ == '__main__':
    main()
