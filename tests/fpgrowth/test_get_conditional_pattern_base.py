from fpgrowth import FPgrowth

from classes.item import Item
from classes.item_tuple import ItemTuple
from classes.fp_tree import FPTree
from classes.conditional_pattern_base import ConditionalPatternBase
from classes.conditional_pattern import ConditionalPattern

#####
# Test with only one correct conditional pattern
#####


def test_with_only_one_correct_conditional_pattern_above_min_support():
    """
    Test the creation of the conditional pattern base with only one correct conditional pattern.

    The conditional pattern has a count above the min support.
    """

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Construct the  FP-tree
    fp_tree = FPTree()
    fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
    )
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Cherry")])))
    fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
    )
    fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Dragonfruit")]))
    )
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")])))

    # Create the conditional pattern base
    conditional_pattern_base = fpgrowth._get_conditional_pattern_base(
        Item("Banana"), fp_tree
    )

    # Create the expected conditional pattern base
    expected_conditional_pattern_base = ConditionalPatternBase(
        {
            ConditionalPattern(
                prefix_items=ItemTuple((Item("Apple"), Item("Cherry"))),
                occurrence_count=2,
            ),
        }
    )

    # Check if all expected conditional patterns are in the conditional pattern base
    for (
        expected_conditional_pattern
    ) in expected_conditional_pattern_base.conditional_patterns:
        # For better error messages
        expected_conditional_pattern_text = ", ".join(
            item.name for item in expected_conditional_pattern.prefix_items.items
        )

        assert (
            expected_conditional_pattern
            in conditional_pattern_base.conditional_patterns
        ), f"The conditional pattern {expected_conditional_pattern_text}:{expected_conditional_pattern.occurrence_count} is missing in the conditional pattern base."

    # Check if all returned conditional patterns are in the expected conditional pattern base
    for conditional_pattern in conditional_pattern_base.conditional_patterns:
        # For better error messages
        conditional_pattern_text = ", ".join(
            item.name for item in conditional_pattern.prefix_items.items
        )

        assert (
            conditional_pattern
            in expected_conditional_pattern_base.conditional_patterns
        ), f"The conditional pattern {conditional_pattern_text}:{conditional_pattern.occurrence_count} should not be in the conditional pattern base."


def test_with_only_one_correct_conditional_pattern_below_min_support():
    """
    Test the creation of the conditional pattern base with only one correct conditional pattern.

    The conditional pattern has a count below the min support.
    """

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Construct the  FP-tree
    fp_tree = FPTree()
    fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
    )
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Cherry"), Item("Banana")])))
    fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
    )
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple"), Item("Cherry")])))
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")])))

    # Create the conditional pattern base
    conditional_pattern_base = fpgrowth._get_conditional_pattern_base(
        Item("Dragonfruit"), fp_tree
    )

    # Create the expected conditional pattern base
    expected_conditional_pattern_base = ConditionalPatternBase(
        {
            ConditionalPattern(
                prefix_items=ItemTuple(tuple([Item("Apple")])),
                occurrence_count=1,
            ),
        }
    )

    # Check if all expected conditional patterns are in the conditional pattern base
    for (
        expected_conditional_pattern
    ) in expected_conditional_pattern_base.conditional_patterns:
        # For better error messages
        expected_conditional_pattern_text = ", ".join(
            item.name for item in expected_conditional_pattern.prefix_items.items
        )

        assert (
            expected_conditional_pattern
            in conditional_pattern_base.conditional_patterns
        ), f"The conditional pattern {expected_conditional_pattern_text}:{expected_conditional_pattern.occurrence_count} is missing in the conditional pattern base."

    # Check if all returned conditional patterns are in the expected conditional pattern base
    for conditional_pattern in conditional_pattern_base.conditional_patterns:
        # For better error messages
        conditional_pattern_text = ", ".join(
            item.name for item in conditional_pattern.prefix_items.items
        )

        assert (
            conditional_pattern
            in expected_conditional_pattern_base.conditional_patterns
        ), f"The conditional pattern {conditional_pattern_text}:{conditional_pattern.occurrence_count} should not be in the conditional pattern base."


#####
# Test with multiple correct conditional patterns
#####


def test_with_multiple_correct_conditional_patterns():
    """
    Test the creation of the conditional pattern base with multiple correct conditional patterns.
    """
    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Construct the  FP-tree
    fp_tree = FPTree()
    fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
    )
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Cherry"), Item("Banana")])))
    fp_tree.add_items_to_tree(
        ItemTuple(
            tuple([Item("Apple"), Item("Cherry"), Item("Banana"), Item("Dragonfruit")])
        )
    )
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple"), Item("Cherry")])))
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")])))
    fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")])))

    # Create the conditional pattern base
    conditional_pattern_base = fpgrowth._get_conditional_pattern_base(
        Item("Dragonfruit"), fp_tree
    )

    # Create the expected conditional pattern base
    expected_conditional_pattern_base = ConditionalPatternBase(
        {
            ConditionalPattern(
                prefix_items=ItemTuple(tuple([Item("Apple")])),
                occurrence_count=2,
            ),
            ConditionalPattern(
                prefix_items=ItemTuple(
                    tuple([Item("Apple"), Item("Cherry"), Item("Banana")])
                ),
                occurrence_count=1,
            ),
        }
    )

    # Check if all expected conditional patterns are in the conditional pattern base
    for (
        expected_conditional_pattern
    ) in expected_conditional_pattern_base.conditional_patterns:
        # For better error messages
        expected_conditional_pattern_text = ", ".join(
            item.name for item in expected_conditional_pattern.prefix_items.items
        )

        assert (
            expected_conditional_pattern
            in conditional_pattern_base.conditional_patterns
        ), f"The conditional pattern {expected_conditional_pattern_text}:{expected_conditional_pattern.occurrence_count} is missing in the conditional pattern base. {fp_tree}"

    # Check if all returned conditional patterns are in the expected conditional pattern base
    for conditional_pattern in conditional_pattern_base.conditional_patterns:
        # For better error messages
        conditional_pattern_text = ", ".join(
            item.name for item in conditional_pattern.prefix_items.items
        )

        assert (
            conditional_pattern
            in expected_conditional_pattern_base.conditional_patterns
        ), f"The conditional pattern {conditional_pattern_text}:{conditional_pattern.occurrence_count} should not be in the conditional pattern base. {fp_tree}"
