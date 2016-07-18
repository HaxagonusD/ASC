from Myro import *

darkBlue = makeColor(0,51,76)

red = makeColor(217, 26, 33)

blue = makeColor(112,150,158)

yellow = makeColor(252, 227, 166)

pic = makePicture(pickAFile())
show(pic)

for pixel in getPixels(pic):
    gray = getGray(pixel)
    if gray > 180:
        setColor(pixel, yellow)
    elif 120 < gray < 180: 
        setColor(pixel, blue)
    elif 60 < gray < 120:
        setColor(pixel, red)
    else:
        setColor(pixel, darkBlue)
        
show(pic)

