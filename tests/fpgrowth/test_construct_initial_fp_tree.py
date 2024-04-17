from fpgrowth import FPgrowth

from classes.sorted_dataset import SortedDataset
from classes.sorted_transaction import SortedTransaction
from classes.item import Item
from classes.item_tuple import ItemTuple
from classes.fp_tree import FPTree

#####
# Test with the small fruit dataset
#####


def test_with_small_fruit_dataset_and_min_support_of_two(small_fruit_dataset):
    """Test the creation of the initial FP-tree with the small fruit dataset and a minimum support of 2."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Sorted dataset
    sorted_dataset = SortedDataset(
        frozenset(
            {
                SortedTransaction(
                    1, ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
                ),
                SortedTransaction(
                    2, ItemTuple(tuple([Item("Cherry"), Item("Banana")]))
                ),
                SortedTransaction(3, ItemTuple(tuple([Item("Apple"), Item("Cherry")]))),
                SortedTransaction(
                    4,
                    ItemTuple(
                        tuple([Item("Apple"), Item("Cherry"), Item("Dragonfruit")])
                    ),
                ),
                SortedTransaction(
                    5, ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")]))
                ),
            }
        )
    )

    # Construct the initial FP-tree
    fp_tree = fpgrowth._construct_initial_fp_tree(sorted_dataset)

    # Construct the expected FP-tree
    expected_fp_tree = FPTree()
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Banana")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Cherry"), Item("Banana")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Cherry"), Item("Dragonfruit")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")]))
    )

    # Check the FP-tree
    assert (
        fp_tree == expected_fp_tree
    ), f"The returned FP-tree is not as expected.\n Returned FP-tree:\n {fp_tree} \n\n Expected FP-tree:\n {expected_fp_tree}."


def test_with_small_fruit_dataset_and_min_support_of_three(small_fruit_dataset):
    """Test the creation of the initial FP-tree with the small fruit dataset and a minimum support of 3."""

    # Initialize the FP-growth algorithm with a minimum support of 3
    fpgrowth = FPgrowth(min_support=3)

    # Sorted dataset
    sorted_dataset = SortedDataset(
        frozenset(
            {
                SortedTransaction(1, ItemTuple(tuple([Item("Cherry"), Item("Apple")]))),
                SortedTransaction(
                    2,
                    ItemTuple(
                        tuple(
                            [
                                Item("Cherry"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(3, ItemTuple(tuple([Item("Cherry"), Item("Apple")]))),
                SortedTransaction(
                    4,
                    ItemTuple(tuple([Item("Cherry"), Item("Apple")])),
                ),
                SortedTransaction(5, ItemTuple(tuple([Item("Apple")]))),
            }
        )
    )

    # Construct the initial FP-tree
    fp_tree = fpgrowth._construct_initial_fp_tree(sorted_dataset)

    # Construct the expected FP-tree
    expected_fp_tree = FPTree()
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Cherry"), Item("Apple")]))
    )
    expected_fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Cherry")])))
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Cherry"), Item("Apple")]))
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(tuple([Item("Cherry"), Item("Apple")]))
    )
    expected_fp_tree.add_items_to_tree(ItemTuple(tuple([Item("Apple")])))

    # Check the FP-tree
    assert (
        fp_tree == expected_fp_tree
    ), f"The returned FP-tree is not as expected.\n Returned FP-tree:\n {fp_tree} \n\n Expected FP-tree:\n {expected_fp_tree}."


#####
# Test with the large book dataset
#####


def test_with_large_book_dataset_and_min_support_of_two(large_book_dataset):
    """Test the creation of the initial FP-tree with the large book dataset and a minimum support of 2."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Sorted dataset
    sorted_dataset = SortedDataset(
        frozenset(
            {
                SortedTransaction(
                    1,
                    ItemTuple(
                        tuple(
                            [
                                Item("The Shadows of Tomorrow"),
                                Item("Echoes of a Forgotten Realm"),
                                Item("Whispers of the Ancient World"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    2,
                    ItemTuple(
                        tuple(
                            [
                                Item("Echoes of a Forgotten Realm"),
                                Item("Chronicles of the Unseen"),
                                Item("Legends of the Fallen Skies"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    3,
                    ItemTuple(
                        tuple(
                            [
                                Item("Whispers of the Ancient World"),
                                Item("Tales of the Crimson Dawn"),
                                Item("Secrets of the Silent Ocean"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    4,
                    ItemTuple(
                        tuple(
                            [
                                Item("Chronicles of the Unseen"),
                                Item("Memories of the Last Horizon"),
                                Item("Dreams of the Distant Stars"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    5,
                    ItemTuple(
                        tuple(
                            [
                                Item("The Shadows of Tomorrow"),
                                Item("Legends of the Fallen Skies"),
                                Item("Visions of the Lost Empire"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    6,
                    ItemTuple(
                        tuple(
                            [
                                Item("Tales of the Crimson Dawn"),
                                Item("Memories of the Last Horizon"),
                                Item("Secrets of the Silent Ocean"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    7,
                    ItemTuple(
                        tuple(
                            [
                                Item("Echoes of a Forgotten Realm"),
                                Item("Dreams of the Distant Stars"),
                                Item("Visions of the Lost Empire"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    8,
                    ItemTuple(
                        tuple(
                            [
                                Item("Whispers of the Ancient World"),
                                Item("Chronicles of the Unseen"),
                                Item("Legends of the Fallen Skies"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    9,
                    ItemTuple(
                        tuple(
                            [
                                Item("The Shadows of Tomorrow"),
                                Item("Tales of the Crimson Dawn"),
                                Item("Memories of the Last Horizon"),
                            ]
                        )
                    ),
                ),
                SortedTransaction(
                    10,
                    ItemTuple(
                        tuple(
                            [
                                Item("Secrets of the Silent Ocean"),
                                Item("Dreams of the Distant Stars"),
                                Item("Visions of the Lost Empire"),
                            ]
                        )
                    ),
                ),
            }
        )
    )

    # Construct the initial FP-tree
    fp_tree = fpgrowth._construct_initial_fp_tree(sorted_dataset)

    # Construct the expected FP-tree
    expected_fp_tree = FPTree()
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("The Shadows of Tomorrow"),
                    Item("Echoes of a Forgotten Realm"),
                    Item("Whispers of the Ancient World"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Echoes of a Forgotten Realm"),
                    Item("Chronicles of the Unseen"),
                    Item("Legends of the Fallen Skies"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Whispers of the Ancient World"),
                    Item("Tales of the Crimson Dawn"),
                    Item("Secrets of the Silent Ocean"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Chronicles of the Unseen"),
                    Item("Memories of the Last Horizon"),
                    Item("Dreams of the Distant Stars"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("The Shadows of Tomorrow"),
                    Item("Legends of the Fallen Skies"),
                    Item("Visions of the Lost Empire"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Tales of the Crimson Dawn"),
                    Item("Memories of the Last Horizon"),
                    Item("Secrets of the Silent Ocean"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Echoes of a Forgotten Realm"),
                    Item("Dreams of the Distant Stars"),
                    Item("Visions of the Lost Empire"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Whispers of the Ancient World"),
                    Item("Chronicles of the Unseen"),
                    Item("Legends of the Fallen Skies"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("The Shadows of Tomorrow"),
                    Item("Tales of the Crimson Dawn"),
                    Item("Memories of the Last Horizon"),
                ]
            )
        )
    )
    expected_fp_tree.add_items_to_tree(
        ItemTuple(
            tuple(
                [
                    Item("Secrets of the Silent Ocean"),
                    Item("Dreams of the Distant Stars"),
                    Item("Visions of the Lost Empire"),
                ]
            )
        )
    )

    # Check the FP-tree
    assert (
        fp_tree == expected_fp_tree
    ), f"The returned FP-tree is not as expected.\n Returned FP-tree:\n {fp_tree} \n\n Expected FP-tree:\n {expected_fp_tree}."
