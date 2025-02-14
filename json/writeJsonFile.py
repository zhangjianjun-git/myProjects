#!/usr/bin/python3

import json

data = {
   "name": "John",
   "age": 30,
   "city": "New York"
}

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)

for key, value in data.items():
    print(key, ":", value)