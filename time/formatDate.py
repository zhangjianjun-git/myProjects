from datetime import date
"""
strftime 方法中的格式代码可以参考以下表格：
%Y：四位数的年份（例：2021）
%m：两位数的月份（01 到 12）
%d：两位数的日期（01 到 31）
%H：24小时制的小时（00 到 23）
%I：12小时制的小时（01 到 12）
%M：分钟（00 到 59）
%S：秒（00 到 59）
%p：AM 或 PM
"""
# 获取当前日期
today = date.today()

# 格式化为“日/月/年”
formatted_today = today.strftime("%Y/%m/%d %p %w")
print("当前日期:", formatted_today)

# 格式化为“月-日-年”
formatted_today2 = today.strftime("%Y-%m-%d")
print("当前日期:", formatted_today2)