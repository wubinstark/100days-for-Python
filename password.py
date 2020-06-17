# 判断密码强弱1.0

class PasswordTool:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def password_ok(self):

        # 规则1：密码至少有八位
        if len(self.password) >= 8:
            self.strength_level += 1
        else:
            print('密码至少有八位')

        # 规则2：密码要有字母
        for i in self.password:
            if i.isalpha():
                break
        if i.isalpha():
            self.strength_level += 1
        else:
            print('密码要有字母')

        # 规则3：密码要有数字
        for i in self.password:
            if i.isnumeric():
                break
        if i.isnumeric():
            self.strength_level += 1
        else:
            print('密码要有数字')

        return self.strength_level


def main():
    password = input('请输入一个密码：')
    cishu = 1

    # 实例化PasswordTool类对象
    password_tool = PasswordTool(password)

    # 调用判断密码强弱的函数
    strength_level = password_tool.password_ok()
    while strength_level != 3 and cishu < 4:
        print('密码不符合规定，至少有8位，字母和数字混合')
        cishu += 1
        password = input('请重新输入密码：')

        # 实例化PasswordTool类对象
        password_tool = PasswordTool(password)
        strength_level = password_tool.password_ok()

        # 将密码写入文件
        f = open('password_text.txt', mode='a')
        f.write("密码：{},强度：{}\n".format(password, strength_level))

    if strength_level != 3:
        print('您已经连续4次输入错误，明天再来尝试')
    else:
        print('成功')


if __name__ == '__main__':
    main()
