from apriori import Apriori


#####
# Test with the small fruit dataset
#####


def test_with_small_fruit_dataset(small_fruit_dataset):
    """Test the generation of 1-itemsets with the small fruit dataset."""

    # Create the Apriori object
    apriori = Apriori()

    # Generate the 1-itemsets
    one_itemsets = apriori._generate_one_itemsets(small_fruit_dataset)

    # Create sets of expected and generated item names for easier comparison
    expected_items = {"Apple", "Banana", "Cherry", "Dragonfruit"}
    generated_items = {item.name for itemset in one_itemsets for item in itemset}

    # Check the content of the 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra items: {extra_items}."
    assert not missing_items, f"Missing items: {missing_items}."


#####
# Test with the large book dataset
#####


def test_with_large_book_dataset(large_book_dataset):
    """Test the generation of 1-itemsets with the large book dataset."""

    # Create the Apriori object
    apriori = Apriori()

    # Generate the 1-itemsets
    one_itemsets = apriori._generate_one_itemsets(large_book_dataset)

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
    generated_items = {item.name for itemset in one_itemsets for item in itemset}

    # Check the content of the 1-itemsets
    missing_items = expected_items - generated_items
    extra_items = generated_items - expected_items

    assert not extra_items, f"Extra items: {extra_items}."

    assert not missing_items, f"Missing items: {missing_items}."
