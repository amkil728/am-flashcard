from flashcard import *

def test_write(deck, handle, s):
    """
    Write a test deck of cards to a file, then read the contents of the file
    as a deck, and check that both decks are equal.
    """

    print("Testing deck write")

    write_deck(deck, handle)

    try:
        with open(handle) as file:
            file_text = file.read()
            assert file_text == s
    except AssertionError:
        print("Expected:")
        print(s)
        print("Received:") 
        print(file_text)


def test_read(handle, deck):
    print("Testing deck read")

    deck_read = read_deck(handle)

    try:
        assert deck_read == deck
    except AssertionError:
        print("expected:")
        for k, v in deck:
            print(k, v)
        print("received:")
        for k, v in deck_read:
            print(k, v)
    

if __name__ == '__main__':
    test_deck = [
        make_card("école", "school"),
        make_card("jeune", "young"),
        make_card("vieux", "old")
    ]

    test_str = """école
school
jeune
young
vieux
old
"""

    HANDLE = 'test_file'

    test_write(test_deck, HANDLE, test_str)
    test_read(HANDLE, test_deck)