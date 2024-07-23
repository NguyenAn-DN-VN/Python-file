from turtle import Turtle, Screen
from tay import Tay
import time
from bong import Bong
from diem import Diem
from ban import Ban

screen = Screen()
screen.title("Bong Ban")
screen.setup(width= 800, height=600)
screen.bgcolor("black")
screen.tracer(0)
bang_diem = Diem()
Bong = Bong()
ban = Ban()
tay_p = Tay((380, 0))
tay_tr = Tay((-380, 0))
game_chay = True
while game_chay:
    screen.listen()
    screen.onkey(tay_p.len, "Up")
    screen.onkey(tay_p.xuong, "Down")
    screen.onkey(tay_tr.len, "w")
    screen.onkey(tay_tr.xuong, "s")
    Bong.Bong_chay()
    if Bong.ycor() > 270 or Bong.ycor() < -270:
        Bong.Bat_doc()
    if Bong.distance(tay_tr) < 30 and Bong.xcor()<370 or Bong.distance(tay_p) < 30 and Bong.xcor() > -370:
        Bong.Bat_ngang()
    if Bong.xcor() > 400:
        Bong.Lai()
        bang_diem.cong_diemtr()
    if Bong.xcor() < -400:
        Bong.Lai()
        bang_diem.cong_diemp()
    time.sleep(0.1)
    screen.update()

















screen.exitonclick()