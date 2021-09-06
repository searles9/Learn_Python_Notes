# Tik Tak Toe Program
#------------------------------
# What is this?:
# This is a 2 player tik tak toe game 
#------------------------------
# How does this work?:
# explanation...
#------------------------------
#===============================================
# CODE
#===============================================
# Import:
import random
#-----------------------------------------------
board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
#-----------------------------------------------
# Display:
def display_board(board):
    print('\n'*30) # clear the history
    print("-----------\nTIK TAK TOE\n-----------")
    print(board[7]+'|'+board[8]+'|'+board[9])
    print("-|-|-")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print("-|-|-")
    print(board[1]+'|'+board[2]+'|'+board[3])
#-------------------------------------------------
# Get player input
def player_input():
    marker = ''
    # choose X or O
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
    # assign marker
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else: 
        player2 = 'X'

    return(player1,player2)
# player1_marker , player2_marker = player_input()
# print(player1_marker)
#-------------------------------------------------
# Update board (3)
#Write a function that takes in the board list object, 
# a marker ('X' or 'O'), and a desired position 
# (number 1-9) and assigns it to the board.
def place_marker(board, marker, position):
    if marker == 'X':
        board[(position+1)] = 'X'
    else: 
        board[(position+1)] = 'O'
#-------------------------------------------------
# Write a function that takes in a board and a mark 
# (X or O) and then checks to see if that mark has won. 
def win_check(board, mark):
    player_won = False
    if (board[7] == board[8] == board[9] == mark):
        player_won = True
    elif (board[4] == board[5] == board[6] == mark):
        player_won = True
    elif (board[1] == board[2] == board[3] == mark):
        player_won = True
    elif (board[1] == board[5] == board[9] == mark):
        player_won = True
    elif (board[3] == board[5] == board[7] == mark):
        player_won = True
    else: 
        return player_won
#-------------------------------------------------
# Random module to decide who goes first - random.randint()
def choose_first():
    pass
#-------------------------------------------------
# Return a boolean to see if the space on a board is freely availible
#-------------------------------------------------
# Check is the board is full 
#-------------------------------------------------
# Write a function that asks for a player's next position 
# (as a number 1-9) and then uses the function from step
# 6 to check if it's a free position. If it is, then 
# return the position for later use.
#-------------------------------------------------
# Write a function that asks the player if they want 
# to play again and returns a boolean True if they 
# do want to play again.
#-------------------------------------------------
# Use while loops and the functions you've
#  made to run the game!
#-------------------------------------------------
#-------------------------------------------------
#-------------------------------------------------