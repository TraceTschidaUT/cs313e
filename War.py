#  File: Dice.py
#  Description: A game of war simulator 
#  Student's Name: Trace Tschida
#  Student's UT EID: TRT729
#  Course Name: CS 313E 
#  Unique Number: 51465
#
#  Date Created: 9/24/2017
#  Date Last Modified: 9/26/2017

import random

class Deck():

    # initialize
    def __init__(self):

        # hold the list of cards
        self.cardList = []
        
        # list of rank and suits
        lst_rank = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        lst_suit = ["C", "D", "H", "S"]

        # loop through each rank and suit and create a card
        for suit in lst_suit:
            for rank in lst_rank:

                # create a card and append to the list
                self.cardList.append(Card(suit, rank))
    
    def shuffle(self):

        # shuffle the cards
        random.shuffle(self.cardList)

    def dealOne(self, player):

        # remove the top card
        card_to_deal = self.cardList.pop(0)

        # give the player a card
        player.hand.append(card_to_deal)
        player.handTotal += 1

    def __str__(self):

        str_deck = ""
        # print method in rows of 13
        count = 1
        for card in self.cardList:

            # spacing for the prints
            space = "  "
            
            # print the space out front 
            if len(str(card)) == 3:
                space = " "

            str_deck += space + str(card)

            # check to see if 13th card
            if count % 13 == 0 and count != 0:
                str_deck += "\n"
            count += 1

        return str_deck
            

class Card():

    def __init__(self, _suit, _rank):
        self.suit = _suit
        self.rank = _rank

        if self.rank not in ["J","Q","K","A"]:
            self.value = int(self.rank)
        elif self.rank == "J":
            self.value = 11
        elif self.rank == "Q":
            self.value = 12
        elif self.rank == "K":
            self.value = 13
        elif self.rank == "A":
            self.value = 14

    def __str__(self):
        
        return self.rank + self.suit.upper()


class Player():

    def __init__(self):
        self.hand = []
        self.handTotal = 0

    def handNotEmpty(self):
        if len(self.hand) != 0: # check that it is blank
            return True

    def playCard(self):

        # get the top card
        playCard = self.hand.pop(0)

        self.handTotal -= 1

        # return the top card of the deck
        return playCard

    def __str__(self):

        # hold the string to be returned
        str_hand = ""

        # hold the count to print correctly for formatting
        count = 1
        for i in range(len(self.hand)):

            # spacing for the prints
            space = "  "
            
            # print the space out front 
            if len(str(self.hand[i])) == 3:
                space = " "

            str_hand += space + str(self.hand[i])

            # check to see if 13th card
            if count % 13 == 0 and count != 0:
                str_hand += "\n"
            count += 1

        return str_hand

