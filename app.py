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


def study_deck(deck):
    for card in deck:
        print(card['front'])
        input('Reveal')
        print(card['back'])


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
    handle = input("Name of deck file: ")
    
    try:
        deck = read_deck(handle)
    except FileNotFoundError:
        print("File with name", handle, "not found. Please enter a valid filename.")
    except UnicodeDecodeError:
        print(f"Could not read {handle}. Please enter a plaintext file")

    print("Select an option:")
    print("1. Add cards to deck.")
    print("2. Edit deck.")
    print("3. Study deck.")
    print("4. Revise deck.")

    options = ['1','2','3','4']

    resp = None
    
    while resp is None:
        input_value = input()
        if input_value in options:
            resp = input_value
        else:
            print("Please select a valid option.")

    if resp == '1':
        add_cards(deck)
        save = input("Save changes: ")
        if save == 'y':
            # handle = input("File name: ")
            write_deck(deck, handle)
    elif resp == '2':
        edit_deck(deck, handle)
        save = input("Save changes: ")
        if save == 'y':
            write_deck(deck, handle)
    elif resp == '4':
        print("Number of cards in deck:", len(deck))
        cards = None

        while cards is None:
            print("How many cards would you like to study?")
            num_cards = input()

            try:
                num_cards = int(num_cards)
                if num_cards <= 0:
                    print(f"{num_cards} is not positive.")
                elif num_cards >= len(deck):
                    print(f"{num_cards} exceeds the size of the deck.")
                else:
                    cards = deck[0:num_cards]
            except ValueError:
                print("Please input an integer.")

        review_deck(cards)
    elif resp == '3':
        study_deck(deck)
