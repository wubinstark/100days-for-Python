import re

# 爬虫学习
content = 'price is $5.00'
print(len(content))
result = re.match('^price is \$5\.00$',content)
print(result)
# print(result.group(1))
# print(result.span())

