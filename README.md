# Card-game-in-Python

In the project there are two files, in one the classes for the game are defined: player, deck and card.
In both, the departments are realized and the game is underway.
We put emphasis on smart and efficient code, and used sophisticated ways throughout the code.
For example - the distribution of the cards to the two players was done in a smart way: a Boolean variable was defined as 0.
A loop ran 52 times as the number of cards,
the turn to receive the card changes from one player to another by changing the boolean variable to reverse after a player receives the card.
flug = 1
for x in range(52):
    tmp = decks.dropCard()
    if flug == 1:
        player1.privateDeck.append(tmp)
        flug = 0
    otherwise:
        player2.privateDeck.append(tmp)
        flug = 1
        
 In addition, for the purpose of understanding the code, I will explain:
To easily add cards to a player's private deck when winning, a global variable - list "draws" has been defined
Each round both players draw cards and they are kept in this list. Even in "war" mode, the four cards in this list are kept.
The player whose card trumps - adds the list of "drawn" cards to his private card list.
I enjoyed doing the project, it solidified my knowledge and understanding of Python and made thinking in general more witty.🎃
Thanks
