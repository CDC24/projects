#Caleb Callaway
#5/23/18
#gameOfLife.py - Conway's Game of Life

from ggame import *

"""
Rules:
Any live cell with fewer than two live neighbors dies, as if by under population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by overpopulation.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""


def buildBoard():    #creates a 12 x 25 matrix of zeroes(dead squares)
    board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    return (board)


def mouseClick(event):
    row = (int(event.y//40))           #senses click in horizontal gridlines with 40 spacing
    col = (int(event.x//40))           #senses click in vertical gridlines with 40 spacing
    
    if 0<= event.x <=1000 and 0<=event.y<=480 and data["matrix"][row][col] == 0:
        Sprite(liveCell,(event.x-(event.x%40),event.y-(event.y%40)))
        data["matrix"][row][col] = 1         #reverses status in matrix

    elif 0<= event.x <=1000 and 0<=event.y<=480 and data["matrix"][row][col] == 1:
        Sprite(deadCell,(event.x-(event.x%40),event.y-(event.y%40)))
        data["matrix"][row][col] = 0           #reverses status in matrix
        
    if 0<= event.x <=80 and 480<=event.y<=520:          #nextGen button
        redrawAll()
        
    if 110<= event.x <=210 and 480<=event.y<=520:          #run button
        runContinuous()


def runContinuous():
    App().run(runContinuous)
    data["steps"] += 1
    if data["steps"]%300 == 0:
        redrawAll()

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    #creating graphics
    

    button = RectangleAsset(100,40,LineStyle(2,black),red)  #the next generation button
    nextGen = TextAsset("Next Gen", fill=fullblack, style='bold 15pt Times')
    run = TextAsset("Run", fill=fullblack, style='bold 15pt Times')
    Sprite(button,(0,480))
    Sprite(button,(110,480))
    Sprite(nextGen,(10,490))
    Sprite(run,(140,490))
    
    nextGeneration()

    for e in range (0,WIDTH//40):               #checks each column
        for i in range (0,HEIGHT//40):          #checks each row
            if data["matrix"][i][e] == 0:
                Sprite(deadCell,((40*e),(40*i)))                    #sprites based on matrix
            if data["matrix"][i][e] == 1:
                Sprite(liveCell,((40*e),(40*i)))

    print("next gen is complete")

    
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
    
    
def numNeighbors(row,col): 
    
    num = 0

    if row!=0 and data["matrix"][row-1][col] == 1:       #tests above
        num+=1
    if row!=11 and data["matrix"][row+1][col] == 1:       #tests below
        num+=1
    if col!=0 and data["matrix"][row][col-1] == 1:       #tests left
        num+=1
    if col!=24 and data["matrix"][row][col+1] == 1:       #tests right
        num+=1
    if row!= 0 and col!=0 and data["matrix"][row-1][col-1] == 1:       #tests top left
        num+=1
    if row!= 11 and col!=24 and data["matrix"][row+1][col+1] == 1:       #tests bottom right
        num+=1
    if row!= 11 and col!=0 and data["matrix"][row+1][col-1] == 1:       #tests bottom left
        num+=1
    if row!= 0 and col!=24 and data["matrix"][row-1][col+1] == 1:       #tests top right
        num+=1


    return num


if __name__ == '__main__':

    data = {}
    data["matrix"] = buildBoard()
    data["steps"] = 0

    blue = Color(0x0000FF,1)
    black = Color(0x000000,0.25)
    fullblack = Color(0x000000,1)
    red = Color(0xFF0000,1)
    yellow = Color(0xFFFF00,0.25)
    
    
    HEIGHT = 480
    WIDTH = 1000
    
    liveCell = RectangleAsset(40,40,LineStyle(0,fullblack),fullblack)
    deadCell = RectangleAsset(40,40,LineStyle(1,black),yellow)
    
    #runnning the functions
    
    """
    for e in range (0,WIDTH//40):
        for i in range (0,HEIGHT//40):
                Sprite(deadCell,((40*e),(40*i))) #sprites initial dead cell grid
    """

    redrawAll()
    

    App().listenMouseEvent("click",mouseClick)
    App().run()
