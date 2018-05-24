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


def buildBoard():               
    board = [[][][][][][][][][][][][][][][][][][][][]]
    for row in board:
        for i in range (0, 20):
            board[i-1].append(i)
    print (board)

    


if __name__ == '__main__':

    #graphics
    
    black = Color(0x000000,0.25)
    red = Color(0xFF0000,1)
    yellow = Color(0xFFFF00,0.25)
    
    #setting up board
    
    HEIGHT = 500
    WIDTH = 1000
    
    
    vertBoardLine = RectangleAsset(2,HEIGHT,LineStyle(0,black),black)
    horizBoardLine = RectangleAsset(WIDTH,2,LineStyle(0,black),black)
    boardBox = RectangleAsset(WIDTH,HEIGHT,LineStyle(1,yellow),yellow)
    
    
    
    # these sprite the grid
    Sprite(boardBox)
    for i in range (0,HEIGHT//20):              #sprites horizontal gridlines with 20 spacing
        Sprite(horizBoardLine,(0,(20*i)))
    for i in range (0,WIDTH//20):               #sprites vertical gridlines with 20 spacing
        Sprite(vertBoardLine,((20*i),0))
    
    
    
    #App().listenMouseEvent("click",mouseClick)
    App().run()
    
