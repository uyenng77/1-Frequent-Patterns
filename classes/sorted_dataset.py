from dataclasses import dataclass
from typing import FrozenSet

from classes.sorted_transaction import SortedTransaction


@dataclass(frozen=True)
class SortedDataset:
    """A class representing a (transactional) dataset. The items in the transactions are sorted."""

    transactions: FrozenSet[SortedTransaction]
