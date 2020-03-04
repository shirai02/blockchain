import hashlib
import json
import time
import pprint
import Transaction


class BlockChain(object):

    def __init__(self):
        self.transaction_pool = []
        self.chain = []
        self.create_block(0, self.hash({}))

    def create_block(self, nonce, previous_hash):
        block = {
            'timestamp': time.time(),
            'transactions': self.transaction_pool,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        self.transaction_pool = []

        return block

    def hash(self, block):
        return hashlib.sha256(json.dumps(block).encode()).hexdigest()

    def add_transaction(self, transaction, signature, sender_public_key):
        if Transaction.VerifyTransaction().verify_transaction_signature(sender_public_key, signature, transaction):
            # print("verified transaction : ")
            # pprint.pprint(transaction)
            self.transaction_pool.append(transaction)
            return True
        else:
            print("unverified transaction : ")
            pprint.pprint(transaction)
            return False

    # 決められた値になっているかどうか検証するメソッド
    def valid_proof(self, transactions, previous_hash, nonce,):
        guess_block = {
            'transactions': transactions,
            'nonce': nonce,
            'previous_hash': previous_hash
        }
        guess_hash = self.hash(guess_block)
        # 前から3文字が000だったらtrueを返し、違ったらfalseを返す
        return guess_hash[:3] == '0' * 3

    # 決められた値になるまでナンスの値を変え続けるメソッド
    def proof_of_work(self):
        transactions = self.transaction_pool.copy()
        previous_hash = self.hash(self.chain[-1])
        nonce = 0
        # 決められた値になるまでナンスの値を変え続ける
        while self.valid_proof(transactions, previous_hash, nonce) is False:
            nonce += 1
        return nonce

    # マイニングの報酬でもらえる通貨は送り主(sender)がいないためあらかじめ決めておく
    MINING_SENDER = 'THIS IS MINING SENDER'
    # マイニングの報酬を決めておく
    MINING_REWARD = 1
    # マイニングのメソッド

    def mining(self, minor_address):
        # マイニングで得られた報酬も一応取引なので未承認の取引リストに追加する
        self.transaction_pool.append({
            'sender_blockchain_address': self.MINING_SENDER,
            'recipient_blockchain_address': minor_address,
            'value': float(self.MINING_REWARD)
        })
        nonce = self.proof_of_work()
        previous_hash = self.hash(self.chain[-1])  # 一つ前のブロックをハッシュ化
        # ナンスと前のブロックのハッシュ値を用いてブロックを作る
        self.create_block(nonce, previous_hash)
        return True
