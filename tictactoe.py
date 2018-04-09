#Caleb Callaway
#4/4/18
#tictactoe.py - project 1 - tic tac toe with graphics


from ggame import *
from random import randint



def isEmpty(squarenum):         #returns True if the square "squarenum" is empty and False if there is already an X or O there.
    return isEmpty(squarenum)=True


def winner():                   #returns True if someone won and False otherwise, but not who won
    return


def fullboard():                #returns True if every square is filled up with an X or O and False otherwise.
    return


def computerTurn():             #picks a random unused square and places the computer piece there.
    horiz = randint(1,3)
    vert = randint(1,3)
    
    Os = TextAsset("O", fill=black, style='bold 100pt Times')
    
    if horiz==1:                                        #decides for first column numbers
        
        if vert == 1 and data[square11]==True:
            Sprite (Os,(120,100))
            return isEmpty(square11)= False
            
        elif vert == 2 and data[square12]==True:
            Sprite (Os,(120,230))
            return isEmpty(square12)=False
            
        elif vert == 3 and data[square13]==True:
            Sprite (Os,(120,360))
            return isEmpty(square13)=False
            
    elif horiz == 2:                                    #decides for second column numbers
        
        if vert == 1 and data[square21]==True:
            Sprite (Os,(250,100))
            return isEmpty(square21)=False
            
        elif vert == 2 and data[square22]==True:
            Sprite (Os,(250,230))
            return isEmpty(square22)=False
            
        elif vert == 3 and data[square23]==True:
            Sprite (Os,(250,360))
            return isEmpty(square23)=False
            
    elif horiz == 3:                            #decides for third column numbers
        
        if vert == 1 and data[square31]==True:
            Sprite (Os,(380,100))
            return isEmpty(square31)=False
            
        elif vert == 2 and data[square32]==True:
            Sprite (Os,(380,230))
            return isEmpty(square32)=False
            
        elif vert == 3 and data[square33]==True:
            Sprite (Os,(380,360))
            return isEmpty(square33)=False


def mouseClick(event):                   #responds to clicks; the player's turn

    Xs = TextAsset("X", fill=black, style='bold 100pt Times')

    if 100<= event.x <= (100+(WIDTH/3)):                                        #checks for first column click
        
        if 100<= event.y <=(100+(HEIGHT/3)):
            Sprite (Xs,(120,100))
            computerTurn()
            
        elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)):
            Sprite (Xs,(120,230))
            computerTurn()
            
        elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT):
            Sprite (Xs,(120,360))
            computerTurn()
            
    elif (100+(WIDTH/3))<= event.x <= (100+(2*WIDTH/3)):                        #checks for second column click
        
        if 100<= event.y <=(100+(HEIGHT/3)):
            Sprite (Xs,(250,100))
            computerTurn()
            
        elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)):
            Sprite (Xs,(250,230))
            computerTurn()
            
        elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT):
            Sprite (Xs,(250,360))
            computerTurn()
            
    elif (100+(2*WIDTH/3))<= event.x <= (100+WIDTH):                            #checks for third column click
        
        if 100<= event.y <=(100+(HEIGHT/3)):
            Sprite (Xs,(380,100))
            computerTurn()
            
        elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)):
            Sprite (Xs,(380,230))
            computerTurn()
            
        elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT):
            Sprite (Xs,(380,360))
            computerTurn()


if __name__ == '__main__':


    data = {}
    data[square11] = True
    data[square12] = True
    data[square13] = True
    data[square21] = True
    data[square22] = True
    data[square23] = True
    data[square31] = True
    data[square32] = True
    data[square33] = True


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
    
    
    
    
    
    
