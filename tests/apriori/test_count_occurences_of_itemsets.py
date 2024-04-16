from apriori import Apriori

from classes.item import Item
from classes.itemset import Itemset


#####
# Test with the small fruit dataset
#####


def test_with_small_fruit_dataset_and_a_full_list_of_1_itemsets(
    small_fruit_dataset,
):
    """Test the counting of occurrences of 1-itemsets with the small fruit dataset. The list of 1-itemsets is complete and contains all possible 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 1-itemsets
    one_itemsets = set()
    one_itemsets.add(Itemset(frozenset({Item("Apple")})))
    one_itemsets.add(Itemset(frozenset({Item("Banana")})))
    one_itemsets.add(Itemset(frozenset({Item("Cherry")})))
    one_itemsets.add(Itemset(frozenset({Item("Dragonfruit")})))

    # Count the occurrences of the 1-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        small_fruit_dataset, one_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("Apple")})): 4,
        Itemset(frozenset({Item("Banana")})): 2,
        Itemset(frozenset({Item("Cherry")})): 4,
        Itemset(frozenset({Item("Dragonfruit")})): 2,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


def test_with_small_fruit_dataset_and_some_missing_1_itemsets(
    small_fruit_dataset,
):
    """Test the counting of occurrences of 1-itemsets with the small fruit dataset. The list of 1-itemsets is incomplete and contains only some of the possible 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 1-itemsets
    one_itemsets = set()
    one_itemsets.add(Itemset(frozenset({Item("Apple")})))
    one_itemsets.add(Itemset(frozenset({Item("Banana")})))

    # Count the occurrences of the 1-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        small_fruit_dataset, one_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("Apple")})): 4,
        Itemset(frozenset({Item("Banana")})): 2,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


def test_with_small_fruit_dataset_and_an_extra_1_itemsets(
    small_fruit_dataset,
):
    """Test the counting of occurrences of 1-itemsets with the small fruit dataset. The list of 1-itemsets is complete and contains an additional 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 1-itemsets
    one_itemsets = set()
    one_itemsets.add(Itemset(frozenset({Item("Apple")})))
    one_itemsets.add(Itemset(frozenset({Item("Banana")})))
    one_itemsets.add(Itemset(frozenset({Item("Cherry")})))
    one_itemsets.add(Itemset(frozenset({Item("Dragonfruit")})))
    one_itemsets.add(Itemset(frozenset({Item("Elderberry")})))

    # Count the occurrences of the 1-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        small_fruit_dataset, one_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("Apple")})): 4,
        Itemset(frozenset({Item("Banana")})): 2,
        Itemset(frozenset({Item("Cherry")})): 4,
        Itemset(frozenset({Item("Dragonfruit")})): 2,
        Itemset(frozenset({Item("Elderberry")})): 0,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


def test_with_small_fruit_dataset_and_a_full_list_of_2_itemsets(
    small_fruit_dataset,
):
    """Test the counting of occurrences of 2-itemsets with the small fruit dataset. The list of 2-itemsets is complete and contains all possible 2-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 2-itemsets
    two_itemsets = set()
    two_itemsets.add(Itemset(frozenset({Item("Apple"), Item("Banana")})))
    two_itemsets.add(Itemset(frozenset({Item("Apple"), Item("Cherry")})))
    two_itemsets.add(Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})))
    two_itemsets.add(Itemset(frozenset({Item("Banana"), Item("Cherry")})))
    two_itemsets.add(Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})))
    two_itemsets.add(Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})))

    # Count the occurrences of the 2-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        small_fruit_dataset, two_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("Apple"), Item("Banana")})): 1,
        Itemset(frozenset({Item("Apple"), Item("Cherry")})): 3,
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})): 2,
        Itemset(frozenset({Item("Banana"), Item("Cherry")})): 2,
        Itemset(frozenset({Item("Banana"), Item("Dragonfruit")})): 0,
        Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})): 1,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


#####
# Test with the large book dataset
#####


