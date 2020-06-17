import turtle


def shuzhi(shuzhichang):
    if shuzhichang <= 5:
        turtle.color('red')

    if shuzhichang > 5:
        # 绘制右侧树枝
        turtle.forward(shuzhichang)
        print('前 ', shuzhichang)
        turtle.right(20)
        print('右转 20')
        shuzhi(shuzhichang - 15)

        # 绘制左边的树枝
        turtle.left(40)
        print('左转 40')
        shuzhi(shuzhichang - 15)

        # if 0 < shuzhichang <= 15:
        #     turtle.color('blue')
        # 返回前树枝
        turtle.right(20)
        print('右转 20')
        turtle.backward(shuzhichang)
        print('右退 ', shuzhichang)
        turtle.color('blue')


def main():
    turtle.penup()
    turtle.left(90)
    turtle.backward(150)
    turtle.pendown()

    shuzhi(63)
    turtle.exitonclick()


if __name__ == '__main__':
    main()
