# -*- coding: utf-8 -*-
import scrapy
import re
import json


# from scrapydemo.items import ScrapydemoItem
class ExampleSpider(scrapy.Spider):
    name = 'example'
    # 爬取这个域名一下的链接
    # allowed_domains = ['baidu.com']
    # scrapy 所要爬取页面的初始页面
    start_urls = [
        'http://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18108836139835706587_1544624874464&params=%7B%22type%22%3A%220%22%7D&_=1544624874685']

    # 该方法负责解析返回的数据(response data)，提取数据(生成item)以及生成需要进一步处理的URL的Request对象。
    def parse(self, response):  # 处理响应，
        # try:
        yield {'re':re.search(r'{.*}',response.body.decode('utf-8'))}
        # jQuery18108836139835706587_1544624874464 = tuple()
        # yield {'tutle': eval(response.body.decode('utf-8')[:-1])[0]}
        # yield {'str':response.body.decode('utf-8')}
        # yield {'eval(response)':eval(response.body)}
        # except Exception as e:
        #     print(e)
        # yield {'image':response.css('.tn-image')}
        # 右侧内容包含的标签
        # yield {'wrapper':response.css('.tn-wrapper')}
        # 下一个爬取的链接，这个用parse_next处理
        # yield scrapy.Request(url, callback=self.parse_next)
        # ERROR: Spider
        # must return Request, BaseItem, dict or None
        # print(price_ls)
        # fname = response.url.split('/')[-2]
        # with open(fname, 'wb') as f:
        #     #print(response.request.headers)
        #     f.write(response.body)
        # self.log('Save file %s.' % name)
        # d
        html = response.body.decode('utf-8')
        # 获取商品的标题字符串数组
        # title_ls = re.findall(r'"title":".*?"', html)
        # 获取商品的价格字符串数组
        # price_ls = re.findall(r'"price":"[\d\.]*?"', html)
        # for i in range(len(title_ls)):
        #     # ilt.append([title_ls[i].split('"')[-2],price_ls[i].split('"')[-2]])
        #     d[eval(title_ls[i].split(':')[1])] = eval(price_ls[i].split(':')[1])
        # url = 'http://s.taobao.com/search?q='+'键盘'+'&s=' + str(48)
        # 返回item
        # yield d
        # image所包含的标签


def parse_next(self, response):
    d = {}
    html = response.body.decode('utf-8')
    # 获取商品的标题字符串数组
    title_ls = re.findall(r'"title":".*?"', html)
    # 获取商品的价格字符串数组
    price_ls = re.findall(r'"price":"[\d\.]*?"', html)
    for i in range(len(title_ls)):
        # ilt.append([title_ls[i].split('"')[-2],price_ls[i].split('"')[-2]])
        d[eval(title_ls[i].split(':')[1])] = eval(price_ls[i].split(':')[1])
    yield d
