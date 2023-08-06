import colorgram
import random
import turtle as t

timmy = t.Turtle()


colors = colorgram.extract("image.jpg", 30)
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if r > 200 and g > 200 and b > 200:
        continue
    rgb_colors.append((r, g, b))

print(rgb_colors)


def random_color():
    return random.choice(rgb_colors)


def paint():
    timmy.hideturtle()
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)
    timmy.speed("fastest")
    for _ in range(10):
        for _ in range(10):
            timmy.dot(20, random_color())
            timmy.forward(50)
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = t.Screen()

screen.colormode(255)
paint()

screen.exitonclick()
