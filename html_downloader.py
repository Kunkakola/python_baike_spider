#网页下载器
from urllib import request


class UrlDownloader():
    def download(self, url):
        if url is None:
            return None
        resp = request.urlopen(url)
        #请求失败
        if resp.getcode() != 200:
            return None
        #页面请求的状态值，分别有：200请求成功、303重定向、400请求错误、401未授权、403禁止访问、404文件未找到、500服务器错误
        return resp.read()