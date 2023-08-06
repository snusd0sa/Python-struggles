
import turtle
from ball import Ball
from paddle import Paddle

# Set up the game window
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# Create paddles
paddle_a = Paddle(-350, 0)
paddle_b = Paddle(350, 0)

# Create the ball
ball = Ball()

# Keyboard bindings
win.listen()
win.onkeypress(paddle_a.paddle_up, "w")
win.onkeypress(paddle_a.paddle_down, "s")
win.onkeypress(paddle_b.paddle_up, "Up")
win.onkeypress(paddle_b.paddle_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.move()

    # Border collision
    ball.border_collision()

    # Paddle collisions
    ball.paddle_collision(paddle_a)
    ball.paddle_collision(paddle_b)

    # Scoring
    ball.check_score()
