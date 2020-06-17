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
        roll_num = np.random.randint(1, 6, (1000, 1))
        return roll_num


def main():
    # 构建数据
    roll_list = []
    times = 10000000

    roll_list = np.random.randint(1, 7, size=times) + np.random.randint(1, 7, size=times)+ np.random.randint(1, 7, size=times)

    # 数据可视化
    plt.hist(roll_list, bins=range(3, 20), normed=1, rwidth=0.8)

    # 设置x轴的坐标显示
    tick_pos = np.arange(2, 19) + 0.5
    tick_xlabel = ['3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点','13点','14点','15点','16点','17点','18点',]

    plt.xticks(tick_pos, tick_xlabel)

    plt.title('掷骰子的概率分布')
    plt.xlabel('骰子点数')
    plt.ylabel('概率')
    plt.show()


if __name__ == '__main__':
    main()
