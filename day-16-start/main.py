# import turtle
# from turtle import Turtle, Screen
#
## timmy = turtle.Turtle()
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DarkOrchid")
#
# timmy.forward(100)
#
# my_screen = Screen()
# my_screen.canvheight
# print(my_screen.canvheight)
#
#
# ninja = Turtle()
#
# ninja.speed(0)
#
# for i in range(180):
#    ninja.forward(100)
#    ninja.right(30)
#    ninja.forward(20)
#    ninja.left(60)
#    ninja.forward(50)
#    ninja.right(30)
#
#    ninja.penup()
#    ninja.setposition(0, 0)
#    ninja.pendown()
#
#    ninja.right(2)
#
# my_screen.exitonclick()
#

print("| Pokemon Name | etc | etc")


# import prettytable

from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

table.align = "r"
print(table)
table.