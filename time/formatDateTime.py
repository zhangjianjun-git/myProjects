from datetime import datetime

# 获取当前时间
now = datetime.now()

# 格式化时间，例如：年-月-日 时:分:秒
formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("当前时间:", formatted_now)


# 将特定的时间字符串转换为 datetime 对象并格式化：
# 时间字符串
time_str = "2021-09-01 12:30:45"

# 将字符串解析为 datetime 对象
time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S ")

# 重新格式化
new_format = time_obj.strftime("%d/%m/%Y %I:%M %p")
print("格式化后的时间:", new_format)
