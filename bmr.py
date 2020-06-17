def bmr(gender, age, weight_body, height_body):
    if gender == '男':
        bmr = (13.7 * weight_body) + (5.0 * height_body) - (6.8 * age) + 66
    elif gender == '女':
        bmr = (9.6 * weight_body) + (1.8 * height_body) - (4.7 * age) + 655
    else:
        bmr = -1

    return bmr


def main():
    i = 'n'

    while i == 'n':
        gender = input('性别：')

        if gender != '男' and gender != '女':
            print('您输入的性别有误,请重新输入')
            continue

        # age = int(input('年龄：'))
        #
        # weight_body = float(input('体重(kg)：'))
        #
        # height_body = float(input('身高(cm)：'))

        print('请输入以下信息，并用逗号隔开')
        in_str_list = input('年龄，体重，身高：')
        str_list = in_str_list.split('，')

        age = int(str_list[0])
        weight_body = float(str_list[1])
        height_body = float(str_list[2])

        out_bmr = bmr(gender, age, weight_body, height_body)

        print('您的性别：{}，年龄：{} 岁，体重：{} 公斤，身高：{} 厘米'.format(gender,age,weight_body,height_body))
        print('您的基础代谢率为：{} 大卡'.format(out_bmr))

        i = input('是否退出程序：y/n?')

    print('您已经退出程序，感谢您的使用')


if __name__ == '__main__':
    main()
