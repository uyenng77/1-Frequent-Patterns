from dataclasses import dataclass
from typing import FrozenSet, Iterator

from classes.item import Item


@dataclass(frozen=True)
class Itemset:
    """A class representing a set of items (commonly known as an itemset)."""

    items: FrozenSet[Item]

    def __iter__(self) -> Iterator[Item]:
        """Helps to iterate over the items."""
        return iter(self.items)
