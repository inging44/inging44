# coding : utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imgList = re.findall(imgre, html)
    print len(imgList)
    x = 0
    for imgurl in imgList:
        # urllib.urlretrieve(imgurl, '/img2/%s.jpg' % x)
        x += 1
    return " "
html = getHtml('http://tieba.baidu.com/p/2460150866')
print getImg(html)
