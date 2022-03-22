"""
Step 1: Create a basic Block class.
Step 2: Create a basic Transaction class.
Step 3: Create helper functions to generate addresses and transactions.

"""
from block import Block
from helpers import generate_transaction


def main():
    """
    Creates a block, populates it with random transactions, and prints it.
    """
    block = Block()
    for _ in range(5):
        block.add_transaction(generate_transaction())
    print(block)


if __name__ == "__main__":
    main()
