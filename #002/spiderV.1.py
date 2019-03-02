import requests
import pymysql
import time
from lxml import etree
'''
步骤
1、获取所有分类的url
2、对读取到的url进行#001的爬取
3、存入数据库
*4、绕过防爬

'''
class allBooks:
    def __init__(self):
        self.url = 'https://book.douban.com/tag/'
        self.proxy = '125.123.137.247:9999'
        self.proxies = {
            'http': 'http://' + self.proxy,
            'https': 'https://' + self.proxy,
        }
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36',
        }
    def get_genre_url(self):
        result = requests.get(self.url,headers=self.headers).text
        Html = etree.HTML(result)
        genre = Html.xpath('//*[@id="content"]/div/div[1]/div[2]//div/table/tbody//a/text()')
        # for i in range(len(genre)):
        #     genre[i] = 'https://book.douban.com' + genre[i]
        return genre
    def add_real_url(self,ss):
        return 'https://book.douban.com/tag/'+ss
    def get_one_page(self,url,ss):
        '''
        爬取一页的书籍
        :param url:当前页的链接
        :return: item包含一本书的信息
        '''
        print(url)
        booklist = []
        text = requests.get(url, headers=self.headers).text
        time.sleep(0.5)
        html = etree.HTML(text)
        bookName = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/h2/a/text()')
        bookInfo = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/div[1]/text()')
        bookScore = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/div[2]/span[2]/text()')
        bookUrl = html.xpath('//*[@id="subject_list"]/ul/li//div[2]/h2/a/@href')
        bookCover = html.xpath('//*[@id="subject_list"]/ul/li//div[1]/a/img/@src')
        bname = []
        for i in range(len(bookName)):
            bookName[i] = bookName[i].strip()
            if (bookName[i] != ''):
                bname.append(bookName[i])
        for i in range(len(bname)):
            item = {}
            item['bookName'] = bname[i]
            item['bookGenre'] = ss
            item['bookInfo'] = bookInfo[i].strip()
            item['bookScore'] = bookScore[i]
            item['bookUrl'] = bookUrl[i]
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
        bookUrl = item['bookUrl']
        bookGenre = item['bookGenre']
        sql = """INSERT INTO doubanbook 
                 VALUES (null, '%s','%s','%s','%s','%s','%s')"""
        try:
            # 执行sql语句
            cursor.execute(sql % (str(bookName),str(bookGenre),str(bookScore),str(bookInfo),str(bookUrl),str(bookCover)))
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
    # start = time.time()
    # print('----------开始爬取----------')
    a = allBooks()
    genre = a.get_genre_url()
    for i in genre:
        print(i)
        ss = a.add_real_url(i)
        for page in range(1):
            url = ss + '?start={}&type=T'.format(page*20)
            list = a.get_one_page(url,i)
            for book in list:
                print(book)
                a.write_to_mysql(book)
    # end = time.time()
    # print('----------爬取结束----------')
    # print('爬取时间：'+str(end-start))