#Caleb Callaway
#4/4/18
#tictactoe.py - project 1 - tic tac toe with graphics


from ggame import *


def isEmpty(squarenum):         #returns True if the square "squarenum" is empty and False if there is already an X or O there.
    return


def winner():                   #returns True if someone won and False otherwise, but not who won
    return


def fullboard():                #returns True if every square is filled up with an X or O and False otherwise.
    return


def computerTurn():             #picks a random unused square and places the computer piece there.
    return


def mouseClick(event):
    return


if __name__ == '__main__':



    #graphics
    
    black = Color(0x000000,1)
    red = Color(0xFF0000,1)
    
    #setting up board
    
    HEIGHT = 300
    WIDTH = 300
    
    vertBoardLine = RectangleAsset(2,200,LineStyle(1,black),black)
    horizBoardLine = RectangleAsset(200,2,LineStyle(1,black),black)
    
    
    
    
    Sprite(horizBoardLine(200+HEIGHT/3,200))
    Sprite(horizBoardLine(200+(2*HEIGHT/3),200))
    Sprite(vertBoardLine(200,200+WIDTH/3))
    Sprite(vertBoardLine(200,200+(2*WIDTH/3)))
    
    App().run()
    
    
    
    
    
    
