from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """A class representing a single item."""

    name: str
