import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.speed(1)
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 0.15
        self.dy = 0.15

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def border_collision(self):
        if self.ycor() > 290 or self.ycor() < -290:
            self.dy *= -1

    def paddle_collision(self, paddle):
        if (self.dx > 0) and (350 > self.xcor() > 340) and (paddle.ycor() + 50 > self.ycor() > paddle.ycor() - 50):
            self.dx *= -1
        elif (self.dx < 0) and (-350 < self.xcor() < -340) and (paddle.ycor() + 50 > self.ycor() > paddle.ycor() - 50):
            self.dx *= -1

    def check_score(self):
        if self.xcor() > 390:
            self.goto(0, 0)
            self.dx *= -1
            # Increase player A's score
            # Your scoring code here

        if self.xcor() < -390:
            self.goto(0, 0)
            self.dx *= -1
            # Increase player B's score
            # Your scoring code here
