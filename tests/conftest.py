import pytest

from classes.item import Item
from classes.itemset import Itemset
from classes.transaction import Transaction
from classes.dataset import Dataset


@pytest.fixture
def small_fruit_dataset():
    """Create a small dataset with fruits."""

    # Create some items
    item1 = Item("Apple")
    item2 = Item("Banana")
    item3 = Item("Cherry")
    item4 = Item("Dragonfruit")

    # Create some transactions
    transaction1 = Transaction(1, Itemset(frozenset({item1, item2, item3})))
    transaction2 = Transaction(2, Itemset(frozenset({item2, item3})))
    transaction3 = Transaction(3, Itemset(frozenset({item3, item1})))
    transaction4 = Transaction(4, Itemset(frozenset({item4, item1, item3})))
    transaction5 = Transaction(5, Itemset(frozenset({item1, item4})))

    # Create the dataset and return it
    return Dataset(
        {
            transaction1,
            transaction2,
            transaction3,
            transaction4,
            transaction5,
        }
    )


@pytest.fixture
def large_book_dataset():
    """Create a large(r) dataset with books."""

    # Create some items (books)
    books = [
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

    # Create transactions (sets of books)
    transactions = [
        Transaction(1, Itemset(frozenset({books[0], books[1], books[2]}))),
        Transaction(2, Itemset(frozenset({books[1], books[3], books[4]}))),
        Transaction(3, Itemset(frozenset({books[2], books[5], books[6]}))),
        Transaction(4, Itemset(frozenset({books[3], books[7], books[8]}))),
        Transaction(5, Itemset(frozenset({books[0], books[4], books[9]}))),
        Transaction(6, Itemset(frozenset({books[5], books[6], books[7]}))),
        Transaction(7, Itemset(frozenset({books[8], books[9], books[1]}))),
        Transaction(8, Itemset(frozenset({books[2], books[3], books[4]}))),
        Transaction(9, Itemset(frozenset({books[5], books[7], books[0]}))),
        Transaction(10, Itemset(frozenset({books[6], books[8], books[9]}))),
    ]

    return Dataset(set(transactions))
