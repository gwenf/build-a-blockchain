import random
from string import ascii_letters, digits
from transaction import Transaction


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
