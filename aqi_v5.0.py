#
# AQI_V4.0
# 网络爬虫只requests请求
# 需求：用Python获取网站的城市AQI
#
import requests
from bs4 import BeautifulSoup


def get_city_url(url):
    # 通过requests网络请求，获取对应URL的文本信息
    r = requests.get(url, timeout=30)

    # 解析网页，找到AQI对应的字段（其实就是实例化一个BeautifulSoup的类对象，然后再调用它）
    soup = BeautifulSoup(r.text, 'lxml')

    # 解析网站之后，去寻找想要的数据
    if soup.find('div', {'class': 'caption'}).text.strip() == 'AQI':
        aqi_val = soup.find('div', {'class': 'value'}).text.strip()
    return aqi_val


def main():
    # 要求用户输入城市全拼，并拼接成URL
    city_name = input('请输入城市的全拼：')
    url = 'http://pm25.in/' + city_name
    aqi_val = get_city_url(url)

    print('所在城市对应的AQI为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
