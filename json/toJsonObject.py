#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'https://www.runoob.com'
}

# 将字典转换为 JSON 对象
json_str = json.dumps(data)

# 输出结果
print("Python 原始数据：", repr(data))
print("JSON 对象：", json_str)