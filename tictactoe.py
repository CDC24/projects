#Caleb Callaway
#4/4/18
#tictactoe.py - project 1 - tic tac toe with graphics


from ggame import *
from random import randint



def winner(lett):                   #returns True if the requested letter won and False otherwise
    if data["square11"] == lett and  data["square12"] == lett and data["square13"] == lett: #checks vertical combos
        return (True)
        data["gameover"] = True
    if data["square21"] == lett and  data["square22"] == lett and data["square23"] == lett:
        return (True)
        data["gameover"] = True
    if data["square31"] == lett and  data["square32"] == lett and data["square33"] == lett:
        return (True)
        data["gameover"] = True
    if data["square11"] == lett and  data["square21"] == lett and data["square31"] == lett: #checks horizontal combos
        return (True)
        data["gameover"] = True
    if data["square12"] == lett and  data["square22"] == lett and data["square32"] == lett:
        return (True)
        data["gameover"] = True
    if data["square13"] == lett and  data["square23"] == lett and data["square33"] == lett:
        return (True)
        data["gameover"] = True
    if data["square11"] == lett and  data["square22"] == lett and data["square33"] == lett: #checks diagonal combos
        return (True)
        data["gameover"] = True
    if data["square31"] == lett and  data["square22"] == lett and data["square13"] == lett:
        return (True)
        data["gameover"] = True
    else:
        return (False)


def fullboard():                #returns True if every square is filled up with an X or O and False otherwise.
    if data["square11"] == "" or  data["square12"] == "" or data["square13"] == "" or data["square21"] == "" or data["square22"] == "" or data["square23"] == "" or data["square31"] == "" or data["square32"] == "" or data["square33"] == "":
        return (False)
    else:
        return(True)



def computerTurn():             #picks a random unused square and places the computer piece there.
    
    piecePlaced=False #used to re-run the function if no open square found
    
    horiz = randint(1,3)  #Random numbers for picking squares
    vert = randint(1,3)

# Establishes text sprites

    red = Color(0xFF0000,1)
    youLose = TextAsset("You lost a game of TIC TAC TOE and your opponent was just guessing! Sheesh.", fill=red, style='bold 25pt Times')
    Os = TextAsset("O", fill=black, style='bold 100pt Times')
    
    
# Picking squares using random numbers and completing move
    
    if horiz == 1:                                        #decides for first column numbers
        
        if vert == 1 and data["square11"]=="":
            Sprite (Os,(120,100))
            data["square11"]= "o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
        elif vert == 2 and data["square12"]=="":
            Sprite (Os,(120,230))
            data["square12"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
        elif vert == 3 and data["square13"]=="":
            Sprite (Os,(120,360))
            data["square13"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
    elif horiz == 2:                                    #decides for second column numbers
        
        if vert == 1 and data["square21"]=="":
            Sprite (Os,(250,100))
            data["square21"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
        elif vert == 2 and data["square22"]=="":
            Sprite (Os,(250,230))
            data["square22"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
        elif vert == 3 and data["square23"]=="":
            Sprite (Os,(250,360))
            data["square23"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
    elif horiz == 3:                            #decides for third column numbers
        
        if vert == 1 and data["square31"]=="":
            Sprite (Os,(380,100))
            data["square31"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
            
        elif vert == 2 and data["square32"]=="":
            Sprite (Os,(380,230))
            data["square32"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
        elif vert == 3 and data["square33"]=="":
            Sprite (Os,(380,360))
            data["square33"]="o"
            if winner("o"):
                Sprite(youLose,(600,100))
            piecePlaced=True
            
    if piecePlaced==False: computerTurn()


def mouseClick(event):                   #responds to clicks; the player's turn
    if data["gameover"] == False:
    
    # Establishes text sprites
    
        red = Color(0xFF0000,1)
        Xs = TextAsset("X", fill=black, style='bold 100pt Times')
        tiegame = TextAsset("It's a tie game, my dude!", fill=red, style='bold 50pt Times')
        youWin = TextAsset("Surprisingly, You Win!!", fill=red, style='bold 50pt Times')
    
    #Actions on click and turn completion
        
        if 100<= event.x <= (100+(WIDTH/3)):                                        #checks for first column click
            
            if 100<= event.y <=(100+(HEIGHT/3)) and data["square11"]=="":
                Sprite (Xs,(120,100))
                data["square11"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                    
            elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)) and data["square12"]=="":
                Sprite (Xs,(120,230))
                data["square12"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                
            elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT) and data["square13"]=="":
                Sprite (Xs,(120,360))
                data["square13"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                    
        elif (100+(WIDTH/3))<= event.x <= (100+(2*WIDTH/3)):                        #checks for second column click
                
            if 100<= event.y <=(100+(HEIGHT/3)) and data["square21"]=="":
                Sprite (Xs,(250,100))
                data["square21"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:                                       
                    computerTurn()
                
            elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)) and data["square22"]=="":
                Sprite (Xs,(250,230))
                data["square22"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                    
            elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT) and data["square23"]=="":
                Sprite (Xs,(250,360))
                data["square23"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                    
        elif (100+(2*WIDTH/3))<= event.x <= (100+WIDTH):                            #checks for third column click
                
            if 100<= event.y <=(100+(HEIGHT/3)) and data["square31"]=="":
                Sprite (Xs,(380,100))
                data["square31"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                    
            elif (100+(HEIGHT/3))<= event.y <=(100+(2*HEIGHT/3)) and data["square32"]=="":
                Sprite (Xs,(380,230))
                data["square32"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()
                    
            elif (100+(2*HEIGHT/3))<= event.y <=(100+HEIGHT) and data["square33"]=="":
                Sprite (Xs,(380,360))
                data["square33"]= "x"
                if winner("x"):
                    Sprite(youWin,(600,100))
                    data["gameover"] = True
                elif fullboard():
                    Sprite(tiegame,(600,100))
                else:
                    computerTurn()


if __name__ == '__main__':


    data = {}
    data["square11"] = ""     #used for determining empty squares and win combos
    data["square12"] = ""
    data["square13"] = ""
    data["square21"] = ""
    data["square22"] = ""
    data["square23"] = ""
    data["square31"] = ""
    data["square32"] = ""
    data["square33"] = ""

    data["gameover"] = False   #for stopping game after a win

    #graphics
    
    black = Color(0x000000,1)
    red = Color(0xFF0000,1)
    yellow = Color(0xFFFF00,0.25)
    
    #setting up board
    
    HEIGHT = 400
    WIDTH = 400
    
    vertBoardLine = RectangleAsset(2,HEIGHT,LineStyle(1,black),black)
    horizBoardLine = RectangleAsset(WIDTH,2,LineStyle(1,black),black)
    boardBox = RectangleAsset(WIDTH,HEIGHT,LineStyle(1,yellow),yellow)
    
    
    
    # these sprite the grid
    Sprite(boardBox,(100,100))
    Sprite(horizBoardLine,(100,100+(HEIGHT/3)))
    Sprite(horizBoardLine,(100,100+(2*HEIGHT/3)))
    Sprite(vertBoardLine,(100+(WIDTH/3),100))
    Sprite(vertBoardLine,(100+(2*WIDTH/3),100))
    
    
    
    App().listenMouseEvent("click",mouseClick)
    App().run()
    
    
    
    
    
    
