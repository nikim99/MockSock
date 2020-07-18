from Tkinter import *

import sys, thread
sys.path.insert(0,"C:\Users\Saritha\Documents\CMU/112\TermProject\LeapDeveloperKit_2.3.1+31549_win\LeapSDK\lib/x86")
import Leap
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
from shapely.geometry import Polygon, Point
import math
import loadImages
import splashScreen
import helpScreen
import cust
import cust2
import bg
import prop
import theatre
import music
from thread import start_new_thread
# audio sample file from 112 website
import audiosample


def init(data):
    data.controller = Leap.Controller()
    data.frame = data.controller.frame()
    data.fingerNames = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    data.boneNames = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    data.mode = "splashScreen"
    loadImages.loadImages(data)
    data.color = 'gray'
    data.outlineX = 0
    data.outlineY = 0
    data.BGoutlineX = 0
    data.BGoutlineY = 0
    data.propOutlineX = 0
    data.propOutlineY = 0
    data.background = None
    data.prop = None
    data.ballCenterX = data.width/2
    data.ballCenterY = 50
    data.down = True
    data.accessory = None
    data.accOutlineX = 0
    data.accOutlineY = 0
    data.sock2 = False
    data.color2 = 'gray'
    data.accessory2 = None
    data.appleState = 0
    data.appleStates = [data.apple, data.apple1, data.apple2, data.apple3, data.apple4, None]
    data.appleCenterX = data.width - 100
    data.appleCenterY = data.height/2 + 25
    data.energy = 6000
    data.carCenterX = data.width/2
    data.velocity = 0
    data.linePoints = []
    data.linePoints2 = []
    data.b1 = 'up'
    data.xold, data.yold = None, None
    data.wrongShape = False
    # Music from http://www.orangefreesounds.com
    data.music = None
    data.playMusic = False
    data.music1 = 'Music/Fur-elise-music-box.wav'
    data.music2 = 'Music/Happy-electronic-music.wav'
    data.music3 = 'Music/Magical-path-melodic-upbeat-electronic-music.wav'
    data.music4 = 'Music/Short-electronic-background-music.wav'
    data.musicOutlineX = 0
    data.musicOutlineY = 0
    
def collisionCheck(data, sock, prop):
    sockPuppet = Polygon(sock)
    if data.prop == 'car':
        cx, cy = prop
        propShape = Polygon([(cx - 57, cy - 33), (cx - 57, cy + 33), (cx + 57, cy + 33), (cx + 57, cy - 33)])
    else:
        cx, cy, r  = prop
        angle = 0
        points = []
        while math.radians(angle) < (2*math.pi):
            x = cx + r*math.cos(math.radians(angle))
            y = cy + r*math.sin(math.radians(angle))
            points += [(x, y)]
            angle += 30
        propShape = Polygon(points)
    return sockPuppet.intersects(propShape)

def biteGesture(data):
    return data.frame.hands[0].pinch_strength > .9 or data.frame.hands[1].pinch_strength > .9

# Line drawing functions (b1down, b1up, motion) from https://svn.python.org/projects/python/trunk/Demo/tkinter/guido/paint.py
# Slightly changed functions to fit to code structure

def b1down(event, data):
    data.b1 = 'down'

def b1up(event, data):
    data.b1 = 'up'
    data.xold = None
    data.yold = None

def motion(event, data):
    if data.b1 == 'down':
        if data.mode == 'cust':
            if data.xold != None and data.yold != None: 
                if (3*data.width/10 - 25) <= event.x <= (4*data.width/10 + 5):
                    if (3*data.height/4 - 40) <= event.y <= (3*data.height/4 + 40):
                        data.linePoints += [data.xold, data.yold, event.x, event.y]
        elif data.mode == 'cust2':
            if data.xold != None and data.yold != None: 
                if (3*data.width/10 - 25) <= event.x <= (4*data.width/10 + 5):
                    if (3*data.height/4 - 40) <= event.y <= (3*data.height/4 + 40):
                        data.linePoints2 += [data.xold, data.yold, event.x, event.y]
        data.xold = event.x
        data.yold = event.y

def mousePressed(event, data):
    if data.mode == 'splashScreen':
        splashScreen.mousePressed(event, data)
    elif data.mode == 'theatre':
        theatre.mousePressed(event, data)
    elif data.mode == 'help':
        helpScreen.mousePressed(event, data)
    elif data.mode == 'cust':
        cust.mousePressed(event, data)
    elif data.mode == 'cust2':
        cust2.mousePressed(event, data) 
    elif data.mode == 'bg':
        bg.mousePressed(event, data)
    elif data.mode == 'prop':
        prop.mousePressed(event, data)
    elif data.mode == 'music':
        music.mousePressed(event, data)


def keyPressed(event, data):
    if data.mode == 'splashScreen':
        splashScreen.keyPressed(event, data)
    elif data.mode == 'theatre':
        theatre.keyPressed(event, data)
    elif data.mode == 'help':
        helpScreen.keyPressed(event, data)
    elif data.mode == "cust":
        cust.keyPressed(event, data)
    elif data.mode == "cust2":
        cust2.keyPressed(event, data)
    elif data.mode == 'bg':
        bg.keyPressed(event, data)
    elif data.mode == 'prop':
        prop.keyPressed(event, data)
    elif data.mode == 'music':
        music.keyPressed(event, data)

