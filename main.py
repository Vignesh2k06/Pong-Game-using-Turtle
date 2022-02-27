from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

# Dividing the screen
sree = Turtle()
sree.shape("square")
sree.color("white")
sree.setheading(270)
sree.pensize(5)
sree.pu()
sree.goto(0, 300)
for i in range(60):
    sree.pd()
    sree.forward(10)
    sree.pu()
    sree.forward(20)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

ball = Ball()

score = Scoreboard()
lscore = 0
rscore = 0

while True:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # colliding with upper and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # colliding with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # Resetting a new ball
    if ball.xcor() > 380:
        ball.refresh()
        lscore += 1
        ball.move_speed = 0.1
        score.scores(rscore, lscore)

    if ball.xcor() < -380:
        ball.refresh()
        rscore += 1
        ball.move_speed = 0.1
        score.scores(rscore, lscore)

screen.exitonclick()
