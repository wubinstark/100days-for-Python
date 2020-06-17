# 模拟掷骰子

import random
import numpy as np
import matplotlib.pyplot as plt

p_list = []


# 掷骰子类
class Roll:
    def __init__(self):
        roll_num = 0

    def roll_dice(self):
        roll_num = random.randint(1, 6)
        return roll_num


def main():
    times = 10000

    roll_num_sum = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    roll_list = [0] * 11
    roll_list_now = []
    roll_dicotionary = dict(zip(roll_num_sum, roll_list))

    # 散点图数据
    roll1_list = []
    roll2_list = []

    # 实例化roll
    roll = Roll()

    for i in range(times):
        # 调用roll中的roll_dice方法
        roll_01 = roll.roll_dice()
        roll_02 = roll.roll_dice()

        roll1_list.append(roll_01)
        roll2_list.append(roll_02)

        for j in range(2, 13):
            if (roll_01 + roll_02) == j:
                roll_dicotionary[j] += 1

    for i, result in roll_dicotionary.items():
        print("点数{}出现的次数是{}，概率是{}".format(i, result, result / times))
        global p_list
        p_list.append(result / times)

    # 数据可视化
    plt.stem(roll_num_sum, p_list, use_line_collection=True)
    plt.show()


if __name__ == '__main__':
    main()
