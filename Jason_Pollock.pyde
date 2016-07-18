from random import *



def setup(): 
    size(500, 500)
    background(255,255,255)
    
def draw():
    noStroke()
    redColor = randint(0, 255)
    greenColor = randint(0, 255)
    blueColor = randint(0, 255)
    
    ellipse(mouseX, mouseY, 55, 55)
    ellipse(mouseX + 50, mouseY, 25, 25)
    ellipse(mouseX, mouseY + 50, 25, 25)
    ellipse(mouseX - 50, mouseY, 25, 25)
    ellipse(mouseX, mouseY - 50, 25, 25)
    ellipse(mouseX + 50, mouseY + 50, 25, 25)
    ellipse(mouseX - 50, mouseY - 50, 25, 25)
    ellipse(mouseX + 50, mouseY - 50, 25, 25)
    ellipse(mouseX - 50, mouseY + 50, 25, 25)
    fill(redColor, blueColor, greenColor)