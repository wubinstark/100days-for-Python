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
    # print('基本信息')
    # print(aqi_data.info())

    # 排名前十个城市
    top_city_aqi = aqi_data.sort_values(by='AQI').head(10)
    print('空气质量排名前十的城市：')
    print(top_city_aqi)
    print()

    # 空气质量最差的十个城市
    bottom_city_aqi = aqi_data.sort_values(by='AQI').tail(10)
    print('空气质量最差的十个城市：')
    print(bottom_city_aqi)

    top_city_aqi.to_csv('top10.csv',index = False)

if __name__ == '__main__':
    main()
