from typing import Set

from classes.dataset import Dataset
from classes.itemset import Itemset
from classes.itemsets_with_occurence_counts import ItemsetsWithOccurenceCounts


class Apriori:
    def __init__(self, min_support: int = 2):
        """
        Initialize the Apriori algorithm with the a minimum (absolute) support.

        Parameters:
        min_support (int): The minimum (absolute) support. This parameter defines the minimum number
                           of occurrences an itemset must have to be considered frequent. Must be a positive integer.
                           Default value is 2.
        """
        # Ensure that the minimum support is a positive integer
        if not isinstance(min_support, int) or min_support < 1:
            raise ValueError("The minimum support must be a positive integer.")

        self.min_support = min_support
        self.frequent_itemsets = set()

    def _generate_one_itemsets(self, dataset: Dataset) -> Set[Itemset]:
        """
        Generate all 1-itemsets for the given dataset.

        Parameters:
        dataset (Dataset): The dataset for which the 1-itemsets should be generated.

        Returns:
        Set[Itemset]: A set containing all 1-itemsets that are contained in the dataset.
        """
        # TODO

    def _count_occurences_of_itemsets(
        self, dataset: Dataset, itemsets: Set[Itemset]
    ) -> ItemsetsWithOccurenceCounts:
        """
        Count the occurrences of the given itemsets in the dataset.

        Parameters:
        dataset (Dataset): The dataset for which the itemset occurrences should be counted.
        itemsets (Set[Itemset]): The itemsets for which the occurrences should be counted. The itemsets do not need to be present in the dataset.

        Returns:
        ItemsetsWithOccurenceCounts: A dictionary containing the itemsets as keys and their occurrence counts as values.
        """
        # TODO

    def _prune_itemsets_below_min_support(
        self,
        itemsets_with_occurence_counts: ItemsetsWithOccurenceCounts,
    ) -> Set[Itemset]:
        """
        Prune itemsets that are below the minimum support threshold.

        Parameters:
        itemsets_with_occurence_counts (ItemsetsWithOccurenceCounts): A dictionary containing the itemsets as keys and their occurrence counts as values.

        Returns:
        Set[Itemset]: A set containing all itemsets that are considered frequent.
        """
        # TODO

    def _generate_candidate_itemsets(
        self, frequent_itemsets: Set[Itemset]
    ) -> Set[Itemset]:
        """
        Generate length-k+1 candidate itemsets based on the given frequent itemsets. k is the length of the longest frequent itemset.

        Parameters:
        frequent_itemsets (Set[Itemset]): A set containing all frequent itemsets.

        Returns:
        Set[Itemset]: A set containing all length-k+1 candidate itemsets.
        """
        # If there are no frequent itemsets, return an empty set
        if not frequent_itemsets:
            return set()

        # TODO

    def fit(self, dataset: Dataset):
        """
        Use the Apriori algorithm to find all frequent itemsets in the given dataset.
        Saves the frequent itemsets in the frequent_itemsets attribute.

        Parameters:
        dataset (Dataset): The dataset to which the Apriori algorithm should be fitted.
        """
        # Reset the set of frequent itemsets
        self.frequent_itemsets = set()

        # TODO
