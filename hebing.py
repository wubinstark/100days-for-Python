import os
import pandas as pd

# 将文件读取出来放一个列表里面

pwd = '/Users/wubin/Downloads/客情汇总'  # 获取文件目录

# 新建列表，存放文件名
file_list = []

# 新建列表存放每个文件数据(依次读取多个相同结构的Excel文件并创建DataFrame)
dfs = []

for root, dirs, files in os.walk(pwd):
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path)
        df = pd.read_excel(file_path)
        dfs.append(df)

# 将多个DataFrame合并为一个
df = pd.concat(dfs)

# 写入excel文件，不包含索引数据
df.to_excel('test\\result.xls', index=False)
