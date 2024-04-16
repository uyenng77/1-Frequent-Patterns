from dataclasses import dataclass
from typing import FrozenSet

from classes.transaction import Transaction


@dataclass(frozen=True)
class Dataset:
    """A class representing a (transactional) dataset."""

    transactions: FrozenSet[Transaction]
