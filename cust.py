from Tkinter import *

def mousePressed(event, data):
    if (3*data.height/10 - 15) <= event.y <= (3*data.height/10 + 15):
        if (data.width/10-15) <= event.x <= (data.width/10+15):
            data.color = 'red'
            data.outlineX = data.width/10
            data.outlineY = 3*data.width/10
        elif (2*data.width/10-15) <= event.x <= (2*data.width/10+15):
            data.color = 'orange'
            data.outlineX = 2*data.width/10
            data.outlineY = 3*data.width/10
        elif (3*data.width/10-15) <= event.x <= (3*data.width/10+15):
            data.color = 'yellow'
            data.outlineX = 3*data.width/10
            data.outlineY = 3*data.width/10
        elif (4*data.width/10-15) <= event.x <= (4*data.width/10+15):
            data.color = 'green'
            data.outlineX = 4*data.width/10
            data.outlineY = 3*data.width/10
        elif (5*data.width/10-15) <= event.x <= (5*data.width/10+15):
            data.color = 'blue'
            data.outlineX = 5*data.width/10
            data.outlineY = 3*data.width/10
        elif (6*data.width/10-15) <= event.x <= (6*data.width/10+15):
            data.color = 'purple'
            data.outlineX = 6*data.width/10
            data.outlineY = 3*data.width/10
        elif (7*data.width/10-15) <= event.x <= (7*data.width/10+15):
            data.color = 'pink'
            data.outlineX = 7*data.width/10
            data.outlineY = 3*data.width/10
        elif (8*data.width/10-15) <= event.x <= (8*data.width/10+15):
            data.color = 'black'
            data.outlineX = 8*data.width/10
            data.outlineY = 3*data.width/10
        elif (9*data.width/10-15) <= event.x <= (9*data.width/10+15):
            data.color = 'gray'
            data.outlineX = 9*data.width/10
            data.outlineY = 3*data.width/10
    elif (data.height/2- 15) <= event.y <= (data.height/2 + 65):
        if (data.width/3 -50) <= event.x <= (data.width/3 + 50):
            data.accessory = 'bowtie'
            data.accOutlineX = (data.width/3 - 50)
            data.accOutlineY = (data.height/2- 10)
        elif (2*data.width/3 - 50) <= event.x <= (2*data.width/2 + 50):
            data.accessory = 'tophat'
            data.accOutlineX = (2*data.width/3 - 50)
            data.accOutlineY = (data.height/2 - 20)
    elif (3*data.height/4 - 40) <= event.y <= (3*data.height/4 + 40):
        if (2*data.width/3 - 40) <= event.x <= (2*data.width/3 + 40):
            data.accessory = 'crown'
            data.accOutlineY = (3*data.height/4 - 40)
            data.accOutlineX = (2*data.width/3 - 40)
    elif (data.width/3 - 62.5) <= event.x <= (data.width/3 + 42.5):
        if (9*data.height/10 - 26) <= event.y <= (9*data.height/10 + 26):
            data.mode = 'bg'
    elif (2*data.width/3 - 90) <= event.x <= (2*data.width/3 + 90):
        if (9*data.height/10 - 26) <= event.y <= (9*data.height/10 + 26):
            data.sock2 = True
            data.outlineX = 0
            data.outlineY = 0
            data.accOutlineX = 0
            data.accOutlineY = 0
            data.mode = 'cust2'

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def drawLine(canvas, data):
    for pairNum in range(0, len(data.linePoints), 4):
        x1 = data.linePoints[pairNum]
        y1 = data.linePoints[pairNum + 1]
        x2 = data.linePoints[pairNum + 2]
        y2 = data.linePoints[pairNum + 3]
        canvas.create_line(x1, y1, x2, y2, width = 3)

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.curtains)
    canvas.create_image(data.width/2, data.height/10, image = data.customize)
    #Color
    canvas.create_text(data.width/2, 2*data.height/10, 
                       text = "Choose a sock color:", font = "Arial 20 bold", 
                       fill = 'white')
    canvas.create_rectangle(data.width/10-15, 3*data.height/10 - 15, 
                            data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'red')
    canvas.create_rectangle(2*data.width/10-15, 3*data.height/10 - 15, 
                            2*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'orange')
    canvas.create_rectangle(3*data.width/10-15, 3*data.height/10 - 15, 
                            3*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'yellow')
    canvas.create_rectangle(4*data.width/10-15, 3*data.height/10 - 15, 
                            4*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'green')
    canvas.create_rectangle(5*data.width/10-15, 3*data.height/10 - 15, 
                            5*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'blue')
    canvas.create_rectangle(6*data.width/10-15, 3*data.height/10 - 15, 
                            6*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'purple')
    canvas.create_rectangle(7*data.width/10-15, 3*data.height/10 - 15, 
                            7*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'pink')
    canvas.create_rectangle(8*data.width/10-15, 3*data.height/10 - 15, 
                            8*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'black')
    canvas.create_rectangle(9*data.width/10-15, 3*data.height/10 - 15, 
                            9*data.width/10 + 15, 3*data.height/10 + 15, 
                            fill = 'gray')
    #Accessories
    canvas.create_text(data.width/2, 4*data.height/10, text = "Choose an accessory", 
                        font = 'Arial 20 bold', fill = 'white')
    canvas.create_image(data.width/3, data.height/2 + 25, image = data.bowtieTN)
    canvas.create_text(data.width/3, data.height/2 + 80, text = "Bowtie", 
                        font = "Arial 15 bold", fill = 'white')
    canvas.create_image(2*data.width/3, data.height/2 + 25, image = data.tophat0)
    canvas.create_text(2*data.width/3, data.height/2 + 80, text = 'Top Hat', 
                        font = 'Arial 15 bold', fill = 'white')
    canvas.create_image(2*data.width/3, 3*data.height/4, image = data.crown0)
    canvas.create_text(2*data.width/3, 3*data.height/4 + 45, text = 'Crown', 
                        font = 'Arial 15 bold', fill = 'white')
    canvas.create_rectangle(3*data.width/10 - 25, 3*data.height/4 - 35, 4*data.width/10 + 5, 
                            3*data.height/4 + 35, fill = 'white')
    canvas.create_text(7*data.width/20 - 10, 3*data.height/4 + 55, text = "Draw Mustache", 
                        font = "Arial 15 bold", fill = 'white')
    drawLine(canvas, data)
    # Highlight box
    if data.outlineX != 0 and data.outlineY != 0:
        canvas.create_rectangle(data.outlineX - 15, data.outlineY - 15, 
                                data.outlineX + 15, data.outlineY + 15, 
                                outline = 'white', width = 5)
    if data.accOutlineX != 0 and data.accOutlineY != 0:
        if data.accessory == 'bowtie':
            canvas.create_rectangle(data.accOutlineX, data.accOutlineY, 
                                    data.accOutlineX + 100, data.accOutlineY + 70, 
                                    outline = 'white', width = 5)
        elif data.accessory == 'tophat':
            canvas.create_rectangle(data.accOutlineX, data.accOutlineY, 
                                    data.accOutlineX + 100, data.accOutlineY + 85, 
                                    outline = 'white', width = 5)
        elif data.accessory == 'crown':
            canvas.create_rectangle(data.accOutlineX, data.accOutlineY, 
                                    data.accOutlineX + 80, data.accOutlineY + 70, 
                                    outline = 'white', width = 5)  
    # Next button
    canvas.create_image(data.width/3 - 10, 9*data.height/10, image = data.next)
    canvas.create_image(2*data.width/3, 9*data.height/10, image = data.addSock)