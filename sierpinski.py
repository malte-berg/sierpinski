import turtle
import random
import numpy as np

def dist(x1, y1, x2, y2):
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    return distance

p = [[0, 280], [-242, -140], [242, -140]]

def color(x):
    colorx = (x + 242)
    if colorx > 0 and colorx < 69:
        t.pencolor((255,0,0))
    elif colorx > 69 and colorx < 69*2:
        t.pencolor((255,127,0))
    elif colorx > 69*2 and colorx < 69*3:
        t.pencolor((255,255,0))
    elif colorx > 69*3 and colorx < 69*4:
        t.pencolor((0,255,0))
    elif colorx > 69*4 and colorx < 69*5:
        t.pencolor((0,0,255))
    elif colorx > 69*5 and colorx < 69*6:
        t.pencolor((75,0,130))
    elif colorx > 69*6 and colorx < 69*7:
        t.pencolor((148,0,211))


t = turtle.Turtle()
turtle.hideturtle()

s = turtle.getscreen()
s.screensize(600,600)
s.colormode(255)
s.bgcolor('black')

t.speed('fastest')
t.hideturtle()
t.up()
for i in range(3):
    t.goto(p[i][0],p[i][1])
    t.dot()

for i in range (10000):
    r = random.randint(0, 2)
    pos = t.pos()
    x, y = (pos[0]+p[r][0])/2, (pos[1]+p[r][1])/2
    t.goto(x, y)
    color(x)
    t.dot()

turtle.exitonclick()