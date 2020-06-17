# 模拟掷骰子

import random
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['PingFang']

p_list = []


# 掷骰子类
class Roll:
    def __init__(self):
        roll_num = 0

    def roll_dice(self):
        roll_num = random.randint(1, 6)
        return roll_num


def main():
    # 构建数据
    roll_list = []

    # 实例化roll
    roll = Roll()
    times = 10000

    for i in range(times):
        roll_num = roll.roll_dice() + roll.roll_dice()

        roll_list.append(roll_num)

    # 数据可视化
    plt.hist(roll_list, range(2, 14), normed=1)
    plt.title('掷骰子的概率分布')
    plt.xlabel('骰子点数')
    plt.ylabel('概率')
    plt.show()


if __name__ == '__main__':
    main()
