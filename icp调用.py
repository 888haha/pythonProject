import urllib.request
import urllib
import sys
host = 'http://www.beiancx.cn'
path = '/icpcx?url_long'
method = 'GET'
querys = 'url_long=http%3A%2F%2Fwww.baidu.com'
bodys = {}
url = host + path + '?' + querys
request = urllib.request.urlopen(url)
content = request.read()
if (content):
    print(content)