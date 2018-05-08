#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/7 下午11:38
# @Author  : zhuo_hf@foxmail.com
# @File    : html_downloader.py

import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib2.urlopen(url)
        if response.getcode() != 200:
            return None

        return response.read()