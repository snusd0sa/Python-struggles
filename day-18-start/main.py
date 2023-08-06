from turtle import Turtle, Screen
from random import randint, choice


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)


def random_walk(turtle, steps, strict=True):
    for _ in range(steps):
        turtle.pensize(5)
        turtle.pencolor(random_color())
        turtle.forward(10)
        if strict:
            turtle.setheading(choice(directions))
        else:
            turtle.setheading(randint(0, 360))


def draw_spirograph(turtle, size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        turtle.pencolor(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)


timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")
timmy.pencolor("red")
timmy.speed("fastest")
directions = [0, 90, 180, 270]


# Timmy draws a square
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)


for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.colormode(255)
screen.resetscreen()


def draw_shape(turtle, sides):
    for i in range(3, 11):
        timmy.pencolor(random_color())
        for _ in range(i):
            timmy.right(360 / i)
            timmy.forward(100)


screen.resetscreen()
# draw_shape(timmy, 10)
# random_walk(timmy, 100)
draw_spirograph(timmy, 5)
screen.exitonclick()
