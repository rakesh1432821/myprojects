from turtle import Turtle

class score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_scre = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-200,200)
        self.write(f"left score: {self.l_score}", align="center")
        self.goto(200, 200)
        self.write(f"Right score: {self.r_scre}", align="center")

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_scre += 1
        self.update_score()