def ballCollisionCheck(data):
    if theatre.getPointsList(data, 0) != None:
        x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, \
                            z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8 =  theatre.sockCoordinates(data, 0)
        leftSock =[(x10, z10), (x12, z12), (x3, z3), (x7, z7), (x8, z8), (x1, z1)]
        rightSock = [(x1, z1), (x5, z5), (x16, z16), (x14, z14), (x15, z15), (x17, z17), (x13, z13), (x11, 
                            z11)]
        propShape = [data.ballCenterX, data.ballCenterY, 30]
        leftCollision = collisionCheck(data, leftSock, propShape)
        rightCollision = collisionCheck(data, rightSock, propShape)
        velocity = data.frame.hands[0].palm_velocity.x
        if data.frame.hands[0].is_left:
            if leftCollision == True:
                data.velocity = -velocity
            elif rightCollision == True:
                data.velocity = velocity
        else:
            if rightCollision == True:
                data.velocity = -velocity
            elif leftCollision == True:
                data.velocity = velocity
    if data.sock2 == True and theatre.getPointsList(data, 1) != None:
        a1, b1, a5, b5, a16, b16, a14, b14, a15, b15, a17, b17, a13, b13, a11, \
                            b11, a10, b10, a12, b12, a3, b3, a7, b7, a8, b8 =  theatre.sockCoordinates(data, 1)
        leftSock2 =[(a10, b10), (a12, b12), (a3, b3), (a7, b7), (a8, b8), (a1, b1)]
        rightSock2 = [(a1, b1), (a5, b5), (a16, b16), (a14, b14), (a15, b15), (a17, b17), (a13, b13), (a11, 
                            b11)]
        leftCollision2 = collisionCheck(data, leftSock2, propShape)
        rightCollision2 = collisionCheck(data, rightSock2, propShape)
        velocity2 = data.frame.hands[1].palm_velocity.x/2
        if data.frame.hands[1].is_left:
            if leftCollision2 == True:
                data.ballCenterX -= 10
                if (data.ballCenterX - 35)< 0:
                    data.ballCenterX = 35
            elif rightCollision2 == True:
                data.ballCenterX += 10
                if (data.ballCenterX + 35) > data.width:
                    data.ballCenterX = data.width-35
        else:
            if rightCollision2 == True:
                data.ballCenterX -= 10
                if (data.ballCenterX - 35)< 0:
                    data.ballCenterX = 35
            elif leftCollision2 == True:
                data.ballCenterX += 10
                if (data.ballCenterX + 35) > data.width:
                    data.ballCenterX = data.width-35


def appleCollisionCheck(data):
    collision = False
    if theatre.getPointsList(data, 0) != None:
        x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, \
                            z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8 =  theatre.sockCoordinates(data, 0)
        topSock = [(x1, z1), (x5, z5), (x16, z16), (x15, z14), (x15, z15),(x17, z17), (x13, z13), (x12, z12), 
                    (x3, z3), (x7, z7), (x8, z8)]
        propShape = [data.appleCenterX, data.appleCenterY, 30]
        topCollision = collisionCheck(data, topSock, propShape)
        if topCollision == True:
            collision = True     
    if data.sock2 == True and theatre.getPointsList(data, 1) != None:
        a1, b1, a5, b5, a16, b16, a14, b14, a15, b15, a17, b17, a13, b13, a11, \
                            b11, a10, b10, a12, b12, a3, b3, a7, b7, a8, b8 =  theatre.sockCoordinates(data, 1)
        topSock = [(a1, b1), (a5, b5), (a16, b16), (a15, b14), (a15, b15),(a17, b17), (a13, b13), (a12, b12), 
                    (a3, b3), (a7, b7), (a8, b8)]
        topCollision = collisionCheck(data, topSock, propShape)
        if topCollision == True:
                collision = True
    return collision

