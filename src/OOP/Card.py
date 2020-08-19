import random


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.total_cards = [Card(value, suit) for suit in allowed_suits for value in allowed_values]
    def count(self):
        return len(self.total_cards)
    def __repr__(self):
        return f"Deck of {self.count()} cards"
    def _deal(self, number):
        count = self.count()
        actually_left = min([count, number])
        if count == 0:
            raise ValueError("All cards have been dealt")
        total_cards = self.total_cards[-actually_left:]
        self.total_cards = self.total_cards[:-actually_left]
        return total_cards

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        random.shuffle(self.total_cards)
        return self

    def deal_card(self):
        return self._deal(1, [0])

    def deal_hand(self, hand_size):
        return self._deal(hand_size)


my_deck = Deck()
print(my_deck)
my_deck.shuffle()
card = my_deck.deal_card()
print(card)
hand = my_deck.deal_hand(5)
print(hand)
print(my_deck)
