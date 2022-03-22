import random
from hashlib import sha256
from string import ascii_letters, digits
from transaction import Transaction
from block import Block


def generate_address() -> str:
    """
    Returns a randomly-generated Base58Check address.

    https://en.bitcoin.it/wiki/Base58Check_encoding
    """
    omit_chars = ("0", "O", "I", "l")  # invalid address characters
    chars = [c for c in ascii_letters + digits if c not in omit_chars]
    # randomly choose 26-35 characters as the address
    address = []
    for _ in range(random.randint(26, 35)):
        address.append(random.choice(chars))
    return "".join(address)


def generate_transaction() -> Transaction:
    """Returns a randomly-generated transaction."""
    to_ = generate_address()
    from_ = generate_address()
    amount = random.randint(1, 10)  # random amount for now
    return Transaction(to_=to_, from_=from_, amount=amount)


def hash_block(block: Block) -> str:
    """Hashes the string representation of a block."""
    block_str = str(block)
    return sha256(block_str.encode()).hexdigest()


def create_block(blocks: list) -> Block:
    """Initializes a new empty block."""
    try:
        prev_block_hash = hash_block(blocks[-1])
    except IndexError:
        prev_block_hash = ""

    block = Block(prev_block_hash)
    return block
