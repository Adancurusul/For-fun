

url="https://blog.csdn.net/Adancurusul/article/details/105764387"

__author__ = 'MrChen'

import urllib.request
import time

# 使用build_opener()是为了让python程序模仿浏览器进行访问
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]

# 专刷某个页面
print('开始刷了哦：')
tempUrl = url
for j in range(10000):
    try:
        opener.open(tempUrl)
        print('%d %s' % (j, tempUrl))
    except urllib.error.HTTPError:
        print('urllib.error.HTTPError')
        time.sleep(1)
    except urllib.error.URLError:
        print('urllib.error.URLError')
        time.sleep(1)
    time.sleep(0.2)


