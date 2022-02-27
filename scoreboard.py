from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score(0)
        self.r_score(0)

    def l_score(self, score):
        self.setpos(-150, 200)
        self.write(f"{score}", font=('Arial', 60, "bold"))

    def r_score(self, score):
        self.setpos(100, 200)
        self.write(f"{score}", font=('Arial', 60, "bold"))

    def scores(self, rscore, lscore):
        self.clear()
        self.r_score(rscore)
        self.l_score(lscore)
