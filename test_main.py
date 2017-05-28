# coding = utf-8
import urllib
import re

def gethtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getimg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    x = 0
    # print imgList[0]
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, 'img/%s.jpg' % x)
        x += 1

html = gethtml('http://tieba.baidu.com/p/2460150866')
print getimg(html)
