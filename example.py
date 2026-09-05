"""Simple Proof-of-Work mining demonstration.

The script searches for a nonce that makes the SHA-256 hash of a toy block
start with a user-defined number of zeroes.
"""

import hashlib, time, sys

NONCE_LIMIT = 4000000000

# Difficulty defines how many leading hexadecimal zeroes the hash must have.
difficulty = int(sys.argv[1])

# Example data for the block that will be mined.
prev_hash = "65d56y6565s98zeABC"
transactions = "Transaction block hash"


def mine(block_number, transactions, previous_hash, difficulty):
    """Try different nonce values until a hash matches the difficulty."""
    for nonce in range(NONCE_LIMIT):
        # A real blockchain block contains more fields. This demo keeps the
        # input small so the nonce search is easy to understand.
        block = str(block_number) + transactions + previous_hash + str(nonce)

        # SHA-256 always returns the same hash for the same block data.
        hash = hashlib.sha256(block.encode()).hexdigest()

        # The block is considered mined when the hash starts with enough zeroes.
        if hash[:difficulty] == ("0" * difficulty):
            print(f"Successfully mined block {block_number}")
            return hash
        nonce += 1


if __name__ == '__main__':
    start = time.time()
    print("Mining...")
    hash = mine(1, transactions, prev_hash, difficulty)
    elapsed_time = time.time() - start

    # Show the runtime and the valid hash found by the nonce search.
    print(f"Mining took {elapsed_time:.2f} seconds")
    print(f"Block hash: {hash}")
