from turtle import Turtle
class Diem(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.diem_p = 0
        self.diem_tr = 0
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.write(f"Ben A:{self.diem_p}   Ben B:{self.diem_tr}", False,  align="center", font=("Courier", 80, "normal"))
    def cong_diemp(self):
        self.clear()
        self.diem_p += 1
        self.write(f"Ben A:{self.diem_p}   Ben B:{self.diem_tr}", False, align="center", font=("Courier", 80, "normal"))
    def cong_diemtr(self):
        self.clear()
        self.diem_tr += 1
        self.write(f"Ben A:{self.diem_p}   Ben B:{self.diem_tr}", False, align="center", font=("Courier", 80, "normal"))