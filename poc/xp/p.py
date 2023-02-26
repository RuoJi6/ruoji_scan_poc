#!/usr/bin/env python
# coding=utf-8
#小皮面板1day存在未授权访问漏洞
import requests, threading
from termcolor import colored
requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    try:
        response = requests.get(url, headers=headers, verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if 'PHPStudy' in response.text:
            print(colored('[+]小皮面板1day存在未授权访问漏洞', 'red'))
            results = f'{urls}-->小皮面板1day存在未授权访问漏洞'
        else:
            print('[-]不存在小皮面板未授权访问漏洞')
    except:
        print('[-]不存在小皮面板未授权访问漏洞')


def xiaopi(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(urls,))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
