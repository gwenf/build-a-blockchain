"""
1. Create a new block (increment the block number for every new block).
2. Add transactions to the block until it fills up.
3. Append block to "chain".
4. Repeat from step 1.
"""
from block import Block
from helpers import generate_transaction


def main():
    """
    Creates an arbitrary number of blocks,
    fills each block with transactions up to the BLOCK_SIZE,
    and appends the block to the list of blocks.
    Finally, each block is printed.
    """
    BLOCK_SIZE = 5  # number of txs per block
    blocks = []

    # creating 5 new blocks in this loop
    for _ in range(5):
        block = Block()

        for _ in range(BLOCK_SIZE):
            block.add_transaction(generate_transaction())

        blocks.append(block)

    for block in blocks:
        print(f"Block Number: {block.number}\n")
        print("Transactions")
        print(f"{block}\n")
        print("-" * 80 + "\n")


if __name__ == "__main__":
    main()
