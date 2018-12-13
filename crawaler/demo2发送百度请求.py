import requests


def get_http_text(url):
    try:
        ky = {'User-Agent': 'Chrome/20'}
        param = {'wd': 'Python'}
        r = requests.get(url, headers=ky)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except Exception as e:
        return e


if __name__ == '__main__':
    url = 'https://pagelet.mafengwo.cn/note/pagelet/recommendNoteApi?callback=jQuery18106586073494615863_1544609603320&params=%7B%22type%22%3A%220%22%7D&_=1544609603682'
    print(get_http_text(url).encode('utf-8'))
