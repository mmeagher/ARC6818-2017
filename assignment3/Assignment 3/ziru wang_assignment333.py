
# coding: utf-8

# In[1]:


import turtle
import random
import datetime
from time import sleep


# setup the window with a background colour
wn = turtle.Screen()
wn.bgcolor("cyan")

# create the turtles for displaying the time
secondTurtle = turtle.Turtle()
minuteTurtle = turtle.Turtle()
hourTurtle = turtle.Turtle()

# get the current time
currentTime=datetime.datetime.now().time()

minuteTurtle.shape("circle")
minuteTurtle.color("blue")
hourTurtle.shape("square")
hourTurtle.color("yellow")
secondTurtle.shape("triangle")
secondTurtle.color("red")

# raise pens for all turtles
secondTurtle.penup()
minuteTurtle.penup()
hourTurtle.penup()

# move the turtles to different locations on the screen
secondTurtle.goto(0,0)
minuteTurtle.goto(-200,0)
hourTurtle.goto(-100,-100)

# set orientation for all turtles
secondTurtle.setheading(90)
minuteTurtle.setheading(90)
hourTurtle.setheading(90)

# set the size of all turtles
secondTurtle.shapesize(0.5,0.5,0.5) 
minuteTurtle.shapesize(7) 
hourTurtle.shapesize(10,10)

minuteTurtle.rt((currentTime.minute*6)-(90-minuteTurtle.heading()))
hourTurtle.rt((currentTime.hour*30)-(90-hourTurtle.heading()))
    
for count in range(0,100):
    sfcolor = ["white", "blue", "purple", "grey", "magenta"]
    secondTurtle.color(random.choice(sfcolor))
    secondTurtle.penup()
    secondTurtle.goto(0,0)
    secondTurtle.rt(currentTime.second*6)
    secondTurtle.fd(currentTime.minute*6)
    secondTurtle.pendown()
    secondTurtle.circle(5)

# define the previous value of time as the currentTime
prevSecond=currentTime.second
prevMinute=currentTime.minute
prevHour=currentTime.hour


# in each second update the size of all the turtles
for i in range(0,100):
	currentTime=datetime.datetime.now().time()
	currentSecond=currentTime.second
	currentMinute=currentTime.minute
	currentHour=currentTime.hour
	
	if (currentSecond != prevSecond):
		secondTurtle.color(random.choice(sfcolor))
		secondTurtle.penup()
		secondTurtle.rt(currentTime.second*6)
		secondTurtle.pendown()
		secondTurtle.fd(currentTime.minute*6)
		secondTurtle.pendown()
		secondTurtle.circle(5)
	
	if (currentMinute != prevMinute):	
		minuteTurtle.shapesize((currentTime.minute*(10/60)))
		
	if (currentHour != prevHour):
		hourTurtle.shapesize((currentTime.hour*(10/12)))
	
	prevSecond=currentTime.second
	prevMinute=currentTime.minute
	prevHour=currentTime.hour
	
	sleep(1)
	

# add this line to prevent the window from closing when the programme finishes executing
win=turtle.Screen(); win.exitonclick()

