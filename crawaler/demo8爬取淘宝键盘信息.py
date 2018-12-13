# encoding='utf-8'

import requests
import re


# 得到html
def get_http_text(url):
    try:
        r = requests.get(url, headers={'User-Agent': 'Chrome/70'},timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:
        return e


# 解析页面
def parse_page(ilt, html):
    # 获取商品的标题字符串数组
    title_ls = re.findall(r'"title":".*?"', html)
    # print(title_ls)
    # 获取商品的价格字符串数组
    price_ls = re.findall(r'"price":"[\d\.]*?"', html)
    # print(price_ls)

    try:
        for i in range(len(title_ls)):
            # ilt.append([title_ls[i].split('"')[-2],price_ls[i].split('"')[-2]])

            ilt.append([eval(title_ls[i].split(':')[1]), eval(price_ls[i].split(':')[1])])
    except Exception as e:
        print(e)


# 打印
def print_info_list(ilt):
    tplt = "{0:^4}\t{2:4}\t{1:^16}"
    print(tplt.format("序号", "名称", "价格", chr(12288)))
    count = 0
    for row in ilt:
        count += 1
        print(tplt.format(count, row[0], row[1], chr(12288)))


def main():
    start_path = 'http://s.taobao.com/search?'
    goods = '键盘'
    num = 10
    info_list = []
    for i in range(num):
        try:
            parse_page(info_list, get_http_text(start_path + 'q=' + goods + '&s=' + str(48 * i)))
        except Exception as e:
            print(e)
    print_info_list(info_list)


main()
