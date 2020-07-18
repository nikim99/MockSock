
from Tkinter import *
import thread
from thread import start_new_thread
import playAudio

def mousePressed(event, data):
    if (data.height/3 - 44.5) <= event.y <= (data.height/3 + 44.5):
        if (data.width/3 - 50) <= event.x <= (data.width/3 + 50):
            data.music = 1
            data.musicOutlineY = data.height/3 - 44.5
            data.musicOutlineX = data.width/3 - 50
            data.playMusic = not data.playMusic
            playMusic(data)
        elif (2*data.width/3 - 50) <= event.x <= (2*data.width/3 + 50):
            data.music = 2
            data.musicOutlineY = data.height/3 - 44.5
            data.musicOutlineX = 2*data.width/3 - 50
            data.playMusic = not data.playMusic
            playMusic(data)
    elif (2*data.height/3 - 44.5) <= event.y <= (2*data.height/3 + 44.5):
        if (data.width/3 - 50) <= event.x <= (data.width/3 + 50):
            data.music = 3
            data.musicOutlineY = 2*data.height/3 - 44.5
            data.musicOutlineX = data.width/3 - 50
            data.playMusic = not data.playMusic
            playMusic(data)
        elif (2*data.width/3 - 50) <= event.x <= (2*data.width/3 + 50):
            data.music = 4
            data.musicOutlineY = 2*data.height/3 - 44.5
            data.musicOutlineX = 2*data.width/3 - 50
            data.playMusic = not data.playMusic
            playMusic(data)
    elif (9*data.height/10 - 26) <= event.y <= (9*data.height/10 + 26):
        if (data.width/2 - 52.5) <= event.x <= (data.width/2 + 52.5):
            data.mode = 'prop'
            data.playMusic = False
            playMusic(data)

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.curtains)
    canvas.create_image(data.width/2, data.height/10, image = data.musicText)
    # Music buttons
    canvas.create_image(data.width/3, data.height/3, image = data.playButton)
    canvas.create_text(data.width/3, data.height/3 + 70, text = 'Music Box', font = 'Arial 20 bold', fill = 'white')
    canvas.create_image(2*data.width/3, data.height/3, image = data.playButton)
    canvas.create_text(2*data.width/3, data.height/3 + 70, text = 'Happy', font = 'Arial 20 bold', fill = 'white')
    canvas.create_image(data.width/3, 2*data.height/3, image = data.playButton)
    canvas.create_text(data.width/3, 2*data.height/3 + 70, text = 'Magical', font = 'Arial 20 bold', fill = 'white')
    canvas.create_image(2*data.width/3, 2*data.height/3, image = data.playButton)
    canvas.create_text(2*data.width/3, 2*data.height/3 + 70, text = 'Electronic', font = 'Arial 20 bold', fill = 'white')
    if data.musicOutlineX != 0 and data.musicOutlineY != 0:
        canvas.create_rectangle(data.musicOutlineX, data.musicOutlineY, data.musicOutlineX + 100, data.musicOutlineY + 89, outline = 'white', width = 5)
    canvas.create_image(data.width/2, 9*data.height/10, image = data.next)

def playMusic(data):
    if data.playMusic == True:
        if data.music == 1:
            start_new_thread(audiosample.play, (data.music1, data))
        elif data.music == 2:
            start_new_thread(audiosample.play, (data.music2, data))
        elif data.music == 3:
            start_new_thread(audiosample.play, (data.music3, data))
        elif data.music == 4:
            start_new_thread(audiosample.play, (data.music4, data))