def playGame(cardDeck, player1, player2):

    # display the initial cards
    print()
    print("Initial Hands:")
    print("Player 1:")
    print(player1)
    print()

    print("Player 2:")
    print(player2)
    print()

    # counter for number of rounds
    int_rounds = 1
    while True:

        try: # to draw a card, if a player has no more = auto loss

            # hold the cards for the round
            player1RoundCards = []
            player2RoundCards = []

            # print the round
            print("ROUND " + str(int_rounds))

            # each player plays a card and add to round cards
            player1Card = player1.playCard()
            player1RoundCards.append(player1Card)
            print("Player 1 plays:  " + str(player1Card))

            player2Card = player2.playCard()
            player2RoundCards.append(player2Card)
            print("Player 2 plays:  " + str(player2Card))
            print()

            # check to see if the values are the same
            while player1Card.rank == player2Card.rank:

                # print the war
                print("War starts:  " + str(player1Card) + " = " +  str(player2Card))

                # each player puts down three cards
                for i in range(0,3):
                    
                    # player 1 and 2 play cards
                    player1DownCard = player1.playCard()
                    player1RoundCards.append(player1DownCard)

                    player2DownCard = player2.playCard()
                    player2RoundCards.append(player2DownCard)

                    # spacing alignment 
                    space1 = "  "
                    space2 = "  "

                    if len(str(player1DownCard)) == 3:
                        space1 = " "
                    if len(str(player2DownCard)) == 3:
                        space2 = " "

                    # print the results
                    print("Player 1 puts" + space1 + str(player1DownCard) + " face down")
                    print("Player 2 puts" + space2 + str(player2DownCard) + " face down")

                # reset the player card to a new card
                # allows the loop to iterate
                player1Card = player1.playCard()
                player2Card = player2.playCard()

                # add the cards to the round cards
                player1RoundCards.append(player1Card)
                player2RoundCards.append(player2Card)

                # spacing alignment 
                space1 = "  "
                space2 = "  "

                if len(str(player1Card)) == 3:
                    space1 = " "
                if len(str(player2Card)) == 3:
                    space2 = " " 

                # print the face up cards
                print("Player 1 puts" + space1 + str(player1Card) + " face up")
                print("Player 2 puts" + space2 + str(player2Card) + " face up")
                print()
                

            # determine whom won becuase the cards are not the same
            if (player1Card.value > player2Card.value):
                
                # print the result
                print("Player 1 wins round " + str(int_rounds) + ":  " + str(player1Card) + " > " + str(player2Card))
                print()

                # add the first players hands to the winner
                # loop through the played cards 
                for i in range(len(player1RoundCards)):

                    # take the first card out for player 1
                    player1.hand.append(player1RoundCards[i])

                    # update the number of cards in the hand
                    player1.handTotal += 1 

                for i in range(len(player2RoundCards)):

                    # take the first card out for player 2
                    player1.hand.append(player2RoundCards[i])

                    # update the number of cards in the hand
                    player1.handTotal += 1
            
            else: # player 2 has won

                # print the result
                print("Player 2 wins round " + str(int_rounds) + ":  " + str(player2Card) + " > " + str(player1Card))
                print()
                
                # add the second players hands to the winner
                # loop through the played cards 
                for i in range(len(player1RoundCards)):

                    # take the first card out for player 1
                    player2.hand.append(player1RoundCards[i])

                    # update the number of cards in the hand
                    player2.handTotal += 1

                # loop through the played cards for the other player 
                for i in range(len(player2RoundCards)):

                    # take the first card out for player 2
                    player2.hand.append(player2RoundCards[i])

                    # update the number of cards in the hand
                    player2.handTotal += 1

            # print the rands remaining
            print("Player 1 now has " + str(player1.handTotal) + " card(s) in hand:")
            print(player1)
            print()

            print("Player 2 now has " + str(player2.handTotal) + " card(s) in hand:")
            print(player2)
            print()

            if (player1.handNotEmpty() and player2.handNotEmpty()):
                # increase the number of rounds 
                int_rounds += 1

                print()

            else:
                # end the loop
                break
        except IndexError as ide:
            
            # print the results of the game

            # blank line
            print()

            if player1.handNotEmpty():
                print("Player 2 has run out of cards.")
            else:
                print("Player 1 has run our of cards.")

            # break out of the loop
            break
            

def main():

    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(15)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    player1 = Player()              # create a player
    player2 = Player()              # create another player

    for i in range(26):             # deal 26 cards to each player, one at 
       cardDeck.dealOne(player1)    #   a time, alternating between players
       cardDeck.dealOne(player2)
    
    playGame(cardDeck,player1,player2)

    if player1.handNotEmpty():
        print("\n\nGame over.  Player 1 wins!")
    else:
        print("\n\nGame over.  Player 2 wins!")

    print ("\n\nFinal hands:")    
    print ("Player 1:   ")
    print (player1)                 # printing a player object should print that player's hand
    print ("\nPlayer 2:")
    print (player2)                 # one of these players will have all of the cards, the other none
    
main()