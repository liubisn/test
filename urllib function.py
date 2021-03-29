#coding: utf-8
from urllib import request
from urllib import parse

resp = request.urlopen('http://www.baidu.com')

print(resp.read())

request.urlretrieve('http://www.baidu.com','baidu.html')

data = {"name":"老王", 'age':18, 'greet':'hello world'}

qs = parse(data)

