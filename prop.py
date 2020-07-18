from Tkinter import *
import thread
from thread import start_new_thread
import audiosample
import music


def mousePressed(event, data):
    if (data.height/3 - 30) <= event.y <= (data.height/3 + 30):
        if (data.width/3 - 30) <= event.x <= (data.width/3 + 30):
            data.propOutlineY = (data.height/3 - 30)
            data.propOutlineX = (data.width/3 - 30)
            data.prop = 'ball'
        elif (2*data.width/3 - 30) <= event.x <= (2*data.width/3 + 30):
            data.propOutlineY = (data.height/3 - 30)
            data.propOutlineX = (2*data.width/3 - 30)
            data.prop = 'apple'
    elif (2*data.height/3 - 33) <= event.y <= (2*data.height/3 + 33):
        if (data.width/2 - 62.5) <= event.x <= (data.width/2 + 62.5):
            data.propOutlineY = (2*data.height/3 - 33)
            data.propOutlineX = (data.width/2 - 62.5)
            data.prop = 'car'
    elif (data.width/2 - 50) <= event.x <= (data.width/2 + 50):
        if (9*data.height/10 - 26) <= event.y <= (9*data.height/10 + 26):
            data.playMusic = True
            music.playMusic(data)
            data.mode = 'theatre'
    

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.curtains)
    canvas.create_image(data.width/2, data.height/10, image = data.propText)
    canvas.create_image(data.width/3, data.height/3, image = data.ball)
    canvas.create_text(data.width/3, data.height/3 + 60, text = "Ball", 
                        font = "Arial 20 bold", fill = 'white')
    canvas.create_image(2*data.width/3, data.height/3, image = data.apple)
    canvas.create_text(2*data.width/3, data.height/3 + 60, text = 'Apple', 
                        font = 'Arial 20 bold', fill = 'white')
    canvas.create_image(data.width/2, 2*data.height/3, image = data.car)
    canvas.create_text(data.width/2, 2*data.height/3 + 50, text = 'Toy Car', 
                        font = "Arial 20 bold", fill = "white")
    if data.propOutlineX != 0 and data.propOutlineY != 0:
        if data.prop == 'car':
            canvas.create_rectangle(data.propOutlineX, data.propOutlineY, 
                                    data.propOutlineX + 125, data.propOutlineY + 66, 
                                    outline = 'white', width = 5)
        else:
            canvas.create_rectangle(data.propOutlineX, data.propOutlineY, 
                                    data.propOutlineX + 60, data.propOutlineY + 60, 
                                    outline = 'white', width = 5)
    canvas.create_image(data.width/2, 9*data.height/10, image = data.play)