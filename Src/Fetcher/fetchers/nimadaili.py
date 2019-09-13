# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re

from Util.WebRequest import WebRequest
from Util.utilFunction import getHtmlTree


class CustomFetcher():
    fetcher_host = "www.nimadaili.com"

    def run(self):
        end = 10
        url = 'http://www.nimadaili.com/{col}/{page}/'
        col_list = ['gaoni', 'http', 'https']
        for col in col_list:
            for i in range(1, end):
                html_tree = getHtmlTree(url.format(page=i, col=col))
                data_list = html_tree.xpath('//tr//td[1]//text()')
                for data in data_list:
                    if ':' in data:
                        yield data.strip()
