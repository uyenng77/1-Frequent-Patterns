from apriori import Apriori

from classes.item import Item
from classes.itemset import Itemset
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts

#####
# Test with 1-itemsets
#####


def test_with_one_itemsets_above_min_support():
    """Test the pruning of 1-itemsets that are all above the minimum support threshold."""

    # Create the Apriori object
    apriori = Apriori(min_support=2)

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
        Itemset(frozenset({Item("Apple")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry")})), 4
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Dragonfruit")})), 5
    )

    # Prune the itemsets
    frequent_itemsets = apriori._prune_itemsets_below_min_support(
        itemsets_with_occurrence_counts
    )

    # Create the expected itemsets
    expected_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - frequent_itemsets
    extra_itemsets = frequent_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier to read
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_one_itemsets_above_and_at_min_support():
    """Test the pruning of 1-itemsets that are above and at the minimum support threshold."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

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
        Itemset(frozenset({Item("Apple")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry")})), 4
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Dragonfruit")})), 5
    )

    # Prune the itemsets
    frequent_itemsets = apriori._prune_itemsets_below_min_support(
        itemsets_with_occurrence_counts
    )

    # Create the expected itemsets
    expected_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - frequent_itemsets
    extra_itemsets = frequent_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier to read
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_one_itemsets_above_at_and_below_min_support():
    """Test the pruning of 1-itemsets that are above, at and below the minimum support threshold."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

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
        Itemset(frozenset({Item("Banana")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry")})), 4
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Dragonfruit")})), 1
    )

    # Prune the itemsets
    frequent_itemsets = apriori._prune_itemsets_below_min_support(
        itemsets_with_occurrence_counts
    )

    # Create the expected itemsets
    expected_itemsets = {
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - frequent_itemsets
    extra_itemsets = frequent_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier to read
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_one_itemsets_below_min_support():
    """Test the pruning of 1-itemsets that are all below the minimum support threshold."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

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
        Itemset(frozenset({Item("Banana")})), 1
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry")})), 0
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Dragonfruit")})), 2
    )

    # Prune the itemsets
    frequent_itemsets = apriori._prune_itemsets_below_min_support(
        itemsets_with_occurrence_counts
    )

    # Create the expected itemsets
    expected_itemsets = set()

    # Check the itemsets
    missing_itemsets = expected_itemsets - frequent_itemsets
    extra_itemsets = frequent_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier to read
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


#####
# Test with 2-itemsets
#####


def test_with_two_itemsets_above_at_and_below_min_support():
    """Test the pruning of 2-itemsets that are above, at and below the minimum support threshold."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

    # Create a set of itemsets with their occurrence counts
    itemsets_with_occurrence_counts = ItemsetsWithOccurrenceCounts(
        frozenset(
            {
                Itemset(frozenset({Item("Apple"), Item("Banana")})),
                Itemset(frozenset({Item("Apple"), Item("Cherry")})),
                Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
                Itemset(frozenset({Item("Banana"), Item("Cherry")})),
                Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})),
                Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})),
            }
        )
    )

    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Banana")})), 2
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Cherry")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})), 1
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana"), Item("Cherry")})), 4
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})), 5
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})), 0
    )

    # Prune the itemsets
    frequent_itemsets = apriori._prune_itemsets_below_min_support(
        itemsets_with_occurrence_counts
    )

    # Create the expected itemsets
    expected_itemsets = {
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - frequent_itemsets
    extra_itemsets = frequent_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier to read
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


#####
# Test with n-itemsets (n > 1 and n < 5)
#####


def test_with_n_itemsets_above_at_and_below_min_support():
    """Test the pruning of n-itemsets (n > 1 and n < 5) that are above, at and below the minimum support threshold."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

    # Create a set of itemsets with their occurrence counts
    itemsets_with_occurrence_counts = ItemsetsWithOccurrenceCounts(
        frozenset(
            {
                Itemset(frozenset({Item("Apple"), Item("Banana")})),
                Itemset(frozenset({Item("Apple"), Item("Cherry")})),
                Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
                Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Cherry")})),
                Itemset(
                    frozenset({Item("Apple"), Item("Banana"), Item("Dragonfruit")})
                ),
                Itemset(
                    frozenset({Item("Apple"), Item("Cherry"), Item("Dragonfruit")})
                ),
                Itemset(
                    frozenset({Item("Banana"), Item("Cherry"), Item("Dragonfruit")})
                ),
                Itemset(
                    frozenset(
                        {
                            Item("Apple"),
                            Item("Banana"),
                            Item("Cherry"),
                            Item("Dragonfruit"),
                        }
                    )
                ),
            }
        )
    )

    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Banana")})), 2
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Cherry")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})), 1
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Cherry")})), 4
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Dragonfruit")})), 5
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Apple"), Item("Cherry"), Item("Dragonfruit")})), 0
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(frozenset({Item("Banana"), Item("Cherry"), Item("Dragonfruit")})), 3
    )
    itemsets_with_occurrence_counts.set_occurrence_count(
        Itemset(
            frozenset(
                {Item("Apple"), Item("Banana"), Item("Cherry"), Item("Dragonfruit")}
            )
        ),
        2,
    )

    # Prune the itemsets
    frequent_itemsets = apriori._prune_itemsets_below_min_support(
        itemsets_with_occurrence_counts
    )

    # Create the expected itemsets
    expected_itemsets = {
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry"), Item("Dragonfruit")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - frequent_itemsets
    extra_itemsets = frequent_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."
