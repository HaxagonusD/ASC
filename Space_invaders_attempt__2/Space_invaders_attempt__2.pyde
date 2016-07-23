matrix  = [[0]*5 for i in range(5)]

bulletList = []

shipX = 0
bulletX = 25
bulletY = 0
bulletY2 = 0
xAdd = 10
state = False
spaceCounter = 0 
middle = 250
bottom = 550

def setup():
    size(500, 600)
    background(0)            

def draw():
    global shipX,bulletX,bulletY,xAdd,state,middle,bottom,bulletY
    background(0)
    for x in range(len(matrix)):
        for y in range(len(matrix[i])):
            if matrix[x][y] == 0:
                fill(255)
                rect(x*100+25,y*100,50,50)
                
    rect(middle + shipX,bottom,50,25)
    if state == True :
        bulletY -= 1 
    if keyPressed:
        
        if key == " " or key == "a" or key == "d":
            if key == " ":
                fill(255)
                ellipse(middle + bulletX,bottom + bulletY,25,25)
                state = True 
                xAdd = 0 
          
        
                
             
            if key == "a" and state == True:
                fill(255)
                ellipse(middle + bulletX,bottom + bulletY,25,25)
            
                xAdd = 0
            if key == "d" and state == True:
                fill(255)
                ellipse(middle + bulletX,bottom + bulletY,25,25)
        
                xAdd = 0
            
                
                
                
                
   
def keyPressed():
    global shipX,bulletX,xAdd
    if key == "a":
        shipX -= 10
        bulletX -= xAdd
        
    if key == "d" :
        shipX += 10
        bulletX += xAdd