def test_with_large_book_dataset_and_a_full_list_of_1_itemsets(
    large_book_dataset,
):
    """Test the counting of occurrences of 1-itemsets with the large book dataset. The list of 1-itemsets is complete and contains all possible 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 1-itemsets
    one_itemsets = set()
    one_itemsets.add(Itemset(frozenset({Item("The Shadows of Tomorrow")})))
    one_itemsets.add(Itemset(frozenset({Item("Echoes of a Forgotten Realm")})))
    one_itemsets.add(Itemset(frozenset({Item("Whispers of the Ancient World")})))
    one_itemsets.add(Itemset(frozenset({Item("Chronicles of the Unseen")})))
    one_itemsets.add(Itemset(frozenset({Item("Legends of the Fallen Skies")})))
    one_itemsets.add(Itemset(frozenset({Item("Tales of the Crimson Dawn")})))
    one_itemsets.add(Itemset(frozenset({Item("Secrets of the Silent Ocean")})))
    one_itemsets.add(Itemset(frozenset({Item("Memories of the Last Horizon")})))
    one_itemsets.add(Itemset(frozenset({Item("Dreams of the Distant Stars")})))
    one_itemsets.add(Itemset(frozenset({Item("Visions of the Lost Empire")})))

    # Count the occurrences of the 1-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        large_book_dataset, one_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("The Shadows of Tomorrow")})): 3,
        Itemset(frozenset({Item("Echoes of a Forgotten Realm")})): 3,
        Itemset(frozenset({Item("Whispers of the Ancient World")})): 3,
        Itemset(frozenset({Item("Chronicles of the Unseen")})): 3,
        Itemset(frozenset({Item("Legends of the Fallen Skies")})): 3,
        Itemset(frozenset({Item("Tales of the Crimson Dawn")})): 3,
        Itemset(frozenset({Item("Secrets of the Silent Ocean")})): 3,
        Itemset(frozenset({Item("Memories of the Last Horizon")})): 3,
        Itemset(frozenset({Item("Dreams of the Distant Stars")})): 3,
        Itemset(frozenset({Item("Visions of the Lost Empire")})): 3,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


def test_with_large_book_dataset_and_some_missing_1_itemsets(
    large_book_dataset,
):
    """Test the counting of occurrences of 1-itemsets with the large book dataset. The list of 1-itemsets is incomplete and contains only some of the possible 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 1-itemsets
    one_itemsets = set()
    one_itemsets.add(Itemset(frozenset({Item("The Shadows of Tomorrow")})))
    one_itemsets.add(Itemset(frozenset({Item("Echoes of a Forgotten Realm")})))

    # Count the occurrences of the 1-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        large_book_dataset, one_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("The Shadows of Tomorrow")})): 3,
        Itemset(frozenset({Item("Echoes of a Forgotten Realm")})): 3,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


