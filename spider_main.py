import url_manager
import html_downloader
import html_parser
import html_outputer


class SpiderMain():
    def __init__(self):
        #url管理器
        self.urls = url_manager.UrlManager()
        #url下载器
        self.downloader = html_downloader.UrlDownloader()
        #url解析器
        self.parser = html_parser.UrlParser()
        #url输出器
        self.outputer = html_outputer.UrlOutputer()

    def craw(self, rooturl):
        #count记录当前爬取的是第几个url
        count = 1
        #添加单条rul
        self.urls.add_new_url(rooturl)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                #输出是第几条url
                print('craw 第%d条url: %s ' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                #添加多条url
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                #只爬取1000条
                if count == 30: break
                count += 1
            except:
                print('craw 第%d条url: %s 失败' % (count, new_url))
            
        #输出数据
        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313?fr=aladdin'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
