from dataclasses import dataclass

from classes.itemset import Itemset


@dataclass(frozen=True)
class Transaction:
    """A class representing a single transaction."""

    id: int
    items: Itemset
