# 设置汇率常识
rate = 7

# 让用户输入带单位的金额
currency_unit = input('请输入带单位的金额：')

# 取出金额的单位，并保存
unit = currency_unit[-3:]

# 判断用户输入的货币单位
if unit == 'cny':
    output_currency = eval(currency_unit[:-3]) / rate
    print('您输入的是人民币：', output_currency)
elif unit == 'usd':
    output_currency = eval(currency_unit[:-3]) * rate
    print('您输入的是美元:', output_currency)
else:
    print('您输入的货'
          '3币目前不支持转换，请重新输入')
