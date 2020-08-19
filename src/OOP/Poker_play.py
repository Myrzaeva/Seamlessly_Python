import random
import cards

#without OOP:

def deal_hand(deck, num_cards):
    hand = deck[-num_cards]
    deck = deck[:-num_cards]
    return (deck, hand)

def reset_deck():
    card1 = {"value":"A", "suit": "hearts"}
    card2 = {"value":"A", "suit": "diamonds"}
    card3 = {"value":"A", "suit": "clubs"}
    card4 = {"value":"A", "suit": "spades"}

    card5 = {"value": "2", "suit": "hearts"}
    card6 = {"value": "2", "suit": "diamonds"}
    card7 = {"value": "2", "suit": "clubs"}
    card8 = {"value": "2", "suit": "spades"}

    card9 = {"value": "3", "suit": "hearts"}
    card10 = {"value": "3", "suit": "diamonds"}
    card11 = {"value": "3", "suit": "clubs"}
    card12 = {"value": "3", "suit": "spades"}

    card13 = {"value": "4", "suit": "hearts"}
    card14 = {"value": "4", "suit": "diamonds"}
    card15 = {"value": "4", "suit": "clubs"}
    card16 = {"value": "4", "suit": "spades"}

    return [card1,card2,card3,card4,card5,card6,card7,card8,card9,card10,card11,card12,
            card13,card14,card15,card16]

def display_card (card):
    return f"{card['value']} of {card['suit']}"

def display_hand (hand):
    return [display_card(card) for card in hand]

poker_deck = reset_deck()
random.shuffle(poker_deck)
poker_deck, hand1 = deal_hand(poker_deck,3)
poker_deck, hand2 = deal_hand(poker_deck,3)
print(display_hand(hand1))
print(display_hand(hand2))
poker_deck = reset_deck()
