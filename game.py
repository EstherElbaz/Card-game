from classes import Deck,Card,Player,shlufim
import random


# make a new deck and 2 players:
deck = Deck()
# mix the deck:
deck.mixDeck()
Dan = Player("Dan")
Gad = Player("Gad")
deck.split(Dan, Gad, deck)


def play(p1, p2):
    if p1.privateDeck == []:
        print(f"{p2}is the winner. congadulation!")
        return p2
    if p2.privateDeck == []:
        print(f"{p1}is the winner. congadulation!")
        return p1
    c1 = p1.dropCard()
    print(c1)
    c2 = p2.dropCard()
    print(c2)
    if c1.details[0] > c2.details[0]:
        p1.addCards()
        print(p1.name)
    elif c1.details[0] < c2.details[0]:
        p2.addCards()
        print(p2.name)
    else:
        war(p1, p2)
    shlufim = []
    play(p1, p2)


def war(p1, p2):
    print("war!!!!!!!!!!!!🚀🛬🛫🚀🛫🛬🛬")
    for x in range(3):
        shlufim.extend(p1.dropCard())
    for x in range(3):
        shlufim.extend(p2.dropCard())
    card1 = p1.dropCard()
    shlufim.extend(card1)
    card2 = p2.dropCard()
    shlufim.extend(card2)
    if card1.details[0] == card2.details[0]:
        return war(p1, p2)
    if card1.details[0] > card2.details[0]:
        p1.addCards()
    else:
        p2.addCards()


play(Dan, Gad)
