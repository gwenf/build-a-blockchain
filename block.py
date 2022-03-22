import itertools


class Block:
    """A basic Block."""

    number = itertools.count()

    def __init__(self):
        self.number = next(Block.number)
        self.transactions = []

    def add_transaction(self, tx):
        """Adds a transaction to the block's ledger."""
        self.transactions.append(tx)

    def __repr__(self):
        return "\n".join([str(tx) for tx in self.transactions])
