import requests

def main():
    response = requests.get('http://old.ibos.ixuenong.com/')
    print(response.status_code)
    print(type(response))
    print(response.text)
    # print(response.cookies)
    # print(response.headers)

if __name__ == '__main__':
    main()
