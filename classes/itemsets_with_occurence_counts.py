from dataclasses import dataclass
from typing import Set
from collections import UserDict

from classes.itemset import Itemset


class ItemsetsWithOccurenceCounts(UserDict):
    """
    A class representing a dictionary that has itemsets as key
    and a corresponding occurrence count as value.
    """

    def __init__(self, itemsets: Set[Itemset]):
        """
        Initialize the dictionary with the given itemsets.
        The occurrence count for each itemset is set to 0.
        """
        super().__init__()
        for itemset in itemsets:
            self.data[itemset] = 0

    def add_occurrence(self, itemset: Itemset):
        """
        Add an occurrence of the given itemset.
        If the itemset does not exist, it is added with a count of 1.
        If it exists, its count is incremented by 1.
        """
        if itemset in self.data:
            self.data[itemset] += 1
        else:
            self.data[itemset] = 1

    def remove_occurrence(self, itemset: Itemset):
        """
        Remove an occurrence of the given itemset.
        If the itemset does not exist, nothing happens.
        If it exists, its count is decremented by 1.
        If the count reaches 0, the itemset is removed.
        """
        if itemset in self.data:
            self.data[itemset] -= 1
            if self.data[itemset] == 0:
                del self.data[itemset]

    def set_occurrence_count(self, itemset: Itemset, count: int):
        """
        Set the occurrence count of the given itemset.
        If the itemset does not exist, it is added with the given count.
        """
        self.data[itemset] = count

    def get_occurrence_count(self, itemset: Itemset) -> int:
        """
        Return the occurrence count of the given itemset.
        If the itemset does not exist, return 0.
        """
        return self.data.get(itemset, 0)
