import requests


def get_http_text(url, param):
    try:
        kv = {'User-Agent': 'Chrome/20'}
        r = requests.get(url, headers=kv, params=param)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r
    except Exception as e:
        return e


if __name__ == '__main__':
    url = 'http://www.ip138.com/ips138.asp'
    param = {'ip': '200.1.1.1'}
    print(get_http_text(url, param).text[1000:])
