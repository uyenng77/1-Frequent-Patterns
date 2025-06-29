from typing import Set, List

from classes.dataset import Dataset
from classes.itemset import Itemset
from classes.item import Item
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts
from classes.sorted_dataset import SortedDataset
from classes.sorted_transaction import SortedTransaction
from classes.item_tuple import ItemTuple
from classes.fp_tree import FPTree
from classes.conditional_pattern_base import ConditionalPatternBase
from classes.conditional_pattern import ConditionalPattern


class FPgrowth:
    def __init__(self, min_support: int = 2):
        """
        Initialize the FP-growth algorithm with the a minimum (absolute) support.

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

    def _generate_frequent_one_itemsets_with_occurrence_counts(
        self, dataset: Dataset
    ) -> ItemsetsWithOccurrenceCounts:
        """
        Generate all frequent 1-itemsets for the given dataset.

        Parameters:
        dataset (Dataset): The dataset for which the frequent 1-itemsets should be generated.

        Returns:
        ItemsetsWithOccurrenceCounts: A dictionary containing the frequent 1-itemsets as keys and their occurrence counts as values.
        """
        # Count occurrences of each item
        item_counts = {}
        
        for transaction in dataset.transactions:
            for item in transaction.items.items:  # Access the items attribute of Itemset
                if item not in item_counts:
                    item_counts[item] = 0
                item_counts[item] += 1
        
        # Create list of frequent itemsets
        frequent_itemsets_list = []
        for item, count in item_counts.items():
            if count >= self.min_support:
                # Create itemset with frozenset to make it hashable
                itemset = Itemset(frozenset({item}))
                frequent_itemsets_list.append(itemset)
        
        # Create ItemsetsWithOccurrenceCounts
        frequent_one_itemsets = ItemsetsWithOccurrenceCounts(frequent_itemsets_list)
        
        # Set the occurrence counts
        for item, count in item_counts.items():
            if count >= self.min_support:
                itemset = Itemset(frozenset({item}))
                frequent_one_itemsets.set_occurrence_count(itemset, count)
        
        return frequent_one_itemsets

    def _generate_f_list(
        self, frequent_one_itemsets: ItemsetsWithOccurrenceCounts
    ) -> List[Itemset]:
        """
        Generate the f-list for the given frequent 1-itemsets.

        Parameters:
        frequent_one_itemsets (ItemsetsWithOccurrenceCounts): The frequent 1-itemsets with their occurrence counts for which the F-list should be generated.

        Returns:
        List[Itemset]: A f-list containing the frequent 1-itemsets sorted by decreasing occurrence count.
        """
        # Sort itemsets by occurrence count in decreasing order
        sorted_itemsets = sorted(
            frequent_one_itemsets.keys(),
            key=lambda itemset: frequent_one_itemsets.get_occurrence_count(itemset),
            reverse=True
        )
        
        return sorted_itemsets

    def _sort_dataset_according_to_f_list(
        self, dataset: Dataset, f_list: List[Itemset]
    ) -> SortedDataset:
        """
        Sort the dataset according to the given f-list.

        Parameters:
        dataset (Dataset): The dataset to be sorted.
        f_list (List[Itemset]): The f-list according to which the dataset should be sorted.

        Returns:
        SortedDataset: The sorted dataset.
        """
        # Create a mapping from items to their position in f_list for sorting
        item_order = {}
        for i, itemset in enumerate(f_list):
            # Each itemset in f_list should contain only one item (1-itemset)
            item = next(iter(itemset.items))  # Get the single item from the itemset
            item_order[item] = i
        
        sorted_transactions = []
        
        for transaction in dataset.transactions:
            # Filter items that are in f_list and sort them according to f_list order
            filtered_items = []
            for item in transaction.items.items:  # Access the items attribute of Itemset
                if item in item_order:
                    filtered_items.append((item, item_order[item]))
            
            # Sort by f_list order
            filtered_items.sort(key=lambda x: x[1])
            sorted_items = tuple(item for item, _ in filtered_items)
            
            # Only include transactions that have at least one frequent item
            if sorted_items:
                item_tuple = ItemTuple(sorted_items)
                sorted_transaction = SortedTransaction(transaction.id, item_tuple)
                sorted_transactions.append(sorted_transaction)
        
        return SortedDataset(frozenset(sorted_transactions))

    def _construct_initial_fp_tree(self, sorted_dataset: SortedDataset) -> FPTree:
        """
        Construct the initial FP-tree from the given sorted dataset.

        Parameters:
        sorted_dataset (SortedDataset): The sorted dataset from which the initial FP-tree should be constructed.

        Returns:
        FPTree: The initial FP-tree.
        """
        fp_tree = FPTree()
        
        for transaction in sorted_dataset.transactions:
            fp_tree.add_items_to_tree(transaction.items, 1)
        
        return fp_tree

    def _get_conditional_pattern_base(
        self, item: Item, fp_tree: FPTree
    ) -> ConditionalPatternBase:
        """
        Get the conditional pattern base for the given item in the FP-tree.

        Parameters:
        item (Item): The item for which the conditional pattern base should be generated.
        fp_tree (FPTree): The FP-tree from which the conditional pattern base should be extracted.

        Returns:
        ConditionalPatternBase: The conditional pattern base for the given item.
        """
        conditional_patterns = set()
        header_table = fp_tree.get_header_table()
        
        # Find the header table element for the given item
        target_element = None
        for element in header_table.elements:
            if element.item == item:
                target_element = element
                break
        
        if target_element is None:
            return ConditionalPatternBase(frozenset())
        
        # For each node of the item in the tree
        for node in target_element.node_links:
            # Get the path from root to this node (excluding the node itself)
            predecessors = node.get_predecessors()
            
            if predecessors:  # If there are predecessors
                # Create ItemTuple from predecessors (they should already be in f_list order)
                prefix_items = ItemTuple(tuple(pred.item for pred in predecessors))
                conditional_pattern = ConditionalPattern(prefix_items, node.occurrence_count)
                conditional_patterns.add(conditional_pattern)
        
        return ConditionalPatternBase(frozenset(conditional_patterns))

    def _construct_conditional_fp_tree(
        self, conditional_pattern_base: ConditionalPatternBase
    ) -> FPTree:
        """
        Construct a conditional FP-tree from the given conditional pattern base.

        Parameters:
        conditional_pattern_base (ConditionalPatternBase): The conditional pattern base from which the conditional FP-tree should be constructed.

        Returns:
        FPTree: The conditional FP-tree.
        """
        # Count occurrences of each item in the conditional pattern base
        item_counts = {}
        
        item_counts = {}
    for pattern in conditional_pattern_base.conditional_patterns:
        for item in pattern.prefix_items.items:
            item_counts[item] = item_counts.get(item, 0) + pattern.occurrence_count
        
        # Filter items that meet minimum support
        # 2) Keep only those items meeting min_support
    frequent_items = {
        item
        for item, count in item_counts.items()
        if count >= self.min_support
    }
        
        # Construct conditional FP-tree
        # 3) Build the conditional tree
    conditional_fp_tree = FPTree()
    for pattern in conditional_pattern_base.conditional_patterns:
        # filter out infrequent items
        filtered = [
            item
            for item in pattern.prefix_items.items
            if item in frequent_items
        ]
        # sort by descending count, then alphabetically for ties
        filtered.sort(key=lambda it: (-item_counts[it], it))

        if filtered:
            item_tuple = ItemTuple(tuple(filtered))
            conditional_fp_tree.add_items_to_tree(
                item_tuple, pattern.occurrence_count
            )

    return conditional_fp_tree

    def fit(self, dataset: Dataset):
        """
        Use the FP-growth algorithm to find all frequent itemsets in the given dataset.
        Saves the frequent itemsets in the frequent_itemsets attribute.

        Parameters:
        dataset (Dataset): The dataset to which the FP-growth algorithm should be fitted.
        """
        self.frequent_itemsets = set()
        
        # Step 1: Generate frequent 1-itemsets
        frequent_one_itemsets = self._generate_frequent_one_itemsets_with_occurrence_counts(dataset)
        
        # Add frequent 1-itemsets to result
        for itemset in frequent_one_itemsets.keys():
            self.frequent_itemsets.add(itemset)
        
        # Step 2: Generate f-list
        f_list = self._generate_f_list(frequent_one_itemsets)
        
        if not f_list:  # No frequent items
            return
        
        # Step 3: Sort dataset according to f-list
        sorted_dataset = self._sort_dataset_according_to_f_list(dataset, f_list)
        
        # Step 4: Construct initial FP-tree
        initial_fp_tree = self._construct_initial_fp_tree(sorted_dataset)
        
        # Step 5: Mine frequent itemsets recursively
        self._fp_growth_recursive(initial_fp_tree, set(), f_list)

    def _fp_growth_recursive(self, fp_tree: FPTree, alpha: Set[Item], f_list: List[Itemset]):
        """
        Recursive function to mine frequent itemsets using FP-growth.
        
        Parameters:
        fp_tree (FPTree): Current FP-tree
        alpha (Set[Item]): Current suffix pattern
        f_list (List[Itemset]): F-list for ordering
        """
        if fp_tree.is_empty():
            return
        
        # If FP-tree has a single path, generate all combinations
        if fp_tree.is_single_path():
            self._generate_combinations_from_single_path(fp_tree, alpha)
            return
        
        # Get header table and process items in reverse f-list order (bottom-up)
        header_table = fp_tree.get_header_table()
        
        # Create a mapping from items to their f-list order
        item_to_order = {}
        for i, itemset in enumerate(f_list):
            item = next(iter(itemset.items))
            item_to_order[item] = i
        
        # Get items that are actually in the tree and sort them
        items_in_tree = []
        for element in header_table.elements:
            if element.item in item_to_order:
                items_in_tree.append(element.item)
        
        # Sort items by f-list order (reverse for bottom-up processing)
        items_in_tree.sort(key=lambda item: item_to_order[item], reverse=True)
        
        for item in items_in_tree:
            # Create new frequent itemset by adding current item to alpha
            beta = alpha | {item}
            beta_itemset = Itemset(frozenset(beta))
            
            # Calculate support for this itemset by checking conditional pattern base
            conditional_pattern_base = self._get_conditional_pattern_base(item, fp_tree)
            
            # Count support for beta itemset
            support_count = 0
            if not conditional_pattern_base.conditional_patterns:
                # If no conditional patterns, this is a 1-itemset extension
                # Get support from header table
                for element in header_table.elements:
                    if element.item == item:
                        support_count = sum(node.occurrence_count for node in element.node_links)
                        break
            else:
                # For multi-item extensions, sum from conditional patterns
                support_count = sum(pattern.occurrence_count for pattern in conditional_pattern_base.conditional_patterns)
            
            # Only add if meets minimum support
            if support_count >= self.min_support:
                self.frequent_itemsets.add(beta_itemset)
                
                # Construct conditional FP-tree
                conditional_fp_tree = self._construct_conditional_fp_tree(conditional_pattern_base)
                
                # Recursively mine the conditional FP-tree
                if not conditional_fp_tree.is_empty():
                    self._fp_growth_recursive(conditional_fp_tree, beta, f_list)

    def _generate_combinations_from_single_path(self, fp_tree: FPTree, alpha: Set[Item]):
        """
        Generate all frequent itemset combinations from a single path FP-tree.
        
        Parameters:
        fp_tree (FPTree): FP-tree with single path
        alpha (Set[Item]): Current suffix pattern
        """
        # Get all nodes in the single path (excluding root)
        path_nodes = []
        current = fp_tree.root
        
        # Traverse the single path to collect all nodes
        while current and current.children:
            if len(current.children) == 1:  # Single path continues
                child = next(iter(current.children.values()))
                path_nodes.append(child)
                current = child
            else:
                break
        
        if not path_nodes:
            return
        
        # Generate all non-empty subsets of path items
        from itertools import combinations
        
        path_items = [(node.item, node.occurrence_count) for node in path_nodes]
        
        for r in range(1, len(path_items) + 1):
            for combo in combinations(path_items, r):
                # Check if combination meets minimum support
                min_count = min(count for _, count in combo)
                if min_count >= self.min_support:
                    items = {item for item, _ in combo}
                    beta = alpha | items
                    beta_itemset = Itemset(frozenset(beta))
                    self.frequent_itemsets.add(beta_itemset)