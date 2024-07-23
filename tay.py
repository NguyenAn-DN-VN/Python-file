from turtle import Turtle
class Tay(Turtle):
    def __init__(self,vi_tri):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(vi_tri)
        self.shapesize(stretch_wid=5,stretch_len =1)
    def len(self):
        if self.ycor() < 280:
            self.goto(self.xcor(),self.ycor()+30)
    def xuong(self):
        if self.ycor() > -280:
            self.goto(self.xcor(), self.ycor() - 30)
