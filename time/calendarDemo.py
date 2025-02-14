#!/usr/bin/python3

import calendar
import time

cal = calendar.month(2016, 1)
print ("以下输出2016年1月份的日历:")
print (cal)

print("返回系统运行时间:",time.perf_counter())  # 返回系统运行时间
print("返回进程运行时间:",time.process_time()) # 返回进程运行时间
print("返回当前时区:",	time.timezone) # 返回当前时区


