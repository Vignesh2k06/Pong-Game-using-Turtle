from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cor):
        super().__init__()
        self.create_paddle(cor)

    def create_paddle(self, cor):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.pu()
        self.speed("fastest")
        self.goto(cor)

    def go_up(self):
        pos = self.ycor() + 20
        self.goto(self.xcor(), pos)

    def go_down(self):
        pos = self.ycor() - 20
        self.goto(self.xcor(), pos)

