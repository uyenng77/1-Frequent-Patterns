from fpgrowth import FPgrowth

from classes.item import Item
from classes.itemset import Itemset
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts

#####
# Test with unique occurrence counts for all itemsets
#####


def test_with_itemsets_that_all_have_unique_occurrence_counts():
    """Test the f-list generation with a set of itemsets that all have unique occurrence counts."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Create a set of itemsets with their occurrence counts
    itemsets_with_occurrence_counts = ItemsetsWithOccurrenceCounts(
        frozenset(
            {
                Itemset(frozenset({Item("Apple")})),
                Itemset(frozenset({Item("Banana")})),
                Itemset(frozenset({Item("Cherry")})),
                Itemset(frozenset({Item("Dragonfruit")})),
            }
        )
    )

    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple")})), 2
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Dragonfruit")})), 5
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry")})), 4
    )

    # Generate the f_list
    f_list = fpgrowth._generate_f_list(itemsets_with_occurrence_counts)

    # Put together the expected f_list
    expected_f_list = [
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Apple")})),
    ]

    # Make the f_list and the expected_f_list easier to read
    f_list_text = " -> ".join(
        [item.name for itemset in f_list for item in itemset.items]
    )
    expected_f_list_text = " -> ".join(
        [item.name for itemset in expected_f_list for item in itemset.items]
    )

    # Verify that the f_list contains the itemsets in the correct order
    assert (
        f_list == expected_f_list
    ), f"Expected f_list to be {expected_f_list_text}, but got {f_list_text}."


#####
# Test with some none non unique occurrence counts
#####


def test_with_itemsets_that_have_some_non_unique_occurrence_counts():
    """Test the f-list generation with a set of itemsets that have some non-unique occurrence counts."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Create a set of itemsets with their occurrence counts
    itemsets_with_occurrence_counts = ItemsetsWithOccurrenceCounts(
        frozenset(
            {
                Itemset(frozenset({Item("Apple")})),
                Itemset(frozenset({Item("Banana")})),
                Itemset(frozenset({Item("Cherry")})),
                Itemset(frozenset({Item("Dragonfruit")})),
            }
        )
    )

    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple")})), 2
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Dragonfruit")})), 5
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry")})), 5
    )

    # Generate the f_list
    f_list = fpgrowth._generate_f_list(itemsets_with_occurrence_counts)

    # Put together the expected f_lists
    # Both are valid
    expected_f_list_1 = [
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Apple")})),
    ]

    expected_f_list_2 = [
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Apple")})),
    ]

    # Make the f_list and the expected_f_list easier to read
    f_list_text = " -> ".join(
        [item.name for itemset in f_list for item in itemset.items]
    )
    expected_f_list_1_text = " -> ".join(
        [item.name for itemset in expected_f_list_1 for item in itemset.items]
    )
    expected_f_list_2_text = " -> ".join(
        [item.name for itemset in expected_f_list_2 for item in itemset.items]
    )

    # Verify that the f_list contains the itemsets in the correct order
    assert (
        f_list == expected_f_list_1 or f_list == expected_f_list_2
    ), f"Expected f_list to be {expected_f_list_1_text} or {expected_f_list_2_text}, but got {f_list_text}."
