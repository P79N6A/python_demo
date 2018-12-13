import turtle


# 每一截线段的长度还有科赫雪花的阶数
def kno(size, n):
    if n == 0:  # 0阶就是画条线
        turtle.fd(size)
    else:
        for i in [0, 60, -120, 60]:  # 画比他低的阶数
            turtle.left(i)
            kno(size / 3, n - 1)


def main():
    turtle.setup(800, 400)  # 设置画布的大小还有出现的位置
    turtle.pensize(2)  # 画笔的大小
    turtle.penup()
    turtle.goto(-300, 100)  # 画笔在画布上的位置
    turtle.pendown()
    for i in range(1, 4):  # 三个科赫合体
        kno(300, 3)
        turtle.right(120)
    turtle.hideturtle()  # 画笔隐藏
    turtle.done()  # 暂停


main()
