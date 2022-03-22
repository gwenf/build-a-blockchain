"""
1. Create a new helper function to hash blocks.
2. Create a function to initialize new blocks.
3. Initialize a new block with a reference to the previous block (if applicable).
4. Generate transactions and add them to the new block until it's full.
5. Add the new block to the list of blocks ("blockchain").
6. Repeat from step 3 for as blocks as you want to create.
"""
from helpers import create_block, generate_transaction


def main():
    """
    Loops through a pre-defined list of blocks,
    adds transactions to the blocks until they fill up (read the BLOCK_SIZE),
    then appends the block to the list of blocks.
    The blocks are printed at the end.
    """
    BLOCK_SIZE = 5  # number of txs per block
    blocks = []

    # creating 5 new blocks in this loop
    for _ in range(5):
        block = create_block(blocks)

        for _ in range(BLOCK_SIZE):
            block.add_transaction(generate_transaction())

        blocks.append(block)

    for block in blocks:
        print(f"Block Number: {block.number}\n")
        print(f"Hash of Previous Block: {block.prev_block_hash}\n")
        print("Transactions")
        print(f"{block}\n")
        print("-" * 80 + "\n")


if __name__ == "__main__":
    main()
