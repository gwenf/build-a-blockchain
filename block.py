class Block:
    """A basic Block."""

    def __init__(self):
        self.sequence = 0  # genesis block
        self.transactions = []  # transaction ledger

    def add_transaction(self, tx):
        """Adds a transaction to the block's ledger."""
        self.transactions.append(tx)

    def __repr__(self):
        return "\n".join([str(tx) for tx in self.transactions])
