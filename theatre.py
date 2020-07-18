from Tkinter import *
import math

def mousePressed(event, data):
    if 0 <= event.x <= 50 and 0 <= event.y <= 50:
        data.playMusic = False
        data.appleState = 0
        data.ballCenterX = data.width/2
        data.ballCenterY = 50
        data.mode = 'splashScreen'

def keyPressed(event, data):
    pass

def timerFired(data):
    if data.prop == 'ball':
        gravity = 10
        if gravity*(data.height - data.ballCenterY) >= data.energy:
            v = 2.5
            data.down = True
        else:
            v = 1.5*math.sqrt(2*(data.energy - gravity*(data.height - data.ballCenterY)))
        if data.down == False:
            v *= -1
        data.ballCenterY += v
        if data.ballCenterY + 25 >= data.height:
            data.down = False
            data.ballCenterY = data.height - 25
            data.energy *= .73


def getPointsList(data, handNum):
    #updateLeapMotionData(data)
    thumb = data.frame.hands[handNum].fingers[0]
    index = data.frame.hands[handNum].fingers[1]
    if data.controller.is_connected:
        thumbTip = thumb.bone(3).next_joint
        thumbEnd =  thumb.bone(2).prev_joint
        thumbMid = thumb.bone(3).prev_joint
        indexTip = index.bone(3).next_joint
        indexMid2 = index.bone(3).prev_joint
        indexMid1 = index.bone(2).prev_joint
        indexEnd = index.bone(1).prev_joint
        wrist = data.frame.hands[handNum].wrist_position
        wristLen = data.frame.hands[handNum].arm.width
        elbow = data.frame.hands[handNum].arm.elbow_position
        armDir = data.frame.hands[handNum].arm.direction
        return (thumbTip, thumbEnd, thumbMid, indexTip, indexEnd, indexMid1,
         indexMid2, wrist, wristLen, elbow, armDir)


def drawRectangle(data, canvas):
    if getPointsList(data, 0) != None:
        thumbTip, thumbEnd, thumbMid, indexTip, indexEnd, indexMid1, indexMid2,\
        wrist, wristLen, elbow, armDir = getPointsList(data, 0)
        x1, z1 = indexTip.x, indexTip.z
        x2, z2 = wrist.x, wrist.z
        x1 += data.width/2
        x2 += data.width/2
        z1 += data.height/2
        z2 += data.height/2
        canvas.create_rectangle(x1, z1, x2, z2, outline = "red", width = 5)

def drawCircle(data, canvas):
    if getPointsList(data, 0) != None:
        thumbTip, thumbEnd, thumbMid, indexTip, indexEnd, indexMid1, indexMid2,\
        wrist, wristLen, elbow, armDir = getPointsList(data, 0)
        x1, z1 = indexTip.x, indexTip.z
        x2, z2 = wrist.x, wrist.z
        x1 += data.width/2
        x2 += data.width/2
        z1 += data.height/2
        z2 += data.height/2
        canvas.create_oval(x1, z1, x2, z2, outline = "blue", width = 5)

def topHatAngle(data, handNum):
    index = data.frame.hands[handNum].pointables[1]
    direction = index.direction
    xDir = direction.x
    zDir = direction.z
    angle = math.degrees(math.atan(zDir/xDir))
    if data.frame.hands[handNum].is_left:
        if -7.5 < angle <= 7.5:
            return data.tophat0, False
        elif 7.5 < angle <= 22.5:
            return data.tophat0, False
        elif 22.5 < angle <= 37.5:
            return data.tophat15, False
        elif 37.5 < angle <= 52.5:
            return data.tophat15, False
        elif 52.5 < angle:
            return data.tophat15, False
        elif -22.5 < angle <= -7.5:
            return data.tophatN15, True
        elif -37.5 < angle <= -22.5:
            return data.tophatN30, True
        elif -52.5 < angle <= -37.5:
            return data.tophatN45, True
        elif angle <= -52.5:
            return data.tophatN60, True
    else:
        if -7.5 < angle <= 7.5:
            return data.tophat0, True
        elif 7.5 < angle <= 22.5:
            return data.tophat0, True
        elif 22.5 < angle <= 37.5:
            return data.tophat15, False
        elif 37.5 < angle <= 52.5:
            return data.tophat30, False
        elif 52.5 < angle <= 67.7:
            return data.tophat45, False
        elif 67.7 < angle:
            return data.tophat60, False
        elif -22.5 < angle <= -7.5:
            return data.tophat0, True
        elif -37.5 < angle <= -22.5:
            return data.tophatN15, True
        elif -52.5 < angle <= -37.5:
            return data.tophatN15, True
        elif angle <= -52.5:
            return data.tophatN15, True

