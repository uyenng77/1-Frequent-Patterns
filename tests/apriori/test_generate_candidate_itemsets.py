from apriori import Apriori

from classes.item import Item
from classes.itemset import Itemset
from classes.itemsets_with_occurrence_counts import ItemsetsWithOccurrenceCounts

#####
# Test with 1-itemsets
#####


def test_with_one_itemsets():
    """Test the generation of 2-itemsets with a set of 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # Create a set of 1-itemsets
    one_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
    }

    # Generate the candidate itemsets
    candidate_itemsets = apriori._generate_candidate_itemsets(one_itemsets)

    # Create sets of expected and generated item names for easier comparison
    expected_itemsets = {
        Itemset(frozenset({Item("Apple"), Item("Banana")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - candidate_itemsets
    extra_itemsets = candidate_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
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


def test_with_two_itemsets_and_all_combinations_being_valid_candidate_three_itemsets():
    """Test the generation of 3-itemsets with a set of 2-itemsets. Every possible combination should be a valid candidate 3-itemset."""

    # Create the Apriori object
    apriori = Apriori()

    # Create a set of frequent itemsets (of course the 1-itemsets have to be frequent, too)
    itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Banana")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})),
    }

    # Generate the candidate itemsets
    candidate_itemsets = apriori._generate_candidate_itemsets(itemsets)

    # Create sets of expected and generated item names for easier comparison
    expected_itemsets = {
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry"), Item("Dragonfruit")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - candidate_itemsets
    extra_itemsets = candidate_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_two_itemsets_and_only_one_valid_candidate_three_itemset():
    """Test the generation of 3-itemsets with a set of 2-itemsets. Only one valid candidate 3-itemset should be generated."""

    # Create the Apriori object
    apriori = Apriori()

    # Create a set of frequent itemsets (of course the 1-itemsets have to be frequent, too)
    itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Banana")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry")})),
    }

    # Generate the candidate itemsets
    candidate_itemsets = apriori._generate_candidate_itemsets(itemsets)

    # Create sets of expected and generated item names for easier comparison
    # Be careful: Only (Apple, Banana, Cherry) is a valid length-3 candidate itemset as the other possible combinations always contain a subset that is not frequent
    expected_itemsets = {
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Cherry")})),
    }

    # Check the itemsets
    missing_itemsets = expected_itemsets - candidate_itemsets
    extra_itemsets = candidate_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_two_itemsets_and_no_valid_candidate_three_itemsets():
    """Test the generation of 3-itemsets with a set of 2-itemsets. No valid candidate 3-itemset should be generated."""

    # Create the Apriori object
    apriori = Apriori()

    # Create a set of frequent itemsets (of course the 1-itemsets have to be frequent, too)
    itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Banana")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})),
    }

    # Generate the candidate itemsets
    candidate_itemsets = apriori._generate_candidate_itemsets(itemsets)

    # Create sets of expected and generated item names for easier comparison
    # Be careful: No valid length-3 candidate itemset can be generated as the possible combinations always contain a subset that is not frequent
    expected_itemsets = set()

    # Check the itemsets
    extra_itemsets = candidate_itemsets - expected_itemsets

    # Make extra itemsets easier printable
    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
