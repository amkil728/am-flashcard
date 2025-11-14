# flashcard.py

from sys import argv

# a flashcard is a dict with entries
# 'front' for the front; 'back' for the back of the card

def make_card(front, back):
    """
    Creates a flashcard with given front and back entries.
    """
    return {'front': front, 'back': back}


# A deck is represented as a list of flashcards

def deck_contains(deck, front):
    """
    Checks if the deck contains a card with the given front text.
    """
    return front in [k['front'] for k in deck]
    

def add_card(deck, card):
    """
    Adds a card to a deck. Raises an error if the front of the card is already
    in the deck.
    """

    if deck_contains(deck, card['front']):
        raise ValueError(f"Card with front {card['front']} already in deck")
    else:
        deck.append(card)


def write_deck(deck, handle):
    """
    Writes a deck to the file with the given handle.
    """
    with open(handle, 'w') as file:
        for card in deck:
            file.write(card['front'] + '\n')
            file.write(card['back'] + '\n')


def read_deck(handle):
    """
    Reads the contents of the file with given handle as a deck.
    """
    deck = []

    with open(handle) as file:
        for index, line in enumerate(file.readlines()):
            if index % 2 == 0:
                front = line.strip()
            else:
                back = line.strip()
                deck.append(make_card(front, back))

    return deck