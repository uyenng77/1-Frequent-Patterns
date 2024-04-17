from fpgrowth import FPgrowth

from classes.sorted_dataset import SortedDataset
from classes.sorted_transaction import SortedTransaction
from classes.item import Item
from classes.item_tuple import ItemTuple
from classes.fp_tree import FPTree
from classes.conditional_pattern_base import ConditionalPatternBase
from classes.conditional_pattern import ConditionalPattern

#####
# Test with one conditional pattern
#####


def test_with_one_conditional_pattern_and_a_count_of_one():
    """
    Test the creation of a conditional FP-tree with the only one conditional pattern (with a count of 1).
    """

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Conditional pattern base
    conditional_pattern_base = ConditionalPatternBase(
        {
            ConditionalPattern(
                prefix_items=ItemTuple((Item("Apple"), Item("Cherry"))),
                occurrence_count=1,
            ),
        }
    )

    # Construct the conditional FP-tree
    fp_tree = fpgrowth._construct_conditional_fp_tree(conditional_pattern_base)

    # Construct the expected FP-tree
    expected_fp_tree = FPTree()
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry")]))
    )

    # Check the FP-tree
    assert (
        fp_tree == expected_fp_tree
    ), f"The returned FP-tree is not as expected.\n Returned FP-tree:\n {fp_tree} \n\n Expected FP-tree:\n {expected_fp_tree}."


def test_with_one_conditional_pattern_and_a_count_of_two():
    """
    Test the creation of a conditional FP-tree with the only one conditional pattern (with a count of 2).
    """

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Conditional pattern base
    conditional_pattern_base = ConditionalPatternBase(
        {
            ConditionalPattern(
                prefix_items=ItemTuple((Item("Banana"), Item("Cherry"))),
                occurrence_count=2,
            ),
        }
    )

    # Construct the conditional FP-tree
    fp_tree = fpgrowth._construct_conditional_fp_tree(conditional_pattern_base)

    # Construct the expected FP-tree
    expected_fp_tree = FPTree()
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Banana"), Item("Cherry")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Banana"), Item("Cherry")]))
    )

    # Check the FP-tree
    assert (
        fp_tree == expected_fp_tree
    ), f"The returned FP-tree is not as expected.\n Returned FP-tree:\n {fp_tree} \n\n Expected FP-tree:\n {expected_fp_tree}."


#####
# Test with multiple conditional patterns
#####


def test_with_multiple_conditional_patterns():
    """
    Test the creation of a conditional FP-tree with multiple conditional patterns.
    """

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Conditional pattern base
    conditional_pattern_base = ConditionalPatternBase(
        {
            ConditionalPattern(
                prefix_items=ItemTuple((Item("Banana"), Item("Cherry"))),
                occurrence_count=2,
            ),
            ConditionalPattern(
                prefix_items=ItemTuple((Item("Apple"), Item("Cherry"))),
                occurrence_count=1,
            ),
        }
    )

    # Construct the conditional FP-tree
    fp_tree = fpgrowth._construct_conditional_fp_tree(conditional_pattern_base)

    # Construct the expected FP-tree
    expected_fp_tree = FPTree()
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Banana"), Item("Cherry")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Banana"), Item("Cherry")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry")]))
    )

    # Check the FP-tree
    assert (
        fp_tree == expected_fp_tree
    ), f"The returned FP-tree is not as expected.\n Returned FP-tree:\n {fp_tree} \n\n Expected FP-tree:\n {expected_fp_tree}."
