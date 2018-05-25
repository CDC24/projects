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


def buildBoard():    #sprites a 13 x 25 matrix of zeroes(dead squares)
    board = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    return (board)

def redrawAll():
    for item in App().spritelist[:]:
        item.destroy()
    #creating graphics
    
    black = Color(0x000000,0.25)
    red = Color(0xFF0000,1)
    yellow = Color(0xFFFF00,0.25)
    
    #setting up board
    
    HEIGHT = 520
    WIDTH = 1000
    
    
    vertBoardLine = RectangleAsset(2,HEIGHT,LineStyle(0,black),black)
    horizBoardLine = RectangleAsset(WIDTH,2,LineStyle(0,black),black)
    boardBox = RectangleAsset(WIDTH,HEIGHT,LineStyle(1,yellow),yellow)
    
    
    
    # these sprite the grid
    Sprite(boardBox)
    for i in range (0,HEIGHT//40):              #sprites horizontal gridlines with 40 spacing
        Sprite(horizBoardLine,(0,(40*i)))
    for i in range (0,WIDTH//40):               #sprites vertical gridlines with 40 spacing
        Sprite(vertBoardLine,((40*i),0))
    
def numNeighbors(row,col): 
    return
            

def mouseClick(event):
    row = (int(event.y//40))           #senses click in horizontal gridlines with 40 spacing
    col = (int(event.x//40))           #senses click in vertical gridlines with 40 spacing
    for i in range(0,13):
        if row == i:
            for i in range (0,25):
                if col == i:
                    print ("You just clicked in row",row,"and column",col)
    liveCell = RectangleAsset(40,40,LineStyle(0,black),black)
    Sprite(liveCell,(event.x,event.y))


if __name__ == '__main__':

    data = {}
    data["matrix"] = buildBoard()

    redrawAll()


    

    App().listenMouseEvent("click",mouseClick)
    App().run()
