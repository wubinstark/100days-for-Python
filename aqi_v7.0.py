#
# AQI_V7.0
# 网络爬虫只requests请求
# 需求：用Python获取网站的城市AQI
#

import requests
from bs4 import BeautifulSoup
import csv


def get_city_aqi(pinyin):
    url = 'http://pm25.in/' + pinyin

    # 通过requests网络请求，获取对应URL的文本信息
    r = requests.get(url, timeout=120)

    # 解析网页，找到AQI对应的字段（其实就是实例化一个BeautifulSoup的类对象，然后再调用它）
    soup = BeautifulSoup(r.text, 'lxml')

    # 解析网站之后，去寻找想要的数据
    # find_all 是拿到相应div中的所有值，并不是拿到解析网页中的所有div
    aqi_list = soup.find_all('div', {'class': "span1"})
    i = 0
    aqi_val = []
    for i in range(8):
        aqi_item = aqi_list[i]
        value = aqi_item.find('div', {'class': 'value'}).text.strip()
        aqi_val.append(value)
    return aqi_val


def get_all_city():
    city_list = []
    url = 'http://pm25.in/'
    r = requests.get(url, timeout=120)
    soup = BeautifulSoup(r.text, 'lxml')
    city_div = soup.find_all('div', {'class': 'bottom'})[1]
    city_link_list = city_div.find_all('a')
    for city_link in city_link_list:
        city_name = city_link.text
        city_pinyin = city_link['href'][1:]
        city_list.append((city_name, city_pinyin))
    return city_list


def main():
    city_list = get_all_city()
    # 创建表头
    header = ['城市', 'AQI', 'PM2.5', 'PM10', 'CO', 'NO2', 'O3/1h', 'O3/8h', 'SO2']
    with open('china_city_aqi.csv', 'w', newline='', encoding='utf-8') as f:
        xxx = csv.writer(f)
        # 写入表头
        xxx.writerow(header)
        # 写入表格数据
        for city in city_list:
            city_name = city[0]
            city_aqi = get_city_aqi(city[1])
            print(city_name, city_aqi)
            row = [city_name] + city_aqi
            xxx.writerow(row)


if __name__ == '__main__':
    main()