def carCollisionCheck(data):
    if theatre.getPointsList(data, 0) != None:
        x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, \
                            z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8 =  theatre.sockCoordinates(data, 0)
        leftSock =[(x10, z10), (x12, z12), (x3, z3), (x7, z7), (x8, z8), (x1, z1)]
        rightSock = [(x1, z1), (x5, z5), (x16, z16), (x14, z14), (x15, z15), (x17, z17), (x13, z13), (x11, 
                            z11)]
        propShape = [data.carCenterX, data.height - 33]
        leftCollision = collisionCheck(data, leftSock, propShape)
        rightCollision = collisionCheck(data, rightSock, propShape)
        if data.frame.hands[0].is_left:
            if leftCollision == True:
                data.carCenterX -= 10
                if (data.carCenterX - 35)< 0:
                    data.carCenterX = 35
            elif rightCollision == True:
                data.carCenterX += 10
                if (data.carCenterX + 35) > data.width:
                    data.carCenterX = data.width-35
        else:
            if rightCollision == True:
                data.carCenterX -= 10
                if (data.carCenterX - 35)< 0:
                    data.carCenterX = 35
            elif leftCollision == True:
                data.carCenterX += 10
                if (data.carCenterX + 35) > data.width:
                    data.carCenterX = data.width-35
    if data.sock2 == True and theatre.getPointsList(data, 1) != None:
        a1, b1, a5, b5, a16, b16, a14, b14, a15, b15, a17, b17, a13, b13, a11, \
                            b11, a10, b10, a12, b12, a3, b3, a7, b7, a8, b8 =  theatre.sockCoordinates(data, 1)
        leftSock2 =[(a10, b10), (a12, b12), (a3, b3), (a7, b7), (a8, b8), (a1, b1)]
        rightSock2 = [(a1, b1), (a5, b5), (a16, b16), (a14, b14), (a15, b15), (a17, b17), (a13, b13), (a11, 
                            b11)]
        leftCollision2 = collisionCheck(data, leftSock2, propShape)
        rightCollision2 = collisionCheck(data, rightSock2, propShape)
        if data.frame.hands[1].is_left:
            if leftCollision2 == True:
                data.carCenterX -= 10
                if (data.carCenterX - 35)< 0:
                    data.carCenterX = 35
            elif rightCollision2 == True:
                data.carCenterX += 10
                if (data.carCenterX + 35) > data.width:
                    data.carCenterX = data.width-35
        else:
            if rightCollision2 == True:
                data.carCenterX -= 10
                if (data.carCenterX - 35)< 0:
                    data.carCenterX = 35
            elif leftCollision2 == True:
                data.carCenterX += 10
                if (data.carCenterX + 35) > data.width:
                    data.carCenterX = data.width-35

def timerFired(data):
    updateLeapMotionData(data)
    printLeapMotionData(data)
    if data.mode == 'splashScreen':
        splashScreen.timerFired(data)
    elif data.mode == 'theatre':
        theatre.timerFired(data)
        if data.prop == 'ball':
            if data.velocity != 0:
                print(data.velocity)
                velocityf = data.velocity + (-200)*(.2)
                data.ballCenterX = data.ballCenterX + ((data.velocity + velocityf)/2)*.2
                data.velocity = velocityf
                if -10 <= data.velocity <= 10:
                    data.velocity = 0
                if data.ballCenterX + 35 >= data.width:
                    data.ballCenterX = data.width - 35
                    data.velocity = 0
                elif data.ballCenterX - 35 <= 0:
                    data.ballCenterX = 35
                    data.velocity = 0
            ballCollisionCheck(data)

        elif data.prop == 'apple':
            if appleCollisionCheck(data):
                if biteGesture(data):
                    data.appleState += 1
                    if data.appleState > 5:
                        data.appleState = 5
        elif data.prop == 'car':
            carCollisionCheck(data)
    elif data.mode == 'help':
        helpScreen.timerFired(data)
    elif data.mode == 'cust':
        cust.timerFired(data)
    elif data.mode == 'cust2':
        cust2.timerFired(data)  
    elif data.mode == 'bg':
        bg.timerFired(data)
    elif data.mode == 'prop':
        prop.timerFired(data)
    elif data.mode == 'music':
        music.timerFired(data)
        
def updateLeapMotionData(data):
    data.frame = data.controller.frame()

# Print code from 112 website (Used in testing)
def printLeapMotionData(data):
    frame = data.frame
    if data.controller.is_connected:
        print("Frame id: %d, timestamp: %d, hands: %d, fingers: %d" % 
          (frame.id, frame.timestamp, len(frame.hands), len(frame.fingers)))

# This code is part of the draw lines functions but I did this on my own


def redrawAll(canvas, data):
    if data.mode == 'theatre':
        theatre.redrawAll(canvas, data)
    elif data.mode == 'splashScreen':
        splashScreen.redrawAll(canvas, data)
    elif data.mode == 'help':
        helpScreen.redrawAll(canvas, data)
    elif data.mode == 'cust':
        cust.redrawAll(canvas, data)
    elif data.mode == 'cust2':
        cust2.redrawAll(canvas, data)
    elif data.mode == 'bg':
        bg.redrawAll(canvas, data)
    elif data.mode == 'prop':
        prop.redrawAll(canvas, data)
    elif data.mode == 'music':
        music.redrawAll(canvas, data)


####################################
# Run function from 112 website
####################################


def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)
    
    def motionWrapper(event, canvas, data):
        motion(event, data)
        redrawAllWrapper(canvas, data)
    
    def b1downWrapper(event, canvas, data):
        b1down(event, data)
        redrawAllWrapper(canvas, data)

    def b1upWrapper(event, canvas, data):
        b1up(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 20 # milliseconds
    # create the root and the canvas
    root = Tk()
    root.title("Mock Sock")
    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    canvas.bind("<Motion>", lambda event:
                            motionWrapper(event, canvas, data))
    canvas.bind("<ButtonPress-1>",  lambda event:
                            b1downWrapper(event, canvas, data))
    canvas.bind("<ButtonRelease-1>",  lambda event:
                            b1upWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)
