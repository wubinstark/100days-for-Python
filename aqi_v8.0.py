#
# AQI_V7.0
# 网络爬虫只requests请求
# 需求：用Python获取网站的城市AQI
#

import pandas as pd


def main():
    aqi_data = pd.read_csv('china_city_aqi.csv')
    # print(aqi_data.head(5))
    # print(aqi_data.min())
    print('基本信息')
    print(aqi_data.info())
if __name__ == '__main__':
    main()
