import requests


def get_http_text(url):
    try:
        ky = {'User-Agent': 'Chrome/20'}
        r = requests.get(url, headers=ky)
        r.raise_for_status()  # 如果不是200 跑出HttpError
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e:

        return e

if __name__ == '__main__':
    # 构造url链接
    link = 'https://item.jd.hk/1938381.html'
    print(get_http_text(link)[1000:2000])
