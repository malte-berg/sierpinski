import turtle
import random

p = [[0, 280], [-242, -140], [242, -140]]
colors = [((255, 0, 0), (0, 69)),
          ((255, 127, 0), (69, 69*2)),
          ((255, 255, 0), (69*2, 69*3)),
          ((0, 255, 0), (69*3, 69*4)),
          ((0, 0, 255), (69*4, 69*5)),
          ((75, 0, 130), (69*5, 69*6)),
          ((148, 0, 211), (69*6, 69*7))]

def rainbow(x):
    colorx = (x + 242)
    for i, (color, (start, end)) in enumerate(colors):
        if start <= colorx < end:
            t.pencolor(color)
            break


# Initialize turtle
t = turtle.Turtle()
turtle.hideturtle()
t.speed('fastest')
t.hideturtle()
t.up()
t.pencolor('white')
# Initialize screen
s = turtle.getscreen()
s.screensize(600,600)
s.colormode(255)
s.bgcolor('black')


# Draw first 3 points
for i in range(3):
    t.goto(p[i][0],p[i][1])
    t.dot()

# Draw 10000 points
for i in range(10000):
    r = random.randint(0, 2)
    pos = t.pos()
    # Midway points
    x, y = (pos[0]+p[r][0])/2, (pos[1]+p[r][1])/2
    t.goto(x, y)
    rainbow(x)
    t.dot()

turtle.exitonclick()
