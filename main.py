import pandas as pd
import hashlib
import pprint
import BlockChain


def main():
    usr1 = "a"
    usr2 = "b"
    usr3 = "c"

    blockChain = BlockChain.BlockChain("minor")

    blockChain.add_transaction(usr1,usr2,30)
    blockChain.add_transaction(usr2,usr3,10)
    blockChain.add_transaction(usr3,usr1,10)

    # blockChain.create_block(0,blockChain.hash(blockChain.chain[-1]))
    blockChain.mining()
    # pprint.pprint(blockChain.transaction_pool)
    pprint.pprint(blockChain.chain)


if __name__ == '__main__':
    main()
