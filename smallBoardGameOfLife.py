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
        data["matrix"][row][col] = 1         #reverses status in matrix

    elif 0<= event.x <=400 and 0<=event.y<=400 and data["matrix"][row][col] == 1:
        Sprite(deadCell,(event.x-(event.x%40),event.y-(event.y%40)))
        data["matrix"][row][col] = 0           #reverses status in matrix
        
    elif 0<= event.x <=100 and 420<=event.y<=480:          #nextGen button
        redrawAll()
        
    elif 110<= event.x <=210 and 420<=event.y<=480:          #run button DOESN'T WORK WELL YET
        runContinuous()


def space(event):               #does the same thing as the next gen button but uses the spacebar
    redrawAll()


def runContinuous():                #runs the program at step intervals
    App().run(runContinuous)
    data["steps"] += 1
    if data["steps"]%500 == 0:
        redrawAll()

def redrawAll():                            #redraws the board based on matrix data
    for item in App().spritelist[:]:
        item.destroy()
        
    #creating graphics

    button = RectangleAsset(100,40,LineStyle(2,black),red)
    nextGen = TextAsset("Next Gen", fill=fullblack, style='bold 15pt Times')
    run = TextAsset("Run", fill=fullblack, style='bold 15pt Times')
    Sprite(button,(0,420))               #the next generation button
    Sprite(button,(110,420))             #the run button
    Sprite(nextGen,(10,430))
    Sprite(run,(140,430))
    
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
            if data["matrix"][i][e] == 0 and numNeighbors(i,e)==3:
                newMatrix[i][e] = 1
            elif data["matrix"][i][e] == 1 and numNeighbors(i,e)>3 or numNeighbors(i,e)<2:
                newMatrix[i][e] = 0
            elif data["matrix"][i][e] == 1 and numNeighbors(i,e)==2 or numNeighbors(i,e)==3:
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
    if row!= 0 and col!=0 and data["matrix"][row-1][col-1] == 1:       #tests top left
        num+=1
    if row!= 9 and col!=9 and data["matrix"][row+1][col+1] == 1:       #tests bottom right
        num+=1
    if row!= 9 and col!=0 and data["matrix"][row+1][col-1] == 1:       #tests bottom left
        num+=1
    if row!= 0 and col!=9 and data["matrix"][row-1][col+1] == 1:       #tests top right
        num+=1

    return num


if __name__ == '__main__':

    data = {}
    data["matrix"] = buildBoard()
    data["steps"] = 0
    data["generation"] = -1

    black = Color(0x000000,0.25)
    fullblack = Color(0x000000,1)
    red = Color(0xFF0000,1)
    yellow = Color(0xFFFF00,0.25)
    
    
    HEIGHT = 400
    WIDTH = 400
    
    liveCell = RectangleAsset(40,40,LineStyle(0,fullblack),fullblack)
    deadCell = RectangleAsset(40,40,LineStyle(1,black),yellow)
    
    
    redrawAll()
    

    App().listenMouseEvent("click",mouseClick)
    App().listenKeyEvent('keydown','space', space)
    App().run()