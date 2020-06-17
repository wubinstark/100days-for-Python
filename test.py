import turtle


# 递归函数绘制五角星
def drawStar_digui(size):
    # 第一次绘制五角星
    i = 0
    while i < 5:
        turtle.forward(size)
        turtle.right(144)
        i = i + 1

    size = size + 10
    # 设置递归次数
    if size <= 90:

        # 递归
        drawStar_digui(size)


def main():
    size = 50
    # 调用递归函数
    drawStar_digui(size)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
