import turtle
import random
import time
import math

# construct a turtle with a circle shape
myTurtle = turtle.Turtle(shape="circle")
turtle.bgcolor("mistyrose")
myTurtle.speed(-1000)
myTurtle.ht()

# create an empty list to hold stampIds
stampIds = []
xposition = []
yposition = []
color = []
alive = []


colors = ["gold", "paleturquoise", "darkkhaki", "lightgreen", "peru", "olive", "deepskyblue"]
# iterate through each circle position...
for i in range(-250, 250, 50):
   for j in range(-250, 250, 50):
       # move the turtle into position…
       colorchoice = random.choice(colors) #Choose a random color
       myTurtle.pencolor(colorchoice)
       myTurtle.fillcolor(colorchoice)
       myTurtle.ht()
       myTurtle.penup()
       x = i+25
       y = j+25

       myTurtle.setposition(x, y)
       # stamp and append the resulting id to the list
       stampIds.append(myTurtle.stamp())
       xposition.append(x)
       yposition.append(y)
       color.append(colorchoice)
       alive.append(True)


#commence the loops
def loopybois():
   # pick a random stampId to not delete
   deadColor = random.choice(colors)
   colorchoice=deadColor
   # iterate through and delete all stamps that are the same color as the stamp not being deleted
   for i in range(len(stampIds)):

       if color[i] == deadColor:
           myTurtle.clearstamp(stampIds[i])
           alive[i]=False

   for i in range(len(stampIds)):
       if not alive[i]:
           colorchoice = random.choice(colors)
           while colorchoice==deadColor:
               colorchoice = random.choice(colors) #Choose a random color
           myTurtle.pencolor(colorchoice)
           myTurtle.fillcolor(colorchoice)
           myTurtle.ht()
           myTurtle.penup()

           myTurtle.setposition(xposition[i], yposition[i])
           # stamp and append the resulting id to the list
           stampIds[i] = myTurtle.stamp()
           color[i]=colorchoice
           alive[i] = True
   
   # background color changing
   numberofcolors = [0, 0, 0, 0, 0, 0, 0]
   for i in range(len(stampIds)):
       currentcolor = color[i]
       if currentcolor == "gold":
           numberofcolors[0] = numberofcolors[0] + 1
       elif currentcolor == "paleturquoise":
           numberofcolors[1] = numberofcolors[1] + 1
       elif currentcolor == "darkkhaki":
           numberofcolors[2] = numberofcolors[2] + 1
       elif currentcolor =="lightgreen":
           numberofcolors[3] = numberofcolors[3] + 1
       elif currentcolor == "peru":
           numberofcolors[4] = numberofcolors[4] + 1
       elif currentcolor == "olive":
           numberofcolors[5] = numberofcolors[5] + 1
       elif currentcolor == "deepskyblue":
           numberofcolors[6] = numberofcolors[6] + 1
   
   disease = 0
   for i in range(len(numberofcolors)):
       if numberofcolors[i] > 5:
           disease = disease + 1     
   if(disease >= 6):
       turtle.bgcolor("mistyrose")
   elif(disease >= 4):
       turtle.bgcolor("lightsalmon")
   elif(disease >= 2):
       turtle.bgcolor("indianred")
   elif(disease >= 0):
       turtle.bgcolor("maroon")

   loopybois()

loopybois()
turtle.done()