def crownAngle(data, handNum):
    index = data.frame.hands[handNum].pointables[1]
    direction = index.direction
    xDir = direction.x
    zDir = direction.z
    angle = math.degrees(math.atan(zDir/xDir))
    if data.frame.hands[handNum].is_left:
        if -7.5 < angle <= 7.5:
            return data.crown0, False
        elif 7.5 < angle <= 22.5:
            return data.crown0, False
        elif 22.5 < angle <= 37.5:
            return data.crown15, False
        elif 37.5 < angle <= 52.5:
            return data.crown15, False
        elif 52.5 < angle:
            return data.crown15, False
        elif -22.5 < angle <= -7.5:
            return data.crownN30, True
        elif -37.5 < angle <= -22.5:
            return data.crownN30, True
        elif -52.5 < angle <= -37.5:
            return data.crownN45, True
        elif angle <= -52.5:
            return data.crownN60, True
    else:
        if -7.5 < angle <= 7.5:
            return data.crown0, True
        elif 7.5 < angle <= 22.5:
            return data.crown0, True
        elif 22.5 < angle <= 37.5:
            return data.crown15, False
        elif 37.5 < angle <= 52.5:
            return data.crown30, False
        elif 52.5 < angle <= 67.7:
            return data.crown45, False
        elif 67.7 < angle:
            return data.crown60, False
        elif -22.5 < angle <= -7.5:
            return data.crown0, True
        elif -37.5 < angle <= -22.5:
            return data.crown0, True
        elif -52.5 < angle <= -37.5:
            return data.crownN15, True
        elif angle <= -52.5:
            return data.crownN15, True

def sockCoordinates(data, handNum):
    if getPointsList(data, handNum) != None:
        thumbTip, thumbEnd, thumbMid, indexTip, indexEnd, indexMid1, indexMid2,\
            wrist, wristLen, elbow, armDir = getPointsList(data, handNum)
        thumb = data.frame.hands[handNum].pointables[0]
        thumbWidth = thumb.width
        x1, z1 = indexTip.x, indexTip.z
        x2, z2 = wrist.x, wrist.z
        x3, z3 = indexEnd.x, indexEnd.z
        x4, z4 = thumbTip.x, thumbTip.z
        x5, z5 = thumbEnd.x, thumbTip.z
        x6, z6 = thumbMid.x, thumbMid.z
        x7, z7 = indexMid1.x, indexMid1.z
        x8, z8 = indexMid2.x, indexMid2.z
        x9, z9 = elbow.x, elbow.z
        vx1, vz1 = armDir.x, armDir.z
        if data.frame.hands[handNum].is_left:
            x10, z10 = x9 - wristLen/2, z9
            x11, z11 = x9 + wristLen/2, z9
            x14, z14 = x4 - thumbWidth/2, z4,
            x15, z15 = x4 + thumbWidth/2, z4
            x16, z16 = x6 - thumbWidth/2, z6,
            x17, z17 = x6 + thumbWidth/2, z6
        else:
            x11, z11 = x9 - wristLen/2, z9
            x10, z10 = x9 + wristLen/2, z9
            x15, z15 = x4 - thumbWidth/2, z4,
            x14, z14 = x4 + thumbWidth/2, z4
            x17, z17 = x6 - thumbWidth/2, z6,
            x16, z16 = x6 + thumbWidth/2, z6
        ratio = (wristLen/2)/(vx1**2 + vz1**2)**.5
        x13, z13 = x2 + vx1*ratio*2, z2 - vz1*ratio/2
        x12, z12 = x2 + vx1*ratio, z2 + vz1*ratio
        x1 += data.width/2
        x2 += data.width/2
        x3 += data.width/2
        x4 += data.width/2
        x5 += data.width/2
        x6 += data.width/2
        x7 += data.width/2
        x8 += data.width/2
        x9 += data.width/2
        x10 += data.width/2
        x11 += data.width/2
        x12 += data.width/2
        x13 += data.width/2
        x14 += data.width/2
        x15 += data.width/2
        x16 += data.width/2
        x17 += data.width/2
        z1 += data.height/2
        z2 += data.height/2
        z3 += data.height/2
        z4 += data.height/2
        z5 += data.height/2
        z6 += data.height/2
        z7 += data.height/2
        z8 += data.height/2
        z9 += data.height/2
        z10 += data.height/2
        z11 += data.height/2
        z12 += data.height/2
        z13 += data.height/2
        z14 += data.height/2
        z15 += data.height/2
        z16 += data.height/2
        z17 += data.height/2
        return [x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, 
                                z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8]
        
