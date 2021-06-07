'''
@Author: Santanu Mohapatra
@Date: 03/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 17:20 PM
@Title: Deck of cards problem
'''

import itertools
import random

suits = "Clubs", "Diamonds", "Hearts", "Spades" 
rank = "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"

class DeckOfCards:

    @staticmethod
    def deck_of_cards():
        cards = list(itertools.product([ "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                              ['Clubs', 'Diamonds', 'Hearts', 'Spades']))

        random.shuffle(cards)  #shuffling cards

        print("***Player 1 Cards***")          
        array_one = []
        try:
            for index in range(9):
                array_one.append(cards[index][0])
                print([ array_one[index] + " of "+ cards[index][1] ], end = " ")
                cards.remove(cards[index])
        except IndexError:
            print("Index is out of range")

        print("\n")
        print("***Player 2 Cards***")
        array_two = []
        try:
            for indexOne in range(9):
                array_two.append(cards[indexOne][0])
                print([array_two[indexOne] + " of " + cards[indexOne][1] ], end = " " )
                cards.remove(cards[indexOne])
        except IndexError:
            print("Index is out of range")

        print("\n")
        print("***Player 3 Cards***")
        array_three = []
        try:
            for indexTwo in range(9):
                array_three.append(cards[indexTwo][0])
                print([array_three[indexTwo] + " of " + cards[indexTwo][1] ], end = " ")
                cards.remove(cards[indexTwo])
        except IndexError:
            print("Index is out of range")

        print("\n")
        print("***Player 4 Cards***\n")
        array_four = []
        try:
            for indexThree in range(9):
                array_four.append(cards[indexThree][0])
                print([array_four[indexThree] + " of " + cards[indexThree][1] ], end = " " )
                cards.remove(cards[indexThree])
        except IndexError:
            print("Index is out of range")

"""
Declare the class within the main function to emulate deck of cards problem
Parameter:
lsit of cards are taken as parameters
"""
if __name__ == "__main__":
    DeckOfCards.deck_of_cards()  