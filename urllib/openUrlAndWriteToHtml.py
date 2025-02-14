from urllib.request import urlopen

myURL = urlopen("https://eco.dameng.com/document/dm/zh-cn/app-dev/java-jdbc.html")
f = open("runoob_urllib_test.html", "wb")
content = myURL.read()  # 读取网页内容
f.write(content)
f.close()