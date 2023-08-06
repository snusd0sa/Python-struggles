from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.create_car()

    def create_car(self):
        self.color = random.choice(COLORS)
        self.random_y = random.randint(-250, 250)
        self.random_x = random.randint(300, 600)
        self.car = Turtle()
        self.car.shape("square")
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.color(self.color)
        self.car.penup()
        print(self.random_x, self.random_y)
        self.car.goto(self.random_x, self.random_y) 
        self.cars.append(self.car)

    def check_collision(self,player):
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False
        
    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.car_speed, car.ycor())
            if car.xcor() < -300:
                car.hideturtle()
                self.cars.remove(car)
                del car
                self.create_car()
            

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        