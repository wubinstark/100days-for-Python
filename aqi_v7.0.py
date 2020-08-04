#
# AQI_V7.0
# 网络爬虫只requests请求
# 需求：用Python获取网站的城市AQI
#

import requests
from bs4 import BeautifulSoup


def get_city_aqi(pinyin):
    url = 'http://pm25.in/' + pinyin

    # 通过requests网络请求，获取对应URL的文本信息
    r = requests.get(url, timeout=120)

    # 解析网页，找到AQI对应的字段（其实就是实例化一个BeautifulSoup的类对象，然后再调用它）
    soup = BeautifulSoup(r.text, 'lxml')

    # 解析网站之后，去寻找想要的数据
    if soup.find('div', {'class': 'caption'}).text.strip() == 'AQI':
        aqi_val = soup.find('div', {'class': 'value'}).text.strip()
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
    for city in city_list:
        city_name = city[0]
        city_aqi = get_city_aqi(city[1])
        print(city_name, city_aqi)


if __name__ == '__main__':
    main()
