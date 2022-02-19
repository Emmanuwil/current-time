import time
import datetime as dt
import turtle

# create a turtle to display time

t = turtle.Turtle()
# create a turtle to create rectangle box
tl = turtle.Turtle()
# create sceem
s = turtle.Screen()
# set background color of the screen
s.bgcolor("blue")
# obtain current hour, minute and sound
# from the sysytem
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
tl.pensize(3)
tl.color('white')
tl.penup()
#set the position of the turtle
for i in range(2):
    tl.forward(200)
    tl.left(90)
    tl.forward(70)
    tl.left(90)

# hide the turtle
tl.hideturtle()

while True:
    t.hideturtle()
    t.clear()
    # display the time
    t.write(str(hr).zfill(2)
    +":"+str(min).zfill(2)+":",
    font =("Arial Narrow", 35, "bold"))
time.sleep(1)
sec+= 1

if sec == 60:
    sec = 0
    min+= 1

if min == 60:
    min = 0
    min+= 1

if hr == 13:
    h = 1