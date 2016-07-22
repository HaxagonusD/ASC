from random import *

board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
ship = 2
board[randint(0,4)][randint(0,4)] = ship

counter = 0



print(board)
def setup():
    size(500,500)
    background(255)
    global board 
################################################################################################################################

    for i in range(len(board)):                  #This says "for every item in the list [0,1,2,3,4] do the next line
        for item in range(len(board[i])):        #Repeat
            if (board[i][item] == 0 or 2 ):      #Looks for possible rectanglees in our board list 
                fill(255)
                rect(i*100, item*100, 100, 100)  #Draws rectangles in every possible x and y coordinates with a multiple of 100

################################################################################################################################

def draw():

    global counter
    
    if mousePressed:
        if board[(mouseX//100)][(mouseY//100)] == 2:
            fill(0,255,0)
            rect((mouseX//100)*100 ,(mouseY//100)*100, 100,100)
        if counter == 5:
            background(0,0,255)
            fill(255,0,0)
            text("You lose", 200,200)
        
        else:
            fill(0)
            rect((mouseX//100)*100 ,(mouseY//100)*100, 100,100)
            counter+=1 
        
""" 
Essentially, these two formulas take where the mouse clicked and divides those coordinats by 100 and returns and integer without the decimal tail then it multiplies that number by 100 to get accurate coordinates for where to draw the rectangle 
"""


#This program is incomplete
#This program needs to have a counter that can only let you guess 5 times and it needs to display the correct message when you run out of guesses or when you find the ship.