import requests

def main():
    response = requests.get('http://www.baidu.com')
    print(response.status_code)
    print(type(response))
    # print(response.text)
    print(response.cookies)

if __name__ == '__main__':
    main()
