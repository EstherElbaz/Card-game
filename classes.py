import random
global shlufim
shlufim = []

class Player:

    def __init__(self ,name):
        self.name = name
        self.privateDeck = []

    def dropCard(self):
        card = self.privateDeck.pop(0)
        shlufim.append(card)
        return card

    def addCards(self):
        self.privateDeck.extend(shlufim)

    def __str__(self):
        return f'{self.name} has {len(self.privateDeck)} cards'


class Card:
    details = [0, 0, 0]

    def __init__(self, value, shape):

        self.details[0] = value
        if value == 11:
            self.details[2] = "prince"
        elif value == 12:
            self.details[2] = "queen"
        elif value == 13:
            self.details[2] = "king"
        self.details[1] = shape
        # print(f'{self.details[0]}_of_{self.details[1]}'  )

    def __str__(self):
        return f'{self.details[0]}_of_{self.details[1]}'




class Deck:
    shapes = ["🍔", "🍜", "🛴", "🎁"]

    def __init__(self):
        self.cardList = []
        for i in Deck.shapes:
            for x in range(1, 14):
                w = Card(x, i)
                print(w)
                self.cardList.append(w)
                # print(w)

        print(*self.cardList)

    def mixDeck(self):
        random.shuffle(self.cardList)
        for x in self.cardList:
            print(x)

    def dropCard(self):
        x = self.cardList.pop(0)
        return x

    # passing the deck one by one in order to give each one of them his own deck:
    def split(self, player1, player2,decks):
        flug = 1
        for x in range(52):
            tmp = decks.dropCard()
            if flug == 1:
                player1.privateDeck.append(tmp)
                flug = 0
            else:
                player2.privateDeck.append(tmp)
                flug = 1