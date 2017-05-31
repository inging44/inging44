# coding:utf-8
import requests
url = "http://wx.kuaijiankang.com/interface/dataService"

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Content-Type": "application/json; charset=utf-8",
            # "VerificationToken": "",
            "X-Requested-With": "XMLHttpRequest",
            # "Referer": "",
            "Content-Length": "385",
            "Cookie": "xxx...",  # 此处省略
            "Connection": "keep-alive"
            }

payload = {'method': 'userLogin', 'mobile': '13990122270', 'password': '111111',
           'unique_id': 'sdfsdgsdfsf', 'is_web': '1'}

r = requests.post(url, json=payload, headers=headers)
print r
print r.json()
