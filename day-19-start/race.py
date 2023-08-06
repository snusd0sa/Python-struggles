from turtle import Turtle, Screen
import random

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="who will win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("red")
# timmy.penup()
# timmy.goto(x=-230, y=-100)

racers = []


for color in colors:
    t = Turtle()
    t.shape("turtle")
    t.color(color)
    t.penup()
    t.goto(x=-230, y=100 - colors.index(color) * 40)
    racers.append(t)

if user_bet:
    race_on = True

while race_on:
    for r in racers:
        random_distance = random.randint(0, 10)
        r.forward(random_distance)
        if r.xcor() > 230:
            print(f"{r.pencolor()} won!")
            race_on = False

screen.exitonclick()
