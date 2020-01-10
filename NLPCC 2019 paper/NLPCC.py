import requests
from lxml import etree

# 1. 获取NLP论文GitHub地址网页源码
result = requests.get('http://tcci.ccf.org.cn/conference/2019/pro_session.php').content
# 2. 解析页面并获取所有论文标题名称
html = etree.HTML(result)
names = html.xpath("//div[@class='programtitle']/a/span")
print(len(names))
# 4. 获取所有论文链接地址，并存储在resu列表里 579条记录
resu = []
links = html.xpath("//div[@class='programtitle']/a/@href")
for link in links:
    if link.startswith('/login'):
        continue
    if link.startswith('https://scholar.google.com'):
        continue
    if link.endswith('en'):
        continue
    resu.append(link)
# 5. 下载单个论文函数
def download2(name, url):
    try:
        print('Downlodaing '+str(name)+' '+str(url))
        r = requests.get(url,stream=True)
        with open(name,'wb') as pdf:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)
    except:
        pass
# 6. 下载论文
for i in range(len(names)):
    download2(names[i], resu[i])