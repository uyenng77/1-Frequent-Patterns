from typing import List

from classes.fp_tree_header_table_element import FPTreeHeaderTableElement


class FPTreeHeaderTable:
    """A class representing the header table of an FP-tree"""

    # Constructor
    def __init__(self):
        """
        Initialize the HeaderTable
        """
        # Save the arguments
        self.elements: List[FPTreeHeaderTableElement] = list()

    # Function(s)
    def __str__(self) -> str:
        """
        Get a human-readable string representation of the FPTreeHeaderTable

        Returns:
        str: A human-readable string representation of the FPTreeHeaderTable
        """
        # Initialize the string representation
        string_representation = ""

        ## Get the string representations of all elements
        for element in self.elements:
            string_representation = string_representation + element.__str__() + "\n"

        # Return the string representation
        return string_representation
