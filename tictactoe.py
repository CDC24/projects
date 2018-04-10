#Caleb Callaway
#4/4/18
#tictactoe.py - project 1 - tic tac toe with graphics


from ggame import *
from random import randint


"""
def isEmpty(squarenum):         #returns True if the square "squarenum" is empty and False if there is already an X or O there.
    if data[squarenum] == True:
        return (isEmpty(squarenum) = True)
        else:
            return (isEmpty(squarenum) = False)
"""

def winner():                   #returns True if someone won and False otherwise, but not who won
    return


def fullboard():                #returns True if every square is filled up with an X or O and False otherwise.
    print(fullboard())
    if data["square11"] == "x" or data["square11"] == "o":
        if data["square12"] == "x" or data["square12"] == "o":
            if data["square13"] == "x" or data["square13"] == "o":
                if data["square21"] == "x" or data["square21"] == "o":
                    if data["square22"] == "x" or data["square22"] == "o":
                        if data["square23"] == "x" or data["square23"] == "o":
                            if data["square31"] == "x" or data["square31"] == "o":
                                if data["square32"] == "x" or data["square32"] == "o":
                                    if data["square33"] == "x" or data["square33"] == "o":
                                        return (True)
    return (False)


def computerTurn():             #picks a random unused square and places the computer piece there.
    
    piecePlaced=False
    
    horiz = randint(1,3)
    vert = randint(1,3)
    
    Os = TextAsset("O", fill=black, style='bold 100pt Times')
    
    if horiz==1 and fullboard()==False:                                        #decides for first column numbers
        
        if vert == 1 and data["square11"]=="":
            Sprite (Os,(120,100))
            data["square11"]= "o"
            piecePlaced=True
            
        elif vert == 2 and data["square12"]=="":
            Sprite (Os,(120,230))
            data["square12"]="o"
            piecePlaced=True
            
        elif vert == 3 and data["square13"]=="":
            Sprite (Os,(120,360))
            data["square13"]="o"
            piecePlaced=True
            
    elif horiz == 2 and fullboard()==False:                                    #decides for second column numbers
        
        if vert == 1 and data["square21"]=="":
            Sprite (Os,(250,100))
            data["square21"]="o"
            piecePlaced=True
            
        elif vert == 2 and data["square22"]=="":
            Sprite (Os,(250,230))
            data["square22"]="o"
            piecePlaced=True
            
        elif vert == 3 and data["square23"]=="":
            Sprite (Os,(250,360))
            data["square23"]="o"
            piecePlaced=True
            
    elif horiz == 3 and fullboard()==False:                            #decides for third column numbers
        
        if vert == 1 and data["square31"]=="":
            Sprite (Os,(380,100))
            data["square31"]="o"
            piecePlaced=True
            
            
        elif vert == 2 and data["square32"]=="":
            Sprite (Os,(380,230))
            data["square32"]="o"
            piecePlaced=True
            
        elif vert == 3 and data["square33"]=="":
            Sprite (Os,(380,360))
            data["square33"]="o"
            piecePlaced=True
            
    if piecePlaced==False: computerTurn()


def mouseClick(event):                   #responds to clicks; the player's turn

    Xs = TextAsset("X", fill=black, style='bold 100pt Times')

    if 100<= event.x <= (100+(WIDTH/3)):                                        #checks for first column click
        
        if 100<= event.y <=(100+(HEIGHT/3)) and data["square11"]=="":
            Sprite (Xs,(120,100))
            data["square11"]= "x"
            computerTurn()
            
        elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)) and data["square12"]=="":
            Sprite (Xs,(120,230))
            data["square12"]= "x"
            computerTurn()
            
        elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT) and data["square13"]=="":
            Sprite (Xs,(120,360))
            data["square13"]= "x"
            computerTurn()
            
    elif (100+(WIDTH/3))<= event.x <= (100+(2*WIDTH/3)):                        #checks for second column click
        
        if 100<= event.y <=(100+(HEIGHT/3)) and data["square21"]=="":
            Sprite (Xs,(250,100))
            data["square21"]= "x"
            computerTurn()
            
        elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)) and data["square22"]=="":
            Sprite (Xs,(250,230))
            data["square22"]= "x"
            computerTurn()
            
        elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT) and data["square23"]=="":
            Sprite (Xs,(250,360))
            data["square23"]= "x"
            computerTurn()
            
    elif (100+(2*WIDTH/3))<= event.x <= (100+WIDTH):                            #checks for third column click
        
        if 100<= event.y <=(100+(HEIGHT/3)) and data["square31"]=="":
            Sprite (Xs,(380,100))
            data["square31"]= "x"
            computerTurn()
            
        elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)) and data["square32"]=="":
            Sprite (Xs,(380,230))
            data["square32"]= "x"
            computerTurn()
            
        elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT) and data["square33"]=="":
            Sprite (Xs,(380,360))
            data["square33"]= "x"
            computerTurn()


if __name__ == '__main__':


    data = {}
    data["square11"] = ""
    data["square12"] = ""
    data["square13"] = ""
    data["square21"] = ""
    data["square22"] = ""
    data["square23"] = ""
    data["square31"] = ""
    data["square32"] = ""
    data["square33"] = ""


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
    
    
    
    
    
    
