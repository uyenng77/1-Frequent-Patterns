from typing import List


class FPTreeNode:
    """Superclass for the two FP-tree node types"""

    def __init__(self):
        """
        Initialize the FPTreeNode with the given parent.
        """
        # Set the childs as an empty list
        self.childs = list()

        # Set the occurrence count to 0
        self.occurrence_count = 0

    def get_predecessors(self) -> List["FPTreeNode"]:
        """
        Get the predecessors of this node (excluding the root node)

        Returns:
        List[FPTreeNode]: The predecessors of this item node.
        """
        # A default FP-tree node has no predecessors
        return []
