# import urllib.request
from urllib.request import urlopen
from lxml import etree

# 使用Chrome浏览器的[XPath Helper]拓展程序获取所有网址和名字并存到相应的txt中

# 获取所有要爬取的网址链接
with open('links.txt', 'r') as f:
    links = f.readlines()

# 获取所有音频的名字
with open('names.txt', 'r') as f: 
    names = f.readlines()
    names = [i.strip() for i in names]

# 获取所有音频的链接
parse = etree.HTMLPullParser()
mp3_links = []
for link in links:
    with urlopen(link) as f:
        tree = etree.parse(f, parse)
        mp3_link = tree.xpath('//div/dl[@class="fr intro "]/dd/input[@id="mp3"]/@value')
        mp3_links.append(mp3_link)
    
# 下载所有音频
for i in range(len(mp3_links)):
    link = mp3_links[i][0]
    try:
        response = urllib.request.urlopen(link).read()
        with open('%s.mp3'%names[i], 'wb') as f: 
            f.write(response)
    except:
        print(link + ' is not found.')