from typing import Set

from classes.dataset import Dataset
from classes.itemset import Itemset
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts
from itertools import combinations  


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
        result = set()
        for transaction in dataset.transactions:
            for item in transaction.items:
                result.add(Itemset(frozenset({item})))
        return result

    def _count_occurrences_of_itemsets(
        self, dataset: Dataset, itemsets: Set[Itemset]
    ) -> ItemsetsWithOccurrenceCounts:
        """
        Count the occurrences of the given itemsets in the dataset.

        Parameters:
        dataset (Dataset): The dataset for which the itemset occurrences should be counted.
        itemsets (Set[Itemset]): The itemsets for which the occurrences should be counted.
                                The itemsets do not need to be present in the dataset.

        Returns:
        ItemsetsWithOccurrenceCounts: A dictionary containing the itemsets as keys and their occurrence counts as values.
        """
        result = ItemsetsWithOccurrenceCounts(itemsets)
        for itemset in itemsets:
            count = 0
            for transaction in dataset.transactions:
                if itemset.items.issubset(transaction.items):
                    count += 1
            result.set_occurrence_count(itemset, count)
        return result

    def _prune_itemsets_below_min_support(
        self,
        itemsets_with_occurrence_counts: ItemsetsWithOccurrenceCounts,
    ) -> Set[Itemset]:
        """
        Prune itemsets that are below the minimum support threshold.

        Parameters:
        itemsets_with_occurrence_counts (ItemsetsWithOccurrenceCounts): A dictionary containing the itemsets as keys and their occurrence counts as values.

        Returns:
        Set[Itemset]: A set containing all itemsets that are considered frequent.
        """
        result = set()
        for itemset, count in itemsets_with_occurrence_counts.items():
            if count >= self.min_support:
                result.add(itemset)
        return result

    def _generate_candidate_itemsets(
        self, frequent_itemsets: Set[Itemset]
    ) -> Set[Itemset]:
        """
        Generate length-k+1 candidate itemsets based on the given frequent itemsets.
        k is the length of the longest frequent itemset.

        Parameters:
        frequent_itemsets (Set[Itemset]): A set containing all frequent itemsets.

        Returns:
        Set[Itemset]: A set containing all length-k+1 candidate itemsets.
        """
        # If there are no frequent itemsets, return an empty set
        if not frequent_itemsets:
            return set()

        # Check if all itemsets have the same length
        if not frequent_itemsets:
            return set()
        
        itemset_lengths = {len(itemset.items) for itemset in frequent_itemsets}
        if len(itemset_lengths) > 1:
            # If itemsets have different lengths, only use the longest ones
            max_length = max(itemset_lengths)
            frequent_itemsets = {itemset for itemset in frequent_itemsets if len(itemset.items) == max_length}

        candidates = set()
        frequent_itemsets_items = {itemset.items for itemset in frequent_itemsets}
        frequent_list = list(frequent_itemsets)
        
        # Generate candidates by joining frequent itemsets
        for i in range(len(frequent_list)):
            for j in range(i + 1, len(frequent_list)):
                set1 = frequent_list[i].items
                set2 = frequent_list[j].items
                union = set1.union(set2)
                
                # Only consider if the union has exactly one more item than the original itemsets
                # Only proceed if union creates a (k+1)-itemset
                if len(union) == len(set1) + 1:
                    # Check that all (k)-subsets of the candidate are frequent
                    all_subsets_frequent = all(
                        frozenset(subset) in frequent_itemsets_items
                        for subset in combinations(union, len(set1))
                    )

                    if all_subsets_frequent:
                        candidates.add(Itemset(frozenset(union)))

        return candidates

    def _is_valid_candidate(self, candidate: Itemset, frequent_itemsets: Set[Itemset]) -> bool:
        """
        Check if a candidate itemset is valid by ensuring all its (k-1)-subsets are frequent.
        This implements the apriori property for pruning.

        Parameters:
        candidate (Itemset): The candidate itemset to validate.
        frequent_itemsets (Set[Itemset]): Set of known frequent itemsets.

        Returns:
        bool: True if the candidate is valid, False otherwise.
        """
        candidate_items = list(candidate.items)
        
        # For each item in the candidate, create a subset without that item
        for i in range(len(candidate_items)):
            subset_items = frozenset(candidate_items[:i] + candidate_items[i+1:])
            subset = Itemset(subset_items)
            # If any (k-1)-subset is not frequent, the candidate is invalid
            if subset not in frequent_itemsets:
                return False
        
        return True

    def fit(self, dataset: Dataset):
        """
        Use the Apriori algorithm to find all frequent itemsets in the given dataset.
        Saves the frequent itemsets in the frequent_itemsets attribute.

        Parameters:
        dataset (Dataset): The dataset to which the Apriori algorithm should be fitted.
        """
        # Reset the set of frequent itemsets
        self.frequent_itemsets = set()
        
        # Start with 1-itemsets
        current_itemsets = self._generate_one_itemsets(dataset)
        
        # Main Apriori loop
        while current_itemsets:
            # Count occurrences of current itemsets
            itemsets_with_counts = self._count_occurrences_of_itemsets(dataset, current_itemsets)
            
            # Prune itemsets below minimum support
            frequent_current = self._prune_itemsets_below_min_support(itemsets_with_counts)
            
            # Add frequent itemsets to the overall result
            self.frequent_itemsets.update(frequent_current)
            
            # Generate candidates for next iteration
            current_itemsets = self._generate_candidate_itemsets(frequent_current)