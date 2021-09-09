# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name:       autoFetcher
   Description:     
   Author:          MicLon
   date:            2021/9/9
-------------------------------------------------
"""
from util.webRequest import WebRequest

#
rules = [
    {
        "url": "http://www.kxdaili.com/dailiip.html",
        "list": "//table[@class='active']//tr[position()>1]",
        "ip": "./td[1]/text()",
        "port": "./td[2]/text()"
    },
    {
        "url": "http://ip.yqie.com/ipproxy.htm",
        "list": "//table[@id='GridViewOrder']//tr[position()>1]",
        "ip": "./td[1]/text()",
        "port": "./td[2]/text()"
    }
]


def auto_fetcher():
    for rule in rules:
        html_tree = WebRequest().get(rule.get('url')).tree
        item_list = html_tree.xpath(rule.get('list'))
        for item in item_list:
            ip = ''.join(item.xpath(rule.get('ip')))
            port = ''.join(item.xpath(rule.get('port')))
            yield '%s:%s' % (ip, port)
