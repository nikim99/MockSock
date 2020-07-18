from Tkinter import *

def mousePressed(event, data):
    if (data.width/2 - 50) <= event.x <= (data.width/2 + 50):
        if (9*data.height/10 - 26) <= event.y <= (9*data.height/10 + 26):
            data.mode = 'cust'

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.curtains)
    #Instructions
    canvas.create_image(data.width/2, data.height/10, image = data.instructions)
    canvas.create_text(data.width/2, 2*data.height/11, 
                       text = "1. Pick one or two puppet", font = "Arial 17 bold", 
                       fill = "white")
    canvas.create_text(data.width/2, 3*data.height/11, 
                       text = "2. Pick a background", font = "Arial 17 bold", 
                       fill = "white")
    canvas.create_text(data.width/2, 4*data.height/11, 
                       text = "3. Pick background music", 
                       font = "Arial 17 bold", fill = "white")
    canvas.create_text(data.width/2, 5*data.height/11, 
                       text = "3. Pick any props you want", 
                       font = "Arial 17 bold", fill = "white")
    canvas.create_text(data.width/2, 6*data.height/11, 
                       text = "4. Place your hand in front of the sensor", 
                       font = "Arial 17 bold", fill = "white")
    canvas.create_text(data.width/2, 7*data.height/11, 
                       text = "in a sock puppet shape", 
                       font = "Arial 17 bold", fill = "white")                  
    canvas.create_text(data.width/2, 8*data.height/11, 
                       text = "5. Interact with props", font = "Arial 17 bold",
                       fill = "white")
    canvas.create_text(data.width/2, 9*data.height/11, 
                       text = "6. Make cool shows with your puppets!", 
                       font = "Arial 17 bold", fill = "white")
    #Play button
    canvas.create_image(data.width/2, 10*data.height/11, image = data.play)