import requests
from bs4 import BeautifulSoup


# 获取页面信息
def get_http_text(url):
    # 设置浏览器的头部标识
    kv = {'User-Agent': 'Chrome/20'}
    r = requests.get(url, headers=kv)
    # 编码转换
    r.encoding = r.apparent_encoding
    return r.text


# 存储信息
def fill(ls, html):
    soup = BeautifulSoup(html, 'html.parser')
    # 得到所有的 class属性值为alt的tr标签
    tr_list = soup.find_all('tr', 'alt')
    # print(tr_list) 没有'\n'
    # soup.find_all('tbody').children
    # 遍历时有'\n' 可以用 isinstance(tr,bs4.elemnt.Tag) 来判断 需要引入 import bst
    # type(td.string) == 'bs4.element.Tag'
    for tr in tr_list:  # 遍历tr，得到tr的td
        tds = tr('td')
        ls.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string])


def print_list(ls, num=10):
    # 中英文混合输出时，长度不够会用西文空格填充，不对齐，所以可以指定用中文空格补齐，就是char(1288)
    tplt = "{0:^5}\t{1:{4}^10}\t{2:{4}^3}\t{3:^6}"
    print(tplt.format("排名", "学校名称", "省市", "总分", chr(12288)))
    for row in range(num):
        print(tplt.format(ls[row][0], ls[row][1], ls[row][2], ls[row][3], chr(12288)))


if __name__ == '__main__':
    ls = []
    html = get_http_text('http://zuihaodaxue.cn/zuihaodaxuepaiming2018.html')
    fill(ls, html)
    print_list(ls)
