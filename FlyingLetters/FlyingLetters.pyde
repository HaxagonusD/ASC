from random import *
import time


#our list of letters
letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
letterList2 = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

score = 0 


#increasing x value
increasingX = 0
increasingX2 = 0

randomLetter = letterList[randint(0,25)]
randomLetter2 = letterList2[randint(0,25)]
positionY = randint(50,450)
positionY2 = randint(50,450)


value = 0 

def setup():
    size(750,500)
    background(255,255,255)


#draws random letter and makes it move
def draw():
    
    global randomLetter
    global increasingX
    global positionY
    global value 
    global score
    global increasingX2
    global positionY2

    
 
    fill(value, 255,255)
    background(255,255,255)
    textSize(100)
    text(randomLetter, increasingX ,positionY)
   
    fill(0, 255,255)
    textSize(50)
    text("score:",0,30)
    fill(0, 255,255)
    text(score, 150,35)
    if increasingX > 200:
        textSize(100)
        fill(0, 255,255)
        text(randomLetter2, increasingX2,positionY2)
        increasingX2 +=1
    
        
    
    if increasingX > 600 or increasingX2 > 600 : 
        background(0) 
        textSize(100)
        fill(255,0,0)
        text("YOU LOSE", 150,250)
    else:
        increasingX += 1
    

        
def keyPressed():
    global value
    global increasingX
    global randomLetter
    global randomLetter2 
    global positionY
    global score 
    global increasingX2
    global positionY2
    
    
    
    if key == randomLetter:
        value = 255
        increasingX = 0

        randomLetter = letterList[randint(0,25)]

        positionY = randint(100,300)
        value = 0
        score += 1 
    elif key == randomLetter2:
        value = 255
        increasingX2 = 0

        randomLetter2 = letterList[randint(0,25)]

        positionY2 = randint(100,300)
    
         
        value=0
        score+=1

         
    
    
    
    

    