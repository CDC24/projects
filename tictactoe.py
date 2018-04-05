#Caleb Callaway
#4/4/18
#tictactoe.py - project 1 - tic tac toe with graphics


from ggame import *
from random import randint



def isEmpty(squarenum):         #returns True if the square "squarenum" is empty and False if there is already an X or O there.
    return


def winner():                   #returns True if someone won and False otherwise, but not who won
    return


def fullboard():                #returns True if every square is filled up with an X or O and False otherwise.
    return


def computerTurn():             #picks a random unused square and places the computer piece there.
    horiz = randint(1,3)
    vert = randint(1,3)


def mouseClick(event):
    if 100<= event.x <= (100+(WIDTH/3)):
        if 100<= event.y <=(100+(HEIGHT/3)):
            letters = TextAsset("X", fill=black, style='bold 100pt Times')
            Sprite (letters,(120,100))
        if (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)):
            letters = TextAsset("X", fill=black, style='bold 100pt Times')
            Sprite (letters,(120,230))
        if (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT):
            letters = TextAsset("X", fill=black, style='bold 100pt Times')
            Sprite (letters,(120,360))


if __name__ == '__main__':



    #graphics
    
    black = Color(0x000000,1)
    red = Color(0xFF0000,1)
    
    #setting up board
    
    HEIGHT = 400
    WIDTH = 400
    
    vertBoardLine = RectangleAsset(2,HEIGHT,LineStyle(1,black),black)
    horizBoardLine = RectangleAsset(WIDTH,2,LineStyle(1,black),black)
    
    
    
    # these sprite the grid
    Sprite(horizBoardLine,(100,100+(HEIGHT/3)))
    Sprite(horizBoardLine,(100,100+(2*HEIGHT/3)))
    Sprite(vertBoardLine,(100+(WIDTH/3),100))
    Sprite(vertBoardLine,(100+(2*WIDTH/3),100))
    
    
    
    App().listenMouseEvent("click",mouseClick)
    App().run()
    
    
    
    
    
    
