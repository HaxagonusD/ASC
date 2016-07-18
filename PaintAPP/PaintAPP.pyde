def setup():
    size(500,500)
    background(255,255,255)
    
firstColor = 0
secondColor = 153
value = 0 
def draw():
    noStroke() 
    rect(0,0,100,100)
    fill(0)
    rect(100,0,100,100)
    fill(153)

        
        
        
    
def mousePressed(): 
    global firstColor
    noStroke()
    if 0 < mouseX < 100 and 0 < mouseY < 100: 
        firstColor = 0 
    
    ellipse(mouseX,mouseY, 10,10)