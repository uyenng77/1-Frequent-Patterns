from typing import List

from classes.item import Item
from classes.fp_tree_node import FPTreeNode


class FPTreeHeaderTableElement:
    """A class representing an element of the header table of an FP-tree. It contains the item, the overall occurrence count, and links to all nodes of the item."""

    def __init__(
        self,
        item: Item,
        overall_occurrence_count: int,
        node_links: List[FPTreeNode],
    ):
        """
        Initialize the HeaderTableElement with the given item, overall occurrence count, and node links.

        Parameters:
        item (Item): The item that the element represents.
        overall_occurrence_count (int): The overall occurrence count of the item.
        node_links (List[FPTreeNode]): A list of all nodes of the item.
        """

        # Save the arguments
        self.item = item
        self.overall_occurrence_count = overall_occurrence_count
        self.node_links = node_links  # Links to every item node regarding our item

    # Function(s)
    def __str__(self) -> str:
        """
        Get a human-readable string representation of the element

        Returns:
        str: A human-readable string representation of the element
        """
        # Create a string with all necessary information
        return (
            self.item.name
            + ": "
            + str(self.overall_occurrence_count)
            + " - Count of linked nodes: "
            + str(len(self.node_links))
        )
