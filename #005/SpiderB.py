import requests
from lxml import etree
url = "https://www.jianshu.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            }
r = requests.get(url,headers=headers)
content = r.content.decode("utf-8")
root = etree.HTML(content)
items = root.xpath('.//div[@class="content"]')
if r.status_code == 200 and len(items) > 1:
    print("good!")