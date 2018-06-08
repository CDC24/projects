#Caleb Callaway
#6/4/18
#smallBoardGameOfLife.py - Conway's Game of Life with a smaller board

from ggame import *

"""
Rules:
Any live cell with fewer than two live neighbors dies, as if by underpopulation.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""


def buildBoard():    #creates a 10 x 10 matrix of zeroes(dead squares)
    return [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]



def mouseClick(event):          #deals with mouse click coordinates and resulting actions
    row = (int(event.y//40))           #senses click in horizontal gridlines with 40 spacing
    col = (int(event.x//40))           #senses click in vertical gridlines with 40 spacing
    
    if 0<= event.x <=400 and 0<=event.y<=400 and data["matrix"][row][col] == 0:
        Sprite(liveCell,(event.x-(event.x%40),event.y-(event.y%40)))
        data["matrix"][row][col] = 1         #reverses square status in matrix

    elif 0<= event.x <=400 and 0<=event.y<=400 and data["matrix"][row][col] == 1:
        Sprite(deadCell,(event.x-(event.x%40),event.y-(event.y%40)))
        data["matrix"][row][col] = 0           #reverses square status in matrix
        
    elif 0<= event.x <=100 and 420<=event.y<=480:          #nextGen button
        redrawAll()
        
    elif 110<= event.x <=210 and 420<=event.y<=480:          #glider button
        glider()
        
    elif 220<= event.x <=320 and 420<=event.y<=480:          #plus button
        plus()


def space(event):               #does the SAME THING as the next gen button but uses the spacebar
    redrawAll()


def glider():                #makes a glider on board when button pressed
    data["matrix"][2][1] = 1        #changes matrix
    data["matrix"][3][2] = 1
    data["matrix"][3][3] = 1
    data["matrix"][2][3] = 1
    data["matrix"][1][3] = 1
    Sprite(liveCell,(80,40))        #temporary sprites
    Sprite(liveCell,(120,80))
    Sprite(liveCell,(120,120))
    Sprite(liveCell,(80,120))
    Sprite(liveCell,(40,120))
    
def plus():                #makes a plus on board when button pressed
    data["matrix"][5][4] = 1        #changes matrix
    data["matrix"][4][4] = 1
    data["matrix"][3][4] = 1
    data["matrix"][4][3] = 1
    data["matrix"][4][5] = 1
    Sprite(liveCell,(200,160))        #temporary sprites
    Sprite(liveCell,(160,160))
    Sprite(liveCell,(120,160))
    Sprite(liveCell,(160,120))
    Sprite(liveCell,(160,200))


def redrawAll():               #destroys and redraws the board based on called matrix data (nextGeneration function)
    for item in App().spritelist[:]:
        item.destroy()
        
    #creating graphics

    Sprite(button,(0,420))               #the next generation button
    Sprite(button,(110,420))             #the glider button
    Sprite(button,(220,420))             #the plus button
    Sprite(nextGen,(10,430))
    Sprite(glider,(135,430))
    Sprite(plus,(250,430))
    
    nextGeneration()

    for e in range (0,WIDTH//40):               #checks each column
        for i in range (0,HEIGHT//40):          #checks each row
            if data["matrix"][i][e] == 0:
                Sprite(deadCell,((40*e),(40*i)))                    #sprites based on matrix
            elif data["matrix"][i][e] == 1:
                Sprite(liveCell,((40*e),(40*i)))

    data["generation"]+=1
    print("Generation",data["generation"],"is complete")

    
def nextGeneration():                   #changes matrix based on each cell's surroundings

    newMatrix = buildBoard()
#THIS IS THE IMPORTANT PART WHERE THE PROGRAM DECIDES WHAT LIVES AND WHAT DIES

    for e in range (0,WIDTH//40):               #checks each column
        for i in range (0,HEIGHT//40):          #checks each row
            if data["matrix"][i][e] == 0 and numNeighbors(i,e)==3:  #if it's dead and has 3 neigbors it comes alive
                newMatrix[i][e] = 1
            elif data["matrix"][i][e] == 1 and numNeighbors(i,e)>3 or numNeighbors(i,e)<2: #if it's alive and has fewer than 2 or more than 3 neigbors it dies
                newMatrix[i][e] = 0
            elif data["matrix"][i][e] == 1 and numNeighbors(i,e)==2 or numNeighbors(i,e)==3: #if it's already alive and has either 2 or 3 neighbors it lives on
                newMatrix[i][e] = 1
    data["matrix"] = newMatrix
    return data["matrix"]
    
    
def numNeighbors(row,col):            #returns the number of living cells around the cell with given coordinates
    
    num = 0

    if row!=0 and data["matrix"][row-1][col] == 1:       #tests above
        num+=1
    if row!=9 and data["matrix"][row+1][col] == 1:       #tests below
        num+=1
    if col!=0 and data["matrix"][row][col-1] == 1:       #tests left
        num+=1
    if col!=9 and data["matrix"][row][col+1] == 1:       #tests right
        num+=1
    if row!= 0 and col!=0 and data["matrix"][row-1][col-1] == 1:       #tests above left
        num+=1
    if row!= 9 and col!=9 and data["matrix"][row+1][col+1] == 1:       #tests below right
        num+=1
    if row!= 9 and col!=0 and data["matrix"][row+1][col-1] == 1:       #tests below left
        num+=1
    if row!= 0 and col!=9 and data["matrix"][row-1][col+1] == 1:       #tests above right
        num+=1

    return num


if __name__ == '__main__':

    data = {}
    data["matrix"] = buildBoard()
    data["generation"] = -1

    black = Color(0x000000,0.25)
    fullblack = Color(0x000000,1)
    red = Color(0xFF0000,1)
    yellow = Color(0xFFFF00,0.5)
    
    
    HEIGHT = 400
    WIDTH = 400
    
    liveCell = RectangleAsset(40,40,LineStyle(0,fullblack),fullblack)
    deadCell = RectangleAsset(40,40,LineStyle(1,black),yellow)
    
    
    #button sprites
    button = RectangleAsset(100,40,LineStyle(2,black),red)
    nextGen = TextAsset("Next Gen", fill=fullblack, style='bold 15pt Times')
    glider = TextAsset("Glider", fill=fullblack, style='bold 15pt Times')
    plus = TextAsset("Plus", fill=fullblack, style='bold 15pt Times')
    
    redrawAll()
    

    App().listenMouseEvent("click",mouseClick)
    App().listenKeyEvent('keydown','space', space)
    App().run()
