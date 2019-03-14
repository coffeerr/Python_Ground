# Python_Ground

### :star: 001||爬取豆瓣历史类书籍

#### :point_right:1、需求

​	对豆瓣读书[历史](https://book.douban.com/tag/%E5%8E%86%E5%8F%B2)进行爬取,将读取到的数据存入数据库

#### :point_right:2、环境

​	Python 3.6x

​	mysql 5.5.6

#### :point_right:3、实现

![](https://github.com/coffeerr/Python_Ground/blob/master/%23001/%23001_1.JPG)

---

### ⭐️ 002||爬取豆瓣所有类别书籍（100页）

#### :point_right:1、需求

​	对豆瓣书籍[所有分类](https://book.douban.com/tag/?icn=index-nav)进行爬取，将读取到的数据存入数据库

​	改动：

​	 	1、相比于#001 数据库需要加上类别，以及排名

​		2、因为数据量比较大，可能需要防止反爬

​		3、代码细节改动

#### :point_right:2、环境

​	Python 3.6x

​	mysql 5.5.6

#### :point_right:3、实现

​	2019/03/03 爬了1000条，大概耗时1h，出现了两个问题

​			     》被反爬了

​			     》爬取时间过于缓慢，需要分布式爬取

#### :point_right:4、GTD

- [ ] 由于每个分类的情况不同，可爬取的最大页数不同，所以需要算法来根据分类爬取页数（无法爬取最大页数）
- [ ] 爬完所有的书籍
- [ ] 对所有的图书进行词云分析

---

### ⭐️ 003||爬取花瓣网分类图片（搁置）

#### :point_right:1、需求

V 0.1 爬取[花瓣旅行](http://huaban.com/favorite/travel_places/)分类下图片

#### :point_right:2、环境

​	Python 3.6x

​	mysql 5.5.6

#### :point_right:3、实现

​	1、解决ajax问题

​	2、解决cookie问题

#### :point_right:4、GTD

---

### ⭐️ 004||爬取新笔趣阁

####  :point_right:1、需求

​	爬取[新笔趣阁](http://www.xbiquge.la/xiaoshuodaquan/)所有小说，并下载

#### :point_right:2、环境

​	Python 3.6x

​	mysql 5.5.6

#### :point_right:3、实现

#### :point_right:4、GTD

---

### ⭐️005||简单代理词

#### 👉1、需求

​	根据西刺网代理搭建自己的代理池

#### 👉2、环境

​	Python 3.6x

​	mysql 5.5.6

#### 👉3、实现

#### 👉4、GTD

### 