def drawSock(data, canvas, handNum):
    if getPointsList(data, handNum) != None:
        x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, \
                                z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8 = \
                                sockCoordinates(data, handNum)
        if handNum == 0:
            canvas.create_polygon(x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, 
                                    z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8, 
                                    width = 1, smooth = 1, fill = data.color)
        elif handNum == 1:
            canvas.create_polygon(x1, z1, x5, z5, x16, z16, x14, z14, x15, z15, x17, z17, x13, z13, x11, 
                                    z11, x10, z10, x12, z12, x3, z3, x7, z7, x8, z8, 
                                    width = 1, smooth = 1, fill = data.color2)
        if data.frame.hands[handNum].is_left:
            if handNum == 0:
                eyeX = x7 - 10
                eyeY = (z7 + z5)/2
                if data.accessory == 'tophat' and len(data.frame.hands) != 0:
                    angle, shift = topHatAngle(data, 0)
                    if shift == False:
                        canvas.create_image(x3 + 40, z3 - 50, image = angle)
                    else:
                        canvas.create_image(x3 - 15, z3 - 55, image = angle)
                elif data.accessory == 'crown' and len(data.frame.hands) != 0:
                    angle, shift = crownAngle(data, 0)
                    if shift == False:
                        canvas.create_image(x3 + 40, z3 - 40, image = angle)
                    else:
                        canvas.create_image(x3 - 15, z3 - 40, image = angle) 
            elif handNum == 1:
                eyeX = x7 - 10
                eyeY = (z7 + z5)/2
                if data.accessory2 == 'tophat' and len(data.frame.hands) != 0:
                    angle, shift = topHatAngle(data, 1)
                    if shift == False:
                        canvas.create_image(x3 + 40, z3 - 50, image = angle)
                    else:
                        canvas.create_image(x3 - 15, z3 - 55, image = angle)
                elif data.accessory2 == 'crown' and len(data.frame.hands) != 0:
                    angle, shift = crownAngle(data, 1)
                    if shift == False:
                        canvas.create_image(x3 + 40, z3 - 40, image = angle)
                    else:
                        canvas.create_image(x3 - 15, z3 - 40, image = angle)
        
        else:
            if handNum == 0:
                eyeX = x7 + 10
                eyeY = (z7 + z5)/2 - 10
                if data.accessory == 'tophat' and len(data.frame.hands) != 0:
                    angle, shift = topHatAngle(data, 0)
                    if shift == False:
                        canvas.create_image(x3 + 15, z3 - 55, image = angle)
                    else:
                        canvas.create_image(x3 - 35, z3 - 55, image = angle) 
                elif data.accessory == 'crown' and len(data.frame.hands) != 0:
                    angle, shift = crownAngle(data, 0)
                    if shift == False:
                        canvas.create_image(x3 + 20, z3 - 40, image = angle)
                    else:
                        canvas.create_image(x3 - 25, z3 - 45, image = angle)
            elif handNum == 1:
                eyeX = x7 + 10
                eyeY = (z7 + z5)/2 - 10
                if data.accessory2 == 'tophat' and len(data.frame.hands) != 0:
                    angle, shift = topHatAngle(data, 1)
                    if shift == False:
                        canvas.create_image(x3 + 15, z3 - 55, image = angle)
                    else:
                        canvas.create_image(x3 - 35, z3 - 55, image = angle) 
                elif data.accessory2 == 'crown' and len(data.frame.hands) != 0:
                    angle, shift = crownAngle(data, 1)
                    if shift == False:
                        canvas.create_image(x3 + 20, z3 - 40, image = angle)
                    else:
                        canvas.create_image(x3 - 25, z3 - 45, image = angle)
        if handNum == 0:
            if data.accessory == 'bowtie' and len(data.frame.hands) != 0:
                canvas.create_image(x13, z13, image = data.bowtie) 
        elif handNum == 1:
            if data.accessory2 == 'bowtie' and len(data.frame.hands) != 0:
                canvas.create_image(x13, z13, image = data.bowtie) 
        if data.controller.is_connected and len(data.frame.hands) != 0:
            canvas.create_image(eyeX, eyeY, image = data.leftEye)
        if handNum == 0 and len(data.frame.hands) != 0:
            mustachePoints = mustacheLocation(data)
            for pairNum in range(0, len(mustachePoints), 4):
                f1 = mustachePoints[pairNum] + x1
                g1 = mustachePoints[pairNum + 1] + z1
                f2 = mustachePoints[pairNum + 2] + x1
                g2 = mustachePoints[pairNum + 3] + z1
                canvas.create_line(f1, g1, f2, g2, width = 3)
        if handNum == 1:
            mustachePoints2 = mustacheLocation2(data)
            for pairNum2 in range(0, len(mustachePoints2), 4):
                h1 = mustachePoints2[pairNum2] + x1
                j1 = mustachePoints2[pairNum2 + 1] + z1
                h2 = mustachePoints2[pairNum2 + 2] + x1
                j2 = mustachePoints2[pairNum2 + 3] + z1
                canvas.create_line(h1, j1, h2, j2, width = 3)

