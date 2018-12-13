# 七段数码管 有七个线条 从最中间的一条向右向下开始绘制
# 代码结构
# draw_line 用来绘制一条直线
# drawDigit 用来绘制绘制对应数字

import turtle
import time


def draw_init():
    turtle.setup(900, 200, 200, 200)
    turtle.penup()
    turtle.fd(-350)
    turtle.pensize(5)


def draw_line(draw):
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    turtle.right(90)


def draw_digit(digit):
    draw_line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 6, 8, 9] else draw_line(False)
    turtle.left(90)  # 向前
    draw_line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    turtle.right(180)  # 回到初始


def draw_next():
    turtle.penup()
    turtle.fd(40)


def draw_data(date):
    draw_init()
    turtle.pencolor('red')
    for i in date:
        if i == '-':
            turtle.write('年')
            turtle.pencolor('green')
        elif i == '+':
            turtle.write('月')
        elif i == '=':
            turtle.write('日')
        else:
            draw_digit(eval(i))  # 为什么不在main里直接用eval  直接用它会得到这个20181127这个大树
        draw_next()
    draw_end()


def draw_end():
    turtle.hideturtle()
    turtle.done()


def main():
    draw_data(time.strftime("%Y-%m+%d=", time.localtime()))


main()
