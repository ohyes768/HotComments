# coding=utf-8
import requests
import os
import re
import json
import getComment


class NetMV:
    def __init__(self, url):
        self.url = url
        self.mv_id = []
        self.mv_urls = []
        self.comment_ids = []
        self.comment_urls = []

    def generate(self):
        try:
            id = self.url
            # id = re.findall(r'id=(.*)', self.url)[0]
        except Exception as e:
            print('歌单地址有错误')
        x = requests.get('https://api.imjad.cn/cloudmusic/?type=playlist&id=%s' % id)
        j = requests.get('https://api.imjad.cn/cloudmusic/?type=playlist&id=%s' % id).json()
        ll = len(j['privileges'])
        # 获取MV ID
        for i in range(0, ll):
            if j['playlist']["tracks"][i]['mv'] != 0:
                self.mv_id.append(j['playlist']["tracks"][i]['mv'])
        # 获取MV的URL
        for id in self.mv_id:
            self.mv_urls.append('https://api.imjad.cn/cloudmusic/?type=mv&id=%s' % id)

        for i in range(0, ll):
            self.comment_ids.append(j['playlist']["tracks"][i]['id'])

        for id in self.comment_ids:
            self.comment_urls.append('http://music.163.com/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=' % id)


    def download(self):
        pwd = os.path.abspath('.')
        directory = pwd + '/' + 'MV'
        if not os.path.exists(directory):
            os.makedirs(directory)
        for mv_url in self.mv_urls:
            name = requests.get(mv_url).json()['data']['name']
            if os.path.exists(directory + '/' + '%s.mkv' % name) == True:
                print('已经下载过这首歌曲了，跳过......')
            else:
                try:
                    url = requests.get(mv_url).json()['data']['brs']['1080']
                    r = requests.get(url)
                    print('开始下载%s到当前的文件夹' % name)
                    with open(directory + '/' + '%s.mkv' % name, 'wb') as f:
                        f.write(r.content)
                except Exception as e:
                    print('1080')

        print('下载结束，看看去吧')

    def hotComment(self):
        headers = {
            'Host': 'music.163.com',
            'Proxy-Connection': 'keep-alive',
            'Origin': 'http://music.163.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        text = {
            'rid': 'R_SO_4_30953009',
            'offset': '0',
            'total': 'true',
            'limit': '20',
            'csrf_token': '',
        }
        modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
        nonce = '0CoJUm6Qyw8W8jud'
        pubKey = '010001'
        text = json.dumps(text)  # 转化成字符串str
        secKey = getComment.createSecretKey(16)
        encText = getComment.aesEncrypt(getComment.aesEncrypt(text, nonce), secKey)
        encSecKey = getComment.rsaEncrypt(secKey, pubKey, modulus)
        data = {
            'params': encText,
            'encSecKey': encSecKey
        }
        for url in self.comment_urls:
            req = requests.post(url, headers=headers, data=data)
            print "---------####----------"
            for content in req.json()['hotComments']:
                if content!="":
                    print content['content'].encode('utf-8')
            print req.json()['total']



def main():
    print('输入歌单的ID')
    nv = NetMV(url=input())
    nv.generate()
    nv.hotComment()
    # nv.download()


if __name__ == '__main__':
    main()