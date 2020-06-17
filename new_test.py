"""
    52周存钱挑战
"""
import math

def save_money_in_n_weeks(money_per_week, increase_money, total_week):
    """
        计算n周内存款金额
    """

def main():

    money_per_week = float(input('请用户输入每周存入的金额：'))  # 每周存入的金额
    increasez_money = float(input('请输入每周递增的金额：'))
    total_week = int(input('请输入存钱周数：'))
    saving = 0
    money_list = []     #记录每周存款数列表



    for i in range(total_week):
        money_list.append(money_per_week)
        saving = math.fsum(money_list)


        print('第{}周, 存入{}元, 账户累计{}元'.format(i+1, money_per_week, saving))
        money_per_week += increasez_money





if __name__ == '__main__':
    main()
