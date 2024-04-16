from apriori import Apriori

from classes.item import Item
from classes.itemset import Itemset

#####
# Test with the small fruit dataset
#####


def test_with_small_fruit_dataset_and_min_support_of_one(small_fruit_dataset):
    """Test the generation of frequent itemsets with the small fruit dataset and a minimum support of 1."""

    # Create the Apriori object
    apriori = Apriori(min_support=1)

    # Generate the frequent itemsets
    apriori.fit(small_fruit_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    expected_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Banana")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Cherry"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Banana"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry"), Item("Dragonfruit")})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_small_fruit_dataset_and_min_support_of_two(small_fruit_dataset):
    """Test the generation of frequent itemsets with the small fruit dataset and a minimum support of 2."""

    # Create the Apriori object
    apriori = Apriori(min_support=2)

    # Generate the frequent itemsets
    apriori.fit(small_fruit_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    expected_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Dragonfruit")})),
        Itemset(frozenset({Item("Banana"), Item("Cherry")})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_small_fruit_dataset_and_min_support_of_three(small_fruit_dataset):
    """Test the generation of frequent itemsets with the small fruit dataset and a minimum support of 3."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

    # Generate the frequent itemsets
    apriori.fit(small_fruit_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    expected_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Apple"), Item("Cherry")})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_small_fruit_dataset_and_min_support_of_four(small_fruit_dataset):
    """Test the generation of frequent itemsets with the small fruit dataset and a minimum support of 4."""

    # Create the Apriori object
    apriori = Apriori(min_support=4)

    # Generate the frequent itemsets
    apriori.fit(small_fruit_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    expected_itemsets = {
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Cherry")})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

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
# Test with the large book dataset
#####


def test_with_large_book_dataset_and_min_support_of_one(large_book_dataset):
    """Test the generation of frequent itemsets with the large book dataset and a minimum support of 1."""

    # Create the Apriori object
    apriori = Apriori(min_support=1)

    # Generate the frequent itemsets
    apriori.fit(large_book_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    items = [
        Item("The Shadows of Tomorrow"),
        Item("Echoes of a Forgotten Realm"),
        Item("Whispers of the Ancient World"),
        Item("Chronicles of the Unseen"),
        Item("Legends of the Fallen Skies"),
        Item("Tales of the Crimson Dawn"),
        Item("Secrets of the Silent Ocean"),
        Item("Memories of the Last Horizon"),
        Item("Dreams of the Distant Stars"),
        Item("Visions of the Lost Empire"),
    ]
    expected_itemsets = {
        Itemset(frozenset({items[0]})),
        Itemset(frozenset({items[1]})),
        Itemset(frozenset({items[2]})),
        Itemset(frozenset({items[3]})),
        Itemset(frozenset({items[4]})),
        Itemset(frozenset({items[5]})),
        Itemset(frozenset({items[6]})),
        Itemset(frozenset({items[7]})),
        Itemset(frozenset({items[8]})),
        Itemset(frozenset({items[9]})),
        Itemset(frozenset({items[0], items[1]})),
        Itemset(frozenset({items[0], items[2]})),
        Itemset(frozenset({items[0], items[4]})),
        Itemset(frozenset({items[0], items[5]})),
        Itemset(frozenset({items[0], items[7]})),
        Itemset(frozenset({items[0], items[9]})),
        Itemset(frozenset({items[1], items[2]})),
        Itemset(frozenset({items[1], items[3]})),
        Itemset(frozenset({items[1], items[4]})),
        Itemset(frozenset({items[1], items[8]})),
        Itemset(frozenset({items[1], items[9]})),
        Itemset(frozenset({items[2], items[3]})),
        Itemset(frozenset({items[2], items[4]})),
        Itemset(frozenset({items[2], items[5]})),
        Itemset(frozenset({items[2], items[6]})),
        Itemset(frozenset({items[3], items[4]})),
        Itemset(frozenset({items[3], items[7]})),
        Itemset(frozenset({items[3], items[8]})),
        Itemset(frozenset({items[4], items[9]})),
        Itemset(frozenset({items[5], items[6]})),
        Itemset(frozenset({items[5], items[7]})),
        Itemset(frozenset({items[6], items[7]})),
        Itemset(frozenset({items[6], items[8]})),
        Itemset(frozenset({items[6], items[9]})),
        Itemset(frozenset({items[7], items[8]})),
        Itemset(frozenset({items[8], items[9]})),
        Itemset(frozenset({items[0], items[1], items[2]})),
        Itemset(frozenset({items[1], items[3], items[4]})),
        Itemset(frozenset({items[2], items[5], items[6]})),
        Itemset(frozenset({items[3], items[7], items[8]})),
        Itemset(frozenset({items[0], items[4], items[9]})),
        Itemset(frozenset({items[5], items[6], items[7]})),
        Itemset(frozenset({items[8], items[9], items[1]})),
        Itemset(frozenset({items[2], items[3], items[4]})),
        Itemset(frozenset({items[5], items[7], items[0]})),
        Itemset(frozenset({items[6], items[8], items[9]})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_large_book_dataset_and_min_support_of_two(large_book_dataset):
    """Test the generation of frequent itemsets with the large book dataset and a minimum support of 2."""

    # Create the Apriori object
    apriori = Apriori(min_support=2)

    # Generate the frequent itemsets
    apriori.fit(large_book_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    items = [
        Item("The Shadows of Tomorrow"),
        Item("Echoes of a Forgotten Realm"),
        Item("Whispers of the Ancient World"),
        Item("Chronicles of the Unseen"),
        Item("Legends of the Fallen Skies"),
        Item("Tales of the Crimson Dawn"),
        Item("Secrets of the Silent Ocean"),
        Item("Memories of the Last Horizon"),
        Item("Dreams of the Distant Stars"),
        Item("Visions of the Lost Empire"),
    ]
    expected_itemsets = {
        Itemset(frozenset({items[0]})),
        Itemset(frozenset({items[1]})),
        Itemset(frozenset({items[2]})),
        Itemset(frozenset({items[3]})),
        Itemset(frozenset({items[4]})),
        Itemset(frozenset({items[5]})),
        Itemset(frozenset({items[6]})),
        Itemset(frozenset({items[7]})),
        Itemset(frozenset({items[8]})),
        Itemset(frozenset({items[9]})),
        Itemset(frozenset({items[3], items[4]})),
        Itemset(frozenset({items[5], items[6]})),
        Itemset(frozenset({items[5], items[7]})),
        Itemset(frozenset({items[8], items[9]})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."


def test_with_large_book_dataset_and_min_support_of_three(large_book_dataset):
    """Test the generation of frequent itemsets with the large book dataset and a minimum support of 3."""

    # Create the Apriori object
    apriori = Apriori(min_support=3)

    # Generate the frequent itemsets
    apriori.fit(large_book_dataset)

    # Create sets of expected and generated itemsets for easier comparison
    items = [
        Item("The Shadows of Tomorrow"),
        Item("Echoes of a Forgotten Realm"),
        Item("Whispers of the Ancient World"),
        Item("Chronicles of the Unseen"),
        Item("Legends of the Fallen Skies"),
        Item("Tales of the Crimson Dawn"),
        Item("Secrets of the Silent Ocean"),
        Item("Memories of the Last Horizon"),
        Item("Dreams of the Distant Stars"),
        Item("Visions of the Lost Empire"),
    ]
    expected_itemsets = {
        Itemset(frozenset({items[0]})),
        Itemset(frozenset({items[1]})),
        Itemset(frozenset({items[2]})),
        Itemset(frozenset({items[3]})),
        Itemset(frozenset({items[4]})),
        Itemset(frozenset({items[5]})),
        Itemset(frozenset({items[6]})),
        Itemset(frozenset({items[7]})),
        Itemset(frozenset({items[8]})),
        Itemset(frozenset({items[9]})),
    }
    generated_itemsets = apriori.frequent_itemsets

    # Check the itemsets
    missing_itemsets = expected_itemsets - generated_itemsets
    extra_itemsets = generated_itemsets - expected_itemsets

    # Make the missing itemsets and extra itemsets easier printable
    missing_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in missing_itemsets
    )

    extra_itemsets_text = ", ".join(
        f"({', '.join(item.name for item in itemset)})" for itemset in extra_itemsets
    )

    assert not extra_itemsets, f"Extra itemsets: {extra_itemsets_text}."
    assert not missing_itemsets, f"Missing itemsets: {missing_itemsets_text}."
