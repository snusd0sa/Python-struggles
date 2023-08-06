import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)


player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")


game_is_on = True
counter = 0
while game_is_on:
    car_manager.move()
    if counter == 16:
        car_manager.create_car()
        counter = 0

    if car_manager.check_collision(player):
        scoreboard.game_over()
        game_is_on = False

    if player.is_top():
        player.reset()
        car_manager.level_up()
        scoreboard.update_score()

    time.sleep(0.1)
    screen.update()
    counter += 1

screen.exitonclick()
