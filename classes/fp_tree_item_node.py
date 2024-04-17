from typing import List

from classes.item import Item
from classes.fp_tree_node import FPTreeNode
from classes.fp_tree_header_table_element import FPTreeHeaderTableElement
from classes.fp_tree_header_table import FPTreeHeaderTable


class FPTreeItemNode(FPTreeNode):
    """A single node in the FP-tree representing an item and an occurrence count."""

    def __init__(
        self,
        item: Item,
        occurrence_count: int,
        parent: FPTreeNode,
    ):
        """
        Initialize the ItemNode with the given item, occurrence count, and parent.

        Parameters:
        item (Item): The item that the node represents.
        occurrence_count (int): The number of occurrences of the item.
        parent (FPTreeNode): The parent node of the item node.
        """

        # Save the arguments
        self.item = item
        self.occurrence_count = occurrence_count
        self.parent = parent

        # Set the other parameters used later in the lifespan
        self.childs = list()

        # Save the node as child in the parent node
        parent.childs.append(self)

    # Functions
    def add_to_header_table(self, header_table: FPTreeHeaderTable):
        """
        Add this FPTreeItemNode to the given FPTreeHeaderTable.

        Parameters:
        header_table (FPTreeHeaderTable): The FPTreeHeaderTable to which the node should be added.
        """
        # Check if there already is a element for this item
        if len([x for x in header_table.elements if x.item == self.item]) > 0:
            # If there is already an element for this item in the HeaderTable
            # Get the element
            header_table_element = [
                x for x in header_table.elements if x.item == self.item
            ][0]

            # Add the occurrence count to the overall occurrence count
            header_table_element.overall_occurrence_count += self.occurrence_count

            # Add the ItemNode itself to the element_node_links
            header_table_element.node_links.append(self)
        else:
            # If there is no element for this item in the HeaderTable
            # Create a new HeaderTableElement
            header_table_element = FPTreeHeaderTableElement(
                self.item, self.occurrence_count, [self]
            )

            # Add it to the HeaderTable
            header_table.elements.append(header_table_element)

        # Do a recursive call to add_to_header_table for all childs
        for child in self.childs:
            # Recursive call of the add_to_header_table() function
            child.add_to_header_table(header_table)

    def get_predecessors(self) -> List[FPTreeNode]:
        """
        Get the predecessors of this item node (excluding the root node)

        Returns:
        List[FPTreeNode]: The predecessors of this item node.
        """

        # Get the parents predecessors
        predecessors = self.parent.get_predecessors()

        # Add the parent to the predecessors if it is not the root node
        if self.parent.parent != None:
            predecessors.append(self.parent)

        # Return the predecessors
        return predecessors

    def get_all_item_nodes(self) -> List[FPTreeNode]:
        """
        Get all item nodes within the FPTree

        Returns:
        List[FPTreeNode]: All item nodes within the FPTree.
        """
        # Init an list and add this node to it
        node_list = [self]

        # Go through all childs and add their lists to this node_list
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

    def __str__(self, level: int = 0) -> str:
        """
        Get a human-readable string representation of the FPTreeItemNode

        Parameters:
        level (int): The level of the current node in the tree.

        Returns:
        str: A human-readable string representation of the FPTreeItemNode.
        """
        # Get the string representation of the FPTreeItemNode
        string_representation = (
            (" " * (level - 1) * 2)
            + "├── "
            + self.item.name
            + ": "
            + str(self.occurrence_count)
        )

        # Get the string representations of all childs
        for child in self.childs:
            string_representation = (
                string_representation + "\n" + child.__str__(level + 1)
            )

        # Return the string representation
        return string_representation

    def __eq__(self, value: object) -> bool:
        """
        Checks if two FPTreeItemNodes are equal.
        Equal FPTreeItemNodes have equal items, occurrence counts, and childs.

        Parameters:
        value (object): The other FPTreeItemNode to compare with

        Returns:
        bool: True if the FPTreeItemNodes are equal, False otherwise
        """
        if not isinstance(value, FPTreeItemNode):
            return False

        # Check if the item and the occurrence count are equal
        if self.item != value.item or self.occurrence_count != value.occurrence_count:
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
