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
    
def numNeighbors(row,col):              #THIS ONLY TESTS INDEXING RIGHT NOW
    if board[row-1][col-1] == 0:
        print ("this square is DEAD")

def mouseClick(event):
    row = (mouseClick.y//40)            #senses click in horizontal gridlines with 40 spacing
    col = (mouseClick.x//40)                #senses click in vertical gridlines with 40 spacing


if __name__ == '__main__':

    buildBoard()


    #graphics
    
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
    
    
    App().listenMouseEvent("click",mouseClick)
    App().run()
    
