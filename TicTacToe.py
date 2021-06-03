'''
@Author: Santanu Mohapatra
@Date: 02/06/2021
@Last Modified by: Santanu Mohapatra
@Last Modified Time: 12:10 PM
@Title: To simulate Tic-Tac-Toe Games
'''
import random as r
# To create positions of a board
board_position={1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

def printBoard(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print('--|--|--')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('--|--|--')
    print(board[7] + '|' + board[8] + '|' + board[9])

"""
Description:
A printBorad  function is created to print the board after taking input.
Parameter:
board is the array that contains position printed in the game board.
"""

def player(board_position, attempt, index):
    try:
        if(attempt == 'o'):
            print('Player ' + attempt + ', Enter your postion number ')
        if(attempt=='x'):
            attempt=r.choice(board_position)
            

    except ValueError:
        print("Enter a correct position")

    attempt1 = int(input())
    if board_position[attempt1] == ' ':
        board_position[attempt1] = attempt
        printBoard(board_position)

    else:
        print('Postion is occupied.Try with different positions.')
        player(board_position, attempt, index)

    if (index >= 4):

        if (board_position[1] == board_position[2] == board_position[3] == attempt or board_position[4] == board_position[5] == board_position[6] == attempt or board_position[7] == board_position[8] ==
                board_position[9] == attempt or board_position[1] == board_position[4] == board_position[7] == attempt or board_position[2] == board_position[5] == board_position[8] == attempt or
                board_position[3] == board_position[6] == board_position[9] == attempt or board_position[1] == board_position[5] == board_position[9] == attempt or board_position[3] == board_position[5] ==
                board_position[7] == attempt):
            printBoard(board_position)
            print(attempt + ' WON')
            return 1
"""
Description:
player function to take input position of player and then check if the player won using if statement 
Parameter:
board_position is the position of the board 
"""


def tictactoe():
    attempt = 'o'
    try:
        for index in range(10):
            if index == 9:
                print("Match Draw")
                break
            if (player(board_position, attempt, index) == 1):
                break
            if (attempt == 'x'):
                attempt = 'o'
            else:
                attempt = 'x'
    except NameError as e:
        print(e)    

#Call the tictactoe() functions to run the game simulator
tictactoe()
