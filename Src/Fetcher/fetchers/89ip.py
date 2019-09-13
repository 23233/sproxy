# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re

from Util.WebRequest import WebRequest
from Util.utilFunction import getHtmlTree


class CustomFetcher():
    fetcher_host = "www.89ip.cn"

    def run(self):
        url = 'http://www.89ip.cn/tqdl.html?num=2500&address=&kill_address=&port=&kill_port=&isp='
        html_tree = getHtmlTree(url)
        data_warp = html_tree.xpath("//div[@class='fly-panel']/div[@style='padding-left:20px;']//text()")
        for data in data_warp:
            if ':' in data:
                yield data.strip()
