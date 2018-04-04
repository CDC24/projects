#Caleb Callaway
#4/4/18
#tictactoe.py - project 1 - tic tac toe with graphics


from ggame import *


def isEmpty(squarenum):         #returns True if the square "squarenum" is empty and False if there is already an X or O there.



def winner():                   #returns True if someone won and False otherwise, but not who won



def fullboard():                #returns True if every square is filled up with an X or O and False otherwise.



def computerTurn():             #picks a random unused square and places the computer piece there.



def mouseClick(event):
    


if __name__ == '__main__':








#graphics

black = Color(0x000000,1)
red = Color(0xFF0000,1)

#setting up board
vertBoardLine = RectangleAsset(width,height,LineStyle(1,black),black)
horizBoardLine = RectangleAsset(height,width,LineStyle(1,black),black)

def printBoard():            #prints out the board with the Xs and Os in the correct places and numbers in the open spots.
    blackline = 











