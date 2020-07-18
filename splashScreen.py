from Tkinter import *

def mousePressed(event, data):
    if (2*data.height/3 -26) <= event.y <= (2*data.height/3 + 26):
        if (data.width/3 - 50) <= event.x <= (data.width/3 + 50):  
            data.mode = 'cust'
    elif (4*data.height/5 - 26) <= event.y <= (4*data.height/5 + 26):
        if (data.width/3 - 52.5) <= event.x <= (data.width/3 + 52.5):
            data.mode = 'help'

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.theatre)
    canvas.create_image(5*data.width/8 + 25, 2*data.height/6 - 60, image = data.mock)
    canvas.create_image(5*data.width/8 + 25, 2*data.height/6 + 60, 
                        image = data.sockImage)
    canvas.create_image(270/2, 150, image = data.sockPuppet2)
    canvas.create_image(data.width-150, data.height- (255/2), 
                        image = data.sockPuppet1)
    canvas.create_image(data.width/3, 2*data.height/3, image = data.play)
    canvas.create_image(data.width/3, 4*data.height/5, image = data.help)