def test_with_large_book_dataset_and_an_extra_1_itemsets(
    large_book_dataset,
):
    """Test the counting of occurrences of 1-itemsets with the large book dataset. The list of 1-itemsets is complete and contains an additional 1-itemsets."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 1-itemsets
    one_itemsets = set()
    one_itemsets.add(Itemset(frozenset({Item("The Shadows of Tomorrow")})))
    one_itemsets.add(Itemset(frozenset({Item("Echoes of a Forgotten Realm")})))
    one_itemsets.add(Itemset(frozenset({Item("Whispers of the Ancient World")})))
    one_itemsets.add(Itemset(frozenset({Item("Chronicles of the Unseen")})))
    one_itemsets.add(Itemset(frozenset({Item("Legends of the Fallen Skies")})))
    one_itemsets.add(Itemset(frozenset({Item("Tales of the Crimson Dawn")})))
    one_itemsets.add(Itemset(frozenset({Item("Secrets of the Silent Ocean")})))
    one_itemsets.add(Itemset(frozenset({Item("Memories of the Last Horizon")})))
    one_itemsets.add(Itemset(frozenset({Item("Dreams of the Distant Stars")})))
    one_itemsets.add(Itemset(frozenset({Item("Visions of the Lost Empire")})))
    one_itemsets.add(Itemset(frozenset({Item("Tales of the Ancient World")})))

    # Count the occurrences of the 1-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        large_book_dataset, one_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(frozenset({Item("The Shadows of Tomorrow")})): 3,
        Itemset(frozenset({Item("Echoes of a Forgotten Realm")})): 3,
        Itemset(frozenset({Item("Whispers of the Ancient World")})): 3,
        Itemset(frozenset({Item("Chronicles of the Unseen")})): 3,
        Itemset(frozenset({Item("Legends of the Fallen Skies")})): 3,
        Itemset(frozenset({Item("Tales of the Crimson Dawn")})): 3,
        Itemset(frozenset({Item("Secrets of the Silent Ocean")})): 3,
        Itemset(frozenset({Item("Memories of the Last Horizon")})): 3,
        Itemset(frozenset({Item("Dreams of the Distant Stars")})): 3,
        Itemset(frozenset({Item("Visions of the Lost Empire")})): 3,
        Itemset(frozenset({Item("Tales of the Ancient World")})): 0,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."


def test_with_large_book_dataset_and_a_some_2_itemsets(
    large_book_dataset,
):
    """Test the counting of occurrences of 2-itemsets with the large book dataset. The list of 2-itemsets is not complete (just 6 random combinations)."""

    # Create the Apriori object
    apriori = Apriori()

    # List of 2-itemsets
    two_itemsets = set()
    two_itemsets.add(
        Itemset(
            frozenset(
                {Item("The Shadows of Tomorrow"), Item("Echoes of a Forgotten Realm")}
            )
        )
    )
    two_itemsets.add(
        Itemset(
            frozenset(
                {Item("The Shadows of Tomorrow"), Item("Whispers of the Ancient World")}
            )
        )
    )
    two_itemsets.add(
        Itemset(
            frozenset(
                {Item("The Shadows of Tomorrow"), Item("Chronicles of the Unseen")}
            )
        )
    )
    two_itemsets.add(
        Itemset(
            frozenset(
                {
                    Item("Echoes of a Forgotten Realm"),
                    Item("Whispers of the Ancient World"),
                }
            )
        )
    )
    two_itemsets.add(
        Itemset(
            frozenset(
                {Item("Echoes of a Forgotten Realm"), Item("Chronicles of the Unseen")}
            )
        )
    )
    two_itemsets.add(
        Itemset(
            frozenset(
                {
                    Item("Whispers of the Ancient World"),
                    Item("Chronicles of the Unseen"),
                }
            )
        )
    )

    # Count the occurrences of the 2-itemsets
    itemsets_with_occurence_counts = apriori._count_occurences_of_itemsets(
        large_book_dataset, two_itemsets
    )

    # Check the occurrence counts
    expected_occurrences = {
        Itemset(
            frozenset(
                {Item("The Shadows of Tomorrow"), Item("Echoes of a Forgotten Realm")}
            )
        ): 1,
        Itemset(
            frozenset(
                {Item("The Shadows of Tomorrow"), Item("Whispers of the Ancient World")}
            )
        ): 1,
        Itemset(
            frozenset(
                {Item("The Shadows of Tomorrow"), Item("Chronicles of the Unseen")}
            )
        ): 0,
        Itemset(
            frozenset(
                {
                    Item("Echoes of a Forgotten Realm"),
                    Item("Whispers of the Ancient World"),
                }
            )
        ): 1,
        Itemset(
            frozenset(
                {Item("Echoes of a Forgotten Realm"), Item("Chronicles of the Unseen")}
            )
        ): 1,
        Itemset(
            frozenset(
                {
                    Item("Whispers of the Ancient World"),
                    Item("Chronicles of the Unseen"),
                }
            )
        ): 1,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            itemsets_with_occurence_counts.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Itemset: ({item_names}), Expected: {expected_occurrences[itemset]}, Actual: {itemsets_with_occurence_counts.get_occurrence_count(itemset)}."

    # Check that itemsets_with_occurence_counts does not contain any other itemsets
    extra_itemsets = itemsets_with_occurence_counts.keys() - expected_occurrences.keys()
    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets}."
