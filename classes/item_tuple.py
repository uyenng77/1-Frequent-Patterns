from dataclasses import dataclass
from typing import Tuple

from classes.item import Item


@dataclass(frozen=True)
class ItemTuple:
    """A class representing a tuple with items (can be sorted - compared to the set)."""

    items: Tuple[Item]
