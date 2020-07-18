from Tkinter import *

def mousePressed(event, data):
    if (data.height/3 - 75) <= event.y <= (data.height/3 + 75):
        if (data.width/4 -75) <= event.x <= (data.width/4 + 75):
            data.background = data.cityBG
            data.BGoutlineY = (data.height/3 - 75)
            data.BGoutlineX = (data.width/4 -75)
        elif (3*data.width/4 - 75) <= event.x <= (3*data.width/4 + 75):
            data.background = data.forestBG
            data.BGoutlineX = (3*data.width/4 - 75)
            data.BGoutlineY = (data.height/3 - 75)
    elif (2*data.height/3 - 75) <= event.y <= (2*data.height/3 + 75):
        if (data.width/4 - 75) <= event.x <= (data.width/4 + 75):
            data.background = data.playgrounfBG
            data.BGoutlineX = (data.width/4 - 75)
            data.BGoutlineY = (2*data.height/3 - 75)
        elif (3*data.width/4 - 75) <= event.x <= (3*data.width/4 + 75):
            data.background = data.underwaterBG
            data.BGoutlineX = (3*data.width/4 - 75)
            data.BGoutlineY = (2*data.height/3 - 75)
    elif (data.width/2 - 52.5) <= event.x <= (data.width/2 +52.5):
        if (9*data.height/10 - 26) <= event.y <= (9*data.height/10 + 26):
            data.mode = 'music'

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.curtains)
    canvas.create_image(data.width/2, data.height/10, image = data.bgText)
    canvas.create_image(data.width/4, data.height/3, image = data.cityTN)
    canvas.create_text(data.width/4, data.height/3 + 95, text = "City", 
                       font = "Arial 20 bold", fill = 'white')
    canvas.create_image(3*data.width/4, data.height/3, image = data.forestTN)
    canvas.create_text(3*data.width/4, data.height/3 + 95, text = "Field", 
                       font = "Arial 20 bold", fill = 'white')
    canvas.create_image(data.width/4, 2*data.height/3,image = data.playgroundTN)
    canvas.create_text(data.width/4, 2*data.height/3 + 95, text = "Playground",
                       font = "Arial 20 bold", fill = 'white')
    canvas.create_image(3*data.width/4, 2*data.height/3, image = data.underwaterTN)
    canvas.create_text(3*data.width/4, 2*data.height/3 + 95, text = 'Underwater',
                        font = "Arial 20 bold", fill = 'white')
    if data.BGoutlineX != 0 and data.BGoutlineY != 0:
        canvas.create_rectangle(data.BGoutlineX, data.BGoutlineY, 
                                data.BGoutlineX + 150, data.BGoutlineY + 150, 
                                outline = 'white', width = 5)
    canvas.create_image(data.width/2, 9*data.height/10, image = data.next)
    