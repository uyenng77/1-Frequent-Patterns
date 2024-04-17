from fpgrowth import FPgrowth

from classes.item import Item
from classes.itemset import Itemset
from classes.item_tuple import ItemTuple
from classes.sorted_transaction import SortedTransaction
from classes.sorted_dataset import SortedDataset

#####
# Test with the small fruit dataset
#####


def test_with_small_fruit_dataset_and_correct_f_list_for_min_support_of_two(
    small_fruit_dataset,
):
    """Test the dataset sorting with the small fruit dataset and a correct f-list for a minimum support of 2."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Put together the f-list
    f_list = [
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Banana")})),
        Itemset(frozenset({Item("Dragonfruit")})),
    ]

    # Sort the Dataset according to the f-list
    sorted_dataset = fpgrowth._sort_dataset_according_to_f_list(
        small_fruit_dataset, f_list
    )

    # Put together the expected sorted dataset
    expected_sorted_dataset = SortedDataset(
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

    # Compare the sorted dataset with the expected sorted dataset transaction by transaction
    for expected_sorted_transaction in expected_sorted_dataset.transactions:
        # For better error messages
        expected_sorted_transaction_text = ", ".join(
            item.name for item in expected_sorted_transaction.items.items
        )

        # Boolean to check if the transaction was found in the sorted dataset
        transaction_found = False

        # Check if there is a transaction with the same id in the returned dataset
        for sorted_transaction in sorted_dataset.transactions:
            # For better error messages
            sorted_transaction_text = ", ".join(
                item.name for item in sorted_transaction.items.items
            )

            if sorted_transaction.id == expected_sorted_transaction.id:
                # Check if the items are the same
                assert (
                    sorted_transaction.items == expected_sorted_transaction.items
                ), f'Returned transaction with id {sorted_transaction.id} and sorted items "{sorted_transaction_text}" should contain the sorted items  "{expected_sorted_transaction_text}".'

                # Set the flag to True
                transaction_found = True

        assert (
            transaction_found
        ), f"Transaction with id {expected_sorted_transaction.id} was not found in the returned dataset."


def test_with_small_fruit_dataset_and_correct_f_list_for_min_support_of_three(
    small_fruit_dataset,
):
    """Test the dataset sorting with the small fruit dataset and a correct f-list for a minimum support of 3."""

    # Initialize the FP-growth algorithm with a minimum support of 3
    fpgrowth = FPgrowth(min_support=3)

    # Put together the f-list
    f_list = [
        Itemset(frozenset({Item("Cherry")})),
        Itemset(frozenset({Item("Apple")})),
    ]

    # Sort the Dataset according to the f-list
    sorted_dataset = fpgrowth._sort_dataset_according_to_f_list(
        small_fruit_dataset, f_list
    )

    # Put together the expected sorted dataset
    expected_sorted_dataset = SortedDataset(
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

    # Compare the sorted dataset with the expected sorted dataset transaction by transaction
    for expected_sorted_transaction in expected_sorted_dataset.transactions:
        # For better error messages
        expected_sorted_transaction_text = ", ".join(
            item.name for item in expected_sorted_transaction.items.items
        )

        # Boolean to check if the transaction was found in the sorted dataset
        transaction_found = False

        # Check if there is a transaction with the same id in the returned dataset
        for sorted_transaction in sorted_dataset.transactions:
            # For better error messages
            sorted_transaction_text = ", ".join(
                item.name for item in sorted_transaction.items.items
            )

            if sorted_transaction.id == expected_sorted_transaction.id:
                # Check if the items are the same
                assert (
                    sorted_transaction.items == expected_sorted_transaction.items
                ), f'Returned transaction with id {sorted_transaction.id} and sorted items "{sorted_transaction_text}" should contain the sorted items  "{expected_sorted_transaction_text}".'

                # Set the flag to True
                transaction_found = True

        assert (
            transaction_found
        ), f"Transaction with id {expected_sorted_transaction.id} was not found in the returned dataset."


def test_with_small_fruit_dataset_and_incorrect_f_list_apple_dragonfruit_cherry(
    small_fruit_dataset,
):
    """Test the dataset sorting with the small fruit dataset and an incorrect f-list with the order Apple, Dragonfruit, Cherry."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Put together the f-list
    f_list = [
        Itemset(frozenset({Item("Apple")})),
        Itemset(frozenset({Item("Dragonfruit")})),
        Itemset(frozenset({Item("Cherry")})),
    ]

    # Sort the Dataset according to the f-list
    sorted_dataset = fpgrowth._sort_dataset_according_to_f_list(
        small_fruit_dataset, f_list
    )

    # Put together the expected sorted dataset
    expected_sorted_dataset = SortedDataset(
        frozenset(
            {
                SortedTransaction(1, ItemTuple(tuple([Item("Apple"), Item("Cherry")]))),
                SortedTransaction(2, ItemTuple(tuple([Item("Cherry")]))),
                SortedTransaction(3, ItemTuple(tuple([Item("Apple"), Item("Cherry")]))),
                SortedTransaction(
                    4,
                    ItemTuple(
                        tuple([Item("Apple"), Item("Dragonfruit"), Item("Cherry")])
                    ),
                ),
                SortedTransaction(
                    5, ItemTuple(tuple([Item("Apple"), Item("Dragonfruit")]))
                ),
            }
        )
    )

    # Compare the sorted dataset with the expected sorted dataset transaction by transaction
    for expected_sorted_transaction in expected_sorted_dataset.transactions:
        # For better error messages
        expected_sorted_transaction_text = ", ".join(
            item.name for item in expected_sorted_transaction.items.items
        )

        # Boolean to check if the transaction was found in the sorted dataset
        transaction_found = False

        # Check if there is a transaction with the same id in the returned dataset
        for sorted_transaction in sorted_dataset.transactions:
            # For better error messages
            sorted_transaction_text = ", ".join(
                item.name for item in sorted_transaction.items.items
            )

            if sorted_transaction.id == expected_sorted_transaction.id:
                # Check if the items are the same
                assert (
                    sorted_transaction.items == expected_sorted_transaction.items
                ), f'Returned transaction with id {sorted_transaction.id} and sorted items "{sorted_transaction_text}" should contain the sorted items  "{expected_sorted_transaction_text}".'

                # Set the flag to True
                transaction_found = True

        assert (
            transaction_found
        ), f"Transaction with id {expected_sorted_transaction.id} was not found in the returned dataset."


