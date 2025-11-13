from flashcard import add_card, make_card, write_deck, read_deck

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


if __name__ == '__main__':
    handle = input("Enter file to read deck:")

    # TODO: exception handling
    deck = read_deck(handle)

    print("Select an option:")
    mode = input("A to add cards, R to review deck")
    
    if mode == 'A':
        add_cards(deck)
        save = input("Save file: ")
        if save == 'y':
            handle = input("File name: ")
            write_deck(deck, handle)
    elif mode == 'R':
        review_deck(deck)
