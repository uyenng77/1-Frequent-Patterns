from typing import List

from classes.fp_tree_item_node import FPTreeItemNode
from classes.fp_tree_header_table import FPTreeHeaderTable
from classes.fp_tree_node import FPTreeNode


class FPTreeRootNode(FPTreeNode):
    """The RootNode of the FP-tree"""

    def __init__(self):
        """
        Initialize the RootNode
        """
        # Call the constructor of the superclass
        super().__init__()

        # The root node has no parent
        self.parent = None

    # Functions
    def add_to_header_table(self, header_table: FPTreeHeaderTable):
        """
        Add this FPTreeRootNode to the given FPTreeHeaderTable

        Parameters:
        header_table (FPTreeHeaderTable): The FPTreeHeaderTable to which the node should be added.
        """
        # The root node itself is not part of the HeaderTable

        # But the all childs have to be added
        for child in self.childs:
            # Recursive call of the add_to_header_table() function
            child.add_to_header_table(header_table)

    def get_predecessors(self) -> List[FPTreeItemNode]:
        """
        Get the predecessors (there is no predecessor to a root node)

        Returns:
        List[FPTreeItemNode]: An empty list as there are no predecessors
        """
        # Return an empty list as there are no predecessors
        return []

    def get_all_item_nodes(self) -> List[FPTreeItemNode]:
        """
        Get all item nodes within the FPTree

        Returns:
        List[FPTreeItemNode]: A list of all item nodes within the FPTree
        """
        # Init an empty list to add all ItemNodes to
        node_list = []

        # Go through all childs and add there lists to this node_list
        for child in self.childs:
            node_list.extend(child.get_all_item_nodes())

        return node_list

    def is_single_path(self) -> bool:
        """
        Check whether the RootNode has only a single path behind it

        Returns:
        bool: True if there is only a single path behind the RootNode, False otherwise
        """
        # If there is more then one child return False
        if len(self.childs) > 1:
            return False
        # If there is exactly one child ask that child if there is only a single path
        elif len(self.childs) == 1:
            return self.childs[0].is_single_path()
        # If there are no childs there is only a single path
        else:
            return True

    def is_empty(self) -> bool:
        """
        Check whether the FPTree is empty

        Returns:
        bool: True if the FPTree is empty, False otherwise
        """
        # If there at least one child return False
        if len(self.childs) >= 1:
            return False
        # Otherwise return true
        return True

    def __str__(self) -> str:
        """
        Get a human-readable string representation of the FPTreeRootNode

        Parameters:
        level (int): The level of the current node in the tree.

        Returns:
        str: A human-readable string representation of the FPTreeRootNode.
        """
        # Get the item of the RootNode
        string_representation = "Root"

        # Get the string representations of all childs
        for child in self.childs:
            string_representation = string_representation + "\n" + child.__str__(1)

        # Return the string representation
        return string_representation

    def __eq__(self, value: object) -> bool:
        """
        Checks if two FPTreeRootNodes are equal.
        Equal FPTreeRootNodes have equal childs.

        Parameters:
        value (object): The other FPTreeRootNode to compare with

        Returns:
        bool: True if the FPTreeRootNodes are equal, False otherwise
        """
        # Check if the value is a FPTreeRootNode
        if not isinstance(value, FPTreeRootNode):
            return False

        # Check if the childs are equal
        # The order of the childs does not matter
        for child in self.childs:
            if child not in value.childs:
                return False
        for child in value.childs:
            if child not in self.childs:
                return False
        return True
