from dataclasses import dataclass

from classes.item_tuple import ItemTuple


@dataclass(frozen=True)
class ConditionalPattern:
    """
    A class representing a single conditional pattern.

    Contains the prefix_items from top to bottom (= the prefix_items have to be ordered according to f-list) and a occurrence count for this conditional pattern.
    """

    prefix_items: ItemTuple
    occurrence_count: int
