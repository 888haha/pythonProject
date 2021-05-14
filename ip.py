import requests
try:
	r = requests.get('http://icp.chinaz.com/baidu.com')
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.text[-500:])
except:
	print("爬取失败")