#####
# Test with the large book dataset
#####


def test_with_large_book_dataset_and_correct_f_list_for_min_support_of_two(
    large_book_dataset,
):
    """Test the dataset sorting with the large book dataset and a correct f-list for a minimum support of 2."""

    # Initialize the FP-growth algorithm with a minimum support of 2
    fpgrowth = FPgrowth(min_support=2)

    # Put together the f-list
    f_list = [
        Itemset(frozenset({Item("The Shadows of Tomorrow")})),
        Itemset(frozenset({Item("Echoes of a Forgotten Realm")})),
        Itemset(frozenset({Item("Whispers of the Ancient World")})),
        Itemset(frozenset({Item("Chronicles of the Unseen")})),
        Itemset(frozenset({Item("Legends of the Fallen Skies")})),
        Itemset(frozenset({Item("Tales of the Crimson Dawn")})),
        Itemset(frozenset({Item("Memories of the Last Horizon")})),
        Itemset(frozenset({Item("Secrets of the Silent Ocean")})),
        Itemset(frozenset({Item("Dreams of the Distant Stars")})),
        Itemset(frozenset({Item("Visions of the Lost Empire")})),
    ]

    # Sort the Dataset according to the f-list
    sorted_dataset = fpgrowth._sort_dataset_according_to_f_list(
        large_book_dataset, f_list
    )

    # Put together the expected sorted dataset
    expected_sorted_dataset = SortedDataset(
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

    # Compare the sorted dataset with the expected sorted dataset transaction by transaction
    for expected_sorted_transaction in expected_sorted_dataset.transactions:
        # For better error messages
        expected_sorted_transaction_text = ", ".join(
            item.name for item in expected_sorted_transaction.items.items
        )

        # Boolean to check if the transaction was found in the sorted dataset
        transaction_found = False

        # Check if there is a transaction with the same id in the returned dataset
        for sorted_transaction in sorted_dataset.transactions:
            # For better error messages
            sorted_transaction_text = ", ".join(
                item.name for item in sorted_transaction.items.items
            )

            if sorted_transaction.id == expected_sorted_transaction.id:
                # Check if the items are the same
                assert (
                    sorted_transaction.items == expected_sorted_transaction.items
                ), f'Returned transaction with id {sorted_transaction.id} and sorted items "{sorted_transaction_text}" should contain the sorted items  "{expected_sorted_transaction_text}".'

                # Set the flag to True
                transaction_found = True

        assert (
            transaction_found
        ), f"Transaction with id {expected_sorted_transaction.id} was not found in the returned dataset."
