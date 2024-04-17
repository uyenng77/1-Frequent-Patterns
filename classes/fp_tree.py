from typing import List

from classes.fp_tree_root_node import FPTreeRootNode
from classes.fp_tree_item_node import FPTreeItemNode
from classes.item_tuple import ItemTuple
from classes.fp_tree_header_table import FPTreeHeaderTable


class FPTree:
    """A class representing an FP-tree."""

    # Constructor
    def __init__(self):
        """
        Initialize the FPTree
        """
        # Create a root node for the tree
        self.root = FPTreeRootNode()

    # Functions
    def add_items_to_tree(self, item_tupel: ItemTuple, occurrence_count: int = 1):
        """
        Add a tuple of items to the FPTree (has to be sorted according to the f-list).

        Parameters:
        item_tupel (ItemTuple): The tuple of items to be added to the FPTree. (sorted according to the f-list)
        occurrence_count (int): The number of occurrences of the item tuple. (default: 1)
        """
        # Set the root node as current node
        current_node = self.root

        # Iterate through the item_tupel
        for item in item_tupel.items:
            # Check if the item is already present as a child of the current node
            if len([x for x in current_node.childs if x.item == item]) > 0:
                # Set the node with the item to be the current_node
                current_node = [x for x in current_node.childs if x.item == item][0]

                # Increase the occurrence count of that node
                current_node.occurrence_count += occurrence_count
            else:
                # Create a new node
                new_node = FPTreeItemNode(item, occurrence_count, current_node)

                # Set the new_node as current_node
                current_node = new_node

    def get_header_table(self) -> FPTreeHeaderTable:
        """
        Get the HeaderTable of the FPTree

        Returns:
        FPTreeHeaderTable: The HeaderTable of the FPTree
        """
        # Create a FPTreeHeaderTable
        header_table = FPTreeHeaderTable()

        # Call the add_to_header_table() function of the FPTreeRootNode
        self.root.add_to_header_table(header_table)

        # Return the header_table
        return header_table

    def get_all_item_nodes(self) -> List[FPTreeItemNode]:
        """
        Get all item nodes within the FPTree

        Returns:
        List[FPTreeItemNode]: A list of all item nodes within the FPTree
        """
        # Ask the root node
        return self.root.get_all_item_nodes()

    def is_single_path(self) -> bool:
        """
        Check whether the FPTree has only a single path

        Returns:
        bool: True if there is only a single path in the FPTree, False otherwise
        """
        # Ask the root node
        return self.root.is_single_path()

    def is_empty(self) -> bool:
        """
        Check whether the FPTree is empty

        Returns:
        bool: True if the FPTree is empty, False otherwise
        """
        # Ask the root node
        return self.root.is_empty()

    def __str__(self) -> str:
        """
        Get a human-readable string representation of the FPTree

        Returns:
        str: A human-readable string representation of the FPTree
        """
        # Get the string representation of the RootNode
        return self.root.__str__()

    def __eq__(self, other) -> bool:
        """
        Checks if two FPTrees are equal.
        Equal FPTrees have the same structure and the same occurrence counts.

        Parameters:
        other (FPTree): The other FPTree to compare with

        Returns:
        bool: True if the FPTrees are equal, False otherwise
        """
        if not isinstance(other, FPTree):
            return False

        return self.root == other.root
