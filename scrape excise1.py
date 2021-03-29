# coding: utf-8

from urllib import request
from urllib import parse

url = "http://imax.maoyan.com/dashboard"
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

result = request.Request(url, headers=header)
#print(result)
resp = request.urlopen(result)

print(resp.read().decode())