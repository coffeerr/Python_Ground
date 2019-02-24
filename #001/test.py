import requests
from lxml import etree
url = 'https://book.douban.com/tag/%E5%8E%86%E5%8F%B2'
proxy = '112.85.164.23:9999'
proxies = {
    'http': 'http://' + proxy,
    'https': 'https://' + proxy,
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
}
text = requests.get(url,headers=headers,proxies = proxies).text
html = etree.HTML(text)
bookName = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/h2/a/text()')
bookInfo = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/div[1]/text()')
bookScore = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/div[2]/span[2]/text()')
bookCover = html.xpath('//*[@id="subject_list"]/ul/li//div[1]/a/img/@src')
bname = []
for i in range(len(bookName)):
    bookName[i] = bookName[i].strip()
    if(bookName[i]!=''):
        bname.append(bookName[i])
item = {}
for i in range(20):
    item['bookName'] = bname[i]
    item['bookInfo'] = bookInfo[i].strip()
    item['bookScore'] = bookScore[i]
    item['bookCover'] = bookCover[i]
    print(item)