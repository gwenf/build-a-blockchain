class Transaction:
    """A basic Transaction."""

    def __init__(self, to_, from_, amount):
        self.to_ = to_
        self.from_ = from_
        self.amount = amount

    def __repr__(self):
        return (
            f"from: {self.from_:<37}"
            f"to: {self.to_:<37}"
            f"amount: {self.amount}"
        )
