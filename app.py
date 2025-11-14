from flashcard import add_card, deck_contains, make_card, write_deck, read_deck
import sys

# main loop:
# Given a deck, print each card, in order
# Count the number of correct answers
# Ask if the user wants to try again

response_map = {
    'e':'easy',
    'd':'difficult',
    'w':'wrong'
}

def review_deck(deck):
    response_counts = {k:0 for k in response_map.keys()}

    while True:
        for card in deck:
            print(card['front'])
            input('Reveal')
            print(card['back'])
            print('Enter e for easy, d for difficult, anything else for wrong')
            response = input()
            if response in response_counts:
                response_counts[response] += 1
            else:
                response_counts['w'] += 1

        for response in response_map:
            print(response_map[response], response_counts[response])

        again = input("Continue: ")
        if again != 'y':
            break


def add_cards(deck):
    while True:
        front = input('Front: ')
        back = input('Back: ')
        add_card(deck, make_card(front, back))
        resp = input("Continue: ")
        if resp != 'y':
            break


def show_deck(deck):
    for card in deck:
        print(f"{card['front']}: {card['back']}")


def edit_deck(deck, handle):
    """
    Show all cards, prompt user to identify card to edit with front of card.
    """

    show_deck(deck)

    while True:
        front = input("Enter the front of the card to be edited: ")

        # find card with front and its index
        for index, card in enumerate(deck):
            if card['front'] == front:
                break
        else:
            print(f"No card with front value {front} in deck")
            break

        front = input('Front: ')
        back = input('Back: ')
        deck[index] = make_card(front, back)

        resp = input("Continue: ")
        if resp != 'y':
            break



if __name__ == '__main__':
    if len(sys.argv) > 2:
        mode, handle = sys.argv[1], sys.argv[2]
    elif len(sys.argv) == 2:
        mode = '-r'
        handle = sys.argv[1]
    else:
        print("argument missing: file name")
        sys.exit(1)

    # TODO: exception handling
    deck = read_deck(handle)
    
    if mode == '-a':
        add_cards(deck)
        save = input("Save changes: ")
        if save == 'y':
            # handle = input("File name: ")
            write_deck(deck, handle)
    elif mode == '-r':
        review_deck(deck)
    elif mode == '-v':
        show_deck(deck)
    elif mode == '-e':
        edit_deck(deck, handle)
        save = input("Save changes: ")
        if save == 'y':
            write_deck(deck, handle)
    else:
        print("command line argument", mode, "not recognised")
        sys.exit(0)
