import random
import collections

POKER_SUITS = ["spades", "hearts", "diamonds", "clubs"]
VALUES = ["ace", "king", "queen", "jack", "10", "9", "8", "7", "6", "5", "4", "3", "2"]

def create_deck():
    decks = []
    for poker_suit in POKER_SUITS:
        for value in VALUES:
            decks.append((poker_suit, value))
    
    return decks

def get_hand(decks, hand_size):
    deck = random.sample(decks, hand_size)

    return deck

def main(hand_size, attempts):
    decks = create_deck()

    hands = []
    for _ in range(attempts):
        hand = get_hand(decks, hand_size)
        hands.append(hand)

    evens = 0
    for hand in hands:
        values = []
        for card in hand:
            values.append(card[1])

        counter = dict(collections.Counter(values))
        print(counter)
        for val in counter.values():
            if val == 3:
                evens += 1
                break
    
    even_probability = evens / attempts
    print(f'The probability of getting a even in a hand of {hand_size} decks is {even_probability}')

if __name__ == "__main__":
    hand_size = int(input("How many decks will the hand be: "))
    attempts = int(input("How many attempts to calculate the probability: "))

    main(hand_size, attempts)