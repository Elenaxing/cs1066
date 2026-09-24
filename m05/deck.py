### m05/deck.py
import cards

def main():
    ans = input('Do you want the deck shuffled? [yY] ')

    # Create the deck then possibly shuffle it
    if ans != '' and ans.strip() in 'yY':
        deck = cards.shuffle()
    else:
        deck = cards.shuffle(False)

    print('\nFull deck:')
    print(deck)

    print('\nDone!')

if __name__ == '__main__':
    main()
