#V0.1 基本的爬取
import requests
import time
from lxml import etree

class douban():
    #get books in one page
    def __init__(self):
        self.proxy = '125.123.137.247:9999'
        self.proxies = {
            'http': 'http://' + self.proxy,
            'https': 'https://' + self.proxy,
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        }
    def get_one_page(self,url):
        '''
        爬取一页的书籍
        :param url:当前页的链接
        :return: item包含一本书的信息
        '''
        booklist = []
        text = requests.get(url, headers=self.headers).text
        time.sleep(1.5)
        html = etree.HTML(text)
        bookName = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/h2/a/text()')
        bookInfo = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/div[1]/text()')
        bookScore = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/div[2]/span[2]/text()')
        bookCover = html.xpath('//*[@id="subject_list"]/ul/li//div[1]/a/img/@src')
        bname = []
        for i in range(len(bookName)):
            bookName[i] = bookName[i].strip()
            if (bookName[i] != ''):
                bname.append(bookName[i])
        for i in range(len(bname)):
            item = {}
            item['bookName'] = bname[i]
            item['bookInfo'] = bookInfo[i].strip()
            item['bookScore'] = bookScore[i]
            item['bookCover'] = bookCover[i]
            booklist.append(item)
        return booklist
    def write_to_mysql(self,item):
        # !/usr/bin/python3
        import pymysql
        # 打开数据库连接
        db = pymysql.connect("localhost", "root", "root", "doubanbook")
        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 插入语句
        bookName = item['bookName']
        bookScore = item['bookScore']
        bookInfo = item['bookInfo']
        bookCover = item['bookCover']
        sql = """INSERT INTO doubanbook 
                 VALUES (null, '%s','%s','%s','%s')"""
        try:
            # 执行sql语句
            cursor.execute(sql % (str(bookName),str(bookScore),str(bookInfo),str(bookCover)))
            # 提交到数据库执行
            db.commit()
        except:
            # 如果发生错误则回滚
            print(item)
            print("插入失败")
            db.rollback()

        # 关闭数据库连接
        db.close()

    # #把数据存入mysql
if __name__ == '__main__':
    demo = douban()
    for i in range(2):
        url ='https://book.douban.com/tag/%E5%8E%86%E5%8F%B2?start={}&type=T'.format(i*20)
        print("-------------------现在是第{}页-------------------".format(i+1))
        list = demo.get_one_page(url)
        for i in list:
            print(i)
            demo.write_to_mysql(i)



