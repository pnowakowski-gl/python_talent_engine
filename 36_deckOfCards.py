suit = ["♠", "♥", "♦", "♣"]
value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


class Card:
    def __init__(self, suit="♠", value="2"):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.suit}{self.value}"


class Deck:
    def __init__(self):
        self.cards = [Card(s, v) for s in suit for v in value] + [Card("", "JOKER")]

    def __repr__(self):
        return " ".join(self.cards)

    def shuffle(self):
        from random import shuffle

        shuffle(self.cards)
        return self.cards

    def pop(self, num=-1):
        return self.cards.pop(num)

    def random(self):
        from random import choice

        return choice(self.cards)

    def index(self, card):
        try:
            return self.cards.index(card)
        except ValueError:
            return f"{card} is not in the deck."


"""d = Deck()
d.shuffle()
print(d)
d.pop()
print(d)
print(d.index("♥9"))
print(d.index("9"))"""
deck = Deck()
print(deck.cards.card)
print(deck.pop())
print(deck.pop().value)
deck.shuffle()
print(deck.pop())
print(deck.pop(23))
print([str(deck.random()) for i in range(5)])
