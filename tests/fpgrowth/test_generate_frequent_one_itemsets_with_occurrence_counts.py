from fpgrowth import FPgrowth

from classes.item import Item
from classes.itemset import Itemset


#####
# Test with the small fruit dataset
#####


def test_with_small_fruit_dataset_and_min_support_of_one(small_fruit_dataset):
    """Test the generation of frequent 1-itemsets with the small fruit dataset and a minimum support of 1."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=1)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            small_fruit_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {"Apple", "Banana", "Cherry", "Dragonfruit"}
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
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
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."


def test_with_small_fruit_dataset_and_min_support_of_two(small_fruit_dataset):
    """Test the generation of frequent 1-itemsets with the small fruit dataset and a minimum support of 2."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=2)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            small_fruit_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {"Apple", "Banana", "Cherry", "Dragonfruit"}
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
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
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."


def test_with_small_fruit_dataset_and_min_support_of_three(small_fruit_dataset):
    """Test the generation of frequent 1-itemsets with the small fruit dataset and a minimum support of 3."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=3)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            small_fruit_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {"Apple", "Cherry"}
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
    expected_occurrences = {
        Itemset(frozenset({Item("Apple")})): 4,
        Itemset(frozenset({Item("Cherry")})): 4,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."


def test_with_small_fruit_dataset_and_min_support_of_four(small_fruit_dataset):
    """Test the generation of frequent 1-itemsets with the small fruit dataset and a minimum support of 4."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=4)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            small_fruit_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {"Apple", "Cherry"}
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
    expected_occurrences = {
        Itemset(frozenset({Item("Apple")})): 4,
        Itemset(frozenset({Item("Cherry")})): 4,
    }

    for itemset in expected_occurrences:
        # For better error messages
        item_names = ", ".join(item.name for item in itemset)

        # Check the occurrence count of the current itemset
        assert (
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."


#####
# Test with the large book dataset
#####


def test_with_large_book_dataset_and_min_support_of_one(large_book_dataset):
    """Test the generation of frequent 1-itemsets with the large book dataset and a minimum support of 1."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=1)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            large_book_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {
        "The Shadows of Tomorrow",
        "Echoes of a Forgotten Realm",
        "Whispers of the Ancient World",
        "Chronicles of the Unseen",
        "Legends of the Fallen Skies",
        "Tales of the Crimson Dawn",
        "Secrets of the Silent Ocean",
        "Memories of the Last Horizon",
        "Dreams of the Distant Stars",
        "Visions of the Lost Empire",
    }
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
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
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."


def test_with_large_book_dataset_and_min_support_of_three(large_book_dataset):
    """Test the generation of frequent 1-itemsets with the large book dataset and a minimum support of 3."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=2)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            large_book_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {
        "The Shadows of Tomorrow",
        "Echoes of a Forgotten Realm",
        "Whispers of the Ancient World",
        "Chronicles of the Unseen",
        "Legends of the Fallen Skies",
        "Tales of the Crimson Dawn",
        "Secrets of the Silent Ocean",
        "Memories of the Last Horizon",
        "Dreams of the Distant Stars",
        "Visions of the Lost Empire",
    }
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
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
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."


def test_with_large_book_dataset_and_min_support_of_one(large_book_dataset):
    """Test the generation of frequent 1-itemsets with the large book dataset and a minimum support of 1."""

    # Create the FPgrowth object
    fpgrowth = FPgrowth(min_support=1)

    # Generate the frequent 1-itemsets
    frequent_one_itemsets = (
        fpgrowth._generate_frequent_one_itemsets_with_occurrence_counts(
            large_book_dataset
        )
    )

    # Check the itemsets (without occurrence counts)
    # Create sets of expected and generated item names for easier comparison
    expected_items = {
        "The Shadows of Tomorrow",
        "Echoes of a Forgotten Realm",
        "Whispers of the Ancient World",
        "Chronicles of the Unseen",
        "Legends of the Fallen Skies",
        "Tales of the Crimson Dawn",
        "Secrets of the Silent Ocean",
        "Memories of the Last Horizon",
        "Dreams of the Distant Stars",
        "Visions of the Lost Empire",
    }
    generated_items = {
        item.name for itemset in frequent_one_itemsets.keys() for item in itemset
    }

    # Compare the expected and generated 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra itemsets: {extra_items}."
    assert not missing_items, f"Missing itemsets: {missing_items}."

    # Check the occurrence counts of the itemsets
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
            frequent_one_itemsets.get_occurrence_count(itemset)
            == expected_occurrences[itemset]
        ), f"Wrong occurrence Count for Itemset: {item_names}, Expected: {expected_occurrences[itemset]}, Returned: {frequent_one_itemsets.get_occurrence_count(itemset)}."
