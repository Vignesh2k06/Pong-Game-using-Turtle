from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.new_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def new_ball(self):
        self.shape("circle")
        self.color("white")
        self.pu()

    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def refresh(self):
        self.setpos(0, 0)

