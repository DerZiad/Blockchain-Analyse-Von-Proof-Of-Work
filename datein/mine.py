import hashlib,time,sys

NONCE_LIMIT = 4000000000
difficulty = int(sys.argv[1])
prev_hash = "65d56y6565s98zeABC"
transactions = "Transaction block hash"


def mine(block_number, transactions, previous_hash, difficulty):
    for nonce in range(NONCE_LIMIT):
        block = str(block_number) + transactions + previous_hash + str(nonce)
        hash = hashlib.sha256(block.encode()).hexdigest()
        if hash[:difficulty] == ("0" * difficulty):
            print(f"Successfully mined block {block_number}")
            return hash
        nonce += 1


if __name__ == '__main__':
    start = time.time()
    print("Mining...")
    hash = mine(1, transactions, prev_hash, difficulty)
    elapsed_time = time.time() - start
    print(f"Mining took {elapsed_time:.2f} seconds")
    print(f"Block hash: {hash}")