from dataclasses import dataclass

from classes.item_tuple import ItemTuple


@dataclass(frozen=True)
class SortedTransaction:
    """A class representing a single transaction. The items in the transaction are sorted."""

    id: int
    items: ItemTuple
