#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 下午11:37
# @Author  : zhuo_hf@foxmail.com
# @File    : spider_main.py

import url_manager, html_downloader, html_outputer, html_parser


class SpiderMain(object):
    def __init__(self):
        # url管理器
        self.urls = url_manager.UrlManager()
        # html下载器
        self.downloader = html_downloader.HtmlDownloader()
        # html解析器
        self.parser = html_parser.HtmlParser()
        # html输出器
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        # 添加一个 主 url
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw {} : {}'.format(count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                # 注意这里是添加多个urls
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                if count == 1000:
                    break
                count = count + 1
            except:
                print('craw failed!!!!')
        self.outputer.output_html()

if __name__ == '__main__':
    root_url = "http://baike.baidu.com/item/python"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)