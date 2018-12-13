import requests
from bs4 import BeautifulSoup

# 用beautiful解析html信息
def  get_http_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        demo = r.text
        soup = BeautifulSoup(demo,'html.parser')
        # print(soup.prettify()) # 修饰
        print(type(soup.p.contents[0].contents[0]))
        # for i in ls:
        #     if i == '\n':
        #         print(True)
        #         ls.remove(i)
        print(ls)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    get_http_text('http://python123.io/ws/demo.html')