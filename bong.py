from turtle import Turtle
class Bong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.gocx = 10
        self.gocy = 10
    def Bong_chay(self):
        a = self.xcor()+self.gocx
        b = self.ycor()+self.gocy
        self.goto(a, b)
    def Bat_doc(self):
        self.gocy *= -1
    def Bat_ngang(self):
        self.gocx *= -1
    def Lai(self):
        self.goto(0,0)
