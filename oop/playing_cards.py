from enum import Enum
from typing import List
Suit = Enum('Suit', 'clubs diamonds hearts spades')
Values = Enum('Values', 'A ' + ' '.join([str(i) for i in range(2, 11)]) + ' J Q K')
class Card:
    SUITS = [s.name for s in Suit]
    VALUES = [v.name for v in Values]

    def __init__(self, suit, value):
        if suit not in self.SUITS:
            raise ValueError(suit + " not in suits")

        if value not in self.VALUES:
            raise ValueError(value + " not in card values")

        self.__suit = Suit[suit]
        self.__value = Values[value]

    @property
    def value(self) -> int:
        return self.__value.value

    def __str__(self) -> str:
        return f"{self.__value.name} of {self.__suit.name}"

class Deck:
    def __init__(self):
        self.__cards = [Card(suit.name, value.name) for suit in Suit
                                                    for value in Values]

    def find(self, suit, value):
        card = Card(suit, value)
        return self.__cards.index(card)

    def __len__(self):
        return len(self.__cards)

    def __getitem__(self, position):
        return self.__cards[position]

    def __str__(self):
        return str([str(c) for c in self.__cards])

class Game:
    def __init__(self):
        self.deck = Deck()

    def card_beats(self, card_a: int, card_b: int) -> bool:
        return self.deck[card_a].value > self.deck[card_b].value

if __name__ == "__main__":
    game = Game()
    #print(game.deck.find("diamonds", "A"))
    print(game.deck[5])
    print(game.deck[10])
    print("true" if game.card_beats(5, 10) else "false")
    print(Card('hearts', '5') in game.deck)
    for card in reversed(game.deck):
        print(card)
