# 判断第几天——用元组的方式
import datetime


def is_run_year(year):
    # 默认平年
    run_num = 0

    # 判断闰年的方法
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        run_num = 1

    return run_num


def main():
    # 让用户输入年份
    input_date = input('请输入一个日期（如，2020-02-11）：')

    # 解析用户输入的日期
    date = datetime.datetime.strptime(input_date, '%Y-%m-%d')
    year = date.year
    month = date.month
    day = date.day

    # 调用判断闰年的函数
    run_num = is_run_year(year)

    # 用字典数据类型解题
    day_months_dictonary = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    days = 0
    days = days + day
    for i in range(1, month):
        days = days + day_months_dictonary[i]

    if run_num == 1 and month > 2:
        days = days + run_num

    print('{}是全年的第{}天'.format(input_date, days))


if __name__ == '__main__':
    main()
