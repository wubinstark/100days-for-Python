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

    days = date.strftime('%j')

    print('{}是全年的第{}天'.format(input_date, days))


if __name__ == '__main__':
    main()
