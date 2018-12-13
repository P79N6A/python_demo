import requests
import os


def get_http_text(url):
    try:
        kv = {'User-Agent': 'Chrome/20'}

        r = requests.get(url, headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.content
    except Exception as e:
        return e


if __name__ == '__main__':
    url = 'http://www.xiaomawang.net/UploadFiles/2018-07-03/15306009861407422.jpg'
    root = 'image'
    path = root + '/'+url.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            with open(path, 'wb') as f:
                f.write(get_http_text(url))
        else:
            print('文件已经存在')
    except Exception as e:
        print(e)
