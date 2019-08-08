import turtle
import random
import time
import math
# construct a turtle with a circle shape
myTurtle = turtle.Turtle(shape="circle")
turtle.bgcolor("blanchedalmond")
myTurtle.speed(0)
myTurtle.ht()
# create an empty list to hold stampIds
stampIds = []
posx=[]
posy=[]
turtleColors = {}
colors = ["tomato", "lightsalmon", "peachpuff", "darkorange", "orange", "mediumseagreen", "mediumaquamarine", "mediumturquoise", "powderblue","lightskyblue","lightslategrey", "lightsteelblue", "mediumslateblue"]
def fillAll(color=None):
   # iterate through each circle position...
   for i in range(10):
       for j in range(10):
           # move the turtle into position...
           clr=color
           if color is None:
               clr = random.choice(colors) #Choose a random color
               print("color is None")
           myTurtle.ht()
           myTurtle.penup()
           x = i*50
           y = j*50
           posx.append(x-250)
           posy.append(y-250)
           myTurtle.setposition(x-250, y-250)
           myTurtle.pencolor(clr)
           myTurtle.fillcolor(clr)
           # stamp and append the resulting id to the list
           turtleId = myTurtle.stamp()
           stampIds.append(turtleId)
           turtleColors[turtleId] = clr
# iterate through and delete all stamps EXCEPT for survivor
def cleanup(survivor):
   for stamp in stampIds:
       if (stamp != survivor):
           myTurtle.clearstamp(stamp)
fillAll(None)
clrtemp=None
#commence the loops
def loopybois (first, clr=None) :
   clrtemp=random.choice(colors)
   while clrtemp==clr: # choose a different color from last time
       clrtemp=random.choice(colors)
   clr=clrtemp
   if first:
       clr="red"
   survivor = random.choice(stampIds)
   myTurtle.clearstamp(survivor)
   index = stampIds.index(survivor)
   myTurtle.pencolor(clr)
   myTurtle.fillcolor(clr)
   myTurtle.setposition(posx[index], posy[index])
   stampIds[index] = myTurtle.stamp()
   # pick a random stampId to not delete
   # iterate through and delete all stamps EXCEPT for survivor
   cleanup(stampIds[index])
   time.sleep(1)
   fillAll(clr)
   loopybois(False, clr)
loopybois(True)