def mustacheLocation(data):
    mustachePoints = []
    for pointNum in range(0, len(data.linePoints), 2):
        x1 = data.linePoints[pointNum] - (7*data.width/20 - 20)
        y1 = data.linePoints[pointNum + 1] - (3*data.height/4)
        mustachePoints += [x1, y1]
    return mustachePoints

def mustacheLocation2(data):
    mustachePoints = []
    for pointNum in range(0, len(data.linePoints2), 2):
        x1 = data.linePoints2[pointNum] - (7*data.width/20 - 20)
        y1 = data.linePoints2[pointNum + 1] - (3*data.height/4)
        mustachePoints += [x1, y1]
    return mustachePoints

def redrawAll(canvas, data):
    canvas.create_image(data.width/2, data.height/2, image = data.background)
    canvas.create_image(27.5, 27.5, image = data.home)
    drawSock(data, canvas, 0)
    if data.sock2 == True and len(data.frame.hands) == 2:
        drawSock(data, canvas, 1)
    if data.prop == 'ball':
        canvas.create_image(data.ballCenterX, data.ballCenterY, image = data.ball)
    elif data.prop == 'apple' and data.appleState != None:
        canvas.create_image(data.width + 50, data.height/2, anchor = E, image = data.branch)
        canvas.create_image(data.appleCenterX, data.appleCenterY, image = data.appleStates[data.appleState])
    elif data.prop == 'car':
        canvas.create_image(data.carCenterX, data.height - 33, image = data.car)