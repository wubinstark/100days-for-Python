#
# AQI_V2.0
# aqi之引入json
#

import json


def decode_jsonfile(filepath):
    # 解码json文件
    f = open(filepath, encoding='utf-8', mode='r')
    city_list = json.load(f)
    return city_list


def main():
    # 让用户输入文件路径
    filePath = input('请输入文件名称：')

    # 引入json文件的函数
    aqi_city_list = decode_jsonfile(filePath)

    # json数据进行排序
    aqi_city_list.sort(key=lambda city: city['aqi'])

    top5_list = aqi_city_list[0:5]
    print(top5_list)

    # 将新的排序文件保存到新的文件
    # 打开文件，如果没有文件，默认新建文件
    f = open('top5_aqi.json', mode='w', encoding='utf-8')
    json.dump(top5_list, f, ensure_ascii=False)
    f.close()


if __name__ == '__main__':
    main()
