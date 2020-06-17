#
# AQI_V4.0
# 网络爬虫只requests请求
# 需求：用Python获取网站的城市AQI
#
import requests

def main():
    # 要求用户输入城市全拼，并拼接成URL
    city_name = input('请输入城市的全拼：')
    url = 'http://pm25.in/' + city_name

    # 通过requests网络请求，获取对应URL的文本信息
    r = requests.get(url)
    # print(r.status_code)

    url_text = r.text
    # print(url_text)

    aqi_div = '''<div class="span12 data">
        <div class="span1">
          <div class="value">
            '''
    index = url_text.find(aqi_div)
    begin_index = index+len(aqi_div)
    end_index = begin_index+3
    aqi_val = url_text[begin_index:end_index]
    print('所在城市对应的AQI为：{}'.format(aqi_val))


if __name__ == '__main__':
    main()
