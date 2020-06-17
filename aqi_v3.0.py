#
# AQI_V2.0
# aqi之引入json
#

import json
import csv


def decode_jsonfile(filepath):
    # 解码json文件
    # f = open(filepath, encoding='utf-8', mode='r')
    # city_list = json.load(f)
    # return city_list
    with open(filepath, encoding='utf-8', mode='r') as f:
        city_list = json.load(f)
    print(city_list)
    return city_list

def main():
    # 让用户输入文件路径
    filePath = input('请输入文件名称：')

    # 引入json文件的函数
    aqi_city_list = decode_jsonfile(filePath)

    # json数据进行排序
    aqi_city_list.sort(key=lambda city: city['aqi'])

    # 把json文件转化为CSV格式
    lines = []
    #取到json文件的中，数据的key作为csv的第一行（列名）
    lines.append(list(aqi_city_list[0].keys()))

    # 遍历json文件中元素的每一项数据的value值，作为数据
    for block in aqi_city_list:
        lines.append(list(block.values()))

    # 将lines列表的数据保存在CSV文件中
    f = open('city.csv',mode='w',newline='')
    writer = csv.writer(f)
    for line in lines:
        writer.writerow(line)
    f.close()

if __name__ == '__main__':
    main()
