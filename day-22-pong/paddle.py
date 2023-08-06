import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__(shape="square")
        self.speed(0)
        self.color("white")
        self.shapesize(stretch_wid=6, stretch_len=2)
        self.penup()
        self.goto(x, y)

    def paddle_up(self):
        y = self.ycor()
        if y < 250:
            y += 20
        self.sety(y)

    def paddle_down(self):
        y = self.ycor()
        if y > -240:
            y -= 20
        self.sety(y)
