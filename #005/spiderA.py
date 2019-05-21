'''
GTD:多线程，提高运行速度
'''
import re
import requests
from lxml import etree
def get_xici_proxy(page_no):
    url = "https://www.xicidaili.com//nn/{}".format(page_no)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"}
    r = requests.get(url, verify=True, headers=headers)
    content = r.content.decode("utf-8")
    root = etree.HTML(content)
    tr_nodes = root.xpath('.//table[@id="ip_list"]/tr')[1:]
    result = []
    for tr_node in tr_nodes:
        td_nodes = tr_node.xpath('./td')
        ip = td_nodes[1].text
        port = td_nodes[2].text
        proxy_type = td_nodes[4].text
        proto = td_nodes[5].text
        proxy = "{}://{}:{}".format(proto.lower(), ip, port)
        uptime = td_nodes[8].text
        if proxy_type == "高匿" and proto.lower() == "https":
            result.append(proxy)
    return result
def dotest_proxy(proxy,url):
    # https_url = "https://book.douban.com/tag/SQL?start=20&type=T"
    # headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
    # try:
    #     proxies = {"https": proxy}
    #     r = requests.get(https_url, headers=headers, verify=True, proxies=proxies, timeout=2)
    #     content = r.content.decode("utf-8")
    #     root = etree.HTML(content)
    #     items = root.xpath('.//li[@class="subject-item"]')
    #     #print(r.status_code)
    #     if r.status_code == 200 and len(items) == 20:
    #         return True
    #     return False
    # except Exception as e:
    #     msg = str(e)
    #     return False
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    try:
        proxies = {"https": proxy}
        r = requests.get(url, headers=headers, verify=True, proxies=proxies, timeout=2)
        content = r.content.decode("utf-8")
        root = etree.HTML(content)
        items = root.xpath('.//div[@class="content"]')
        if r.status_code == 200 and len(items) > 1:
            return True
    except Exception as e:
        msg = str(e)
        return False
'''
#url:需要爬取的网址
#page：需要在代理网站爬取的页数
'''
def good_IP(url,page):
    for j in range(page):
        result = get_xici_proxy(j)
        for i in result:
            if(dotest_proxy(i,url)):
                print(i)

if __name__ == '__main__':
    url = "https://www.jianshu.com/"
    good_IP(url,10)