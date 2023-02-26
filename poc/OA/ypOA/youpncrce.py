#!/usr/bin/env python
# coding=utf-8
#用友NC_RCE漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/servlet/~ic/bsh.servlet.BshServlet', verify=False,timeout=20)
        if response.status_code == 200 and 'BeanShell Test Servlet' in response.text:
            print(colored('[+]存在用友NC_RCE漏洞', 'red'))
            results = f'{urls}-->存在用友NC_RCE漏洞'
        else:
            print('[-]不存在用友NC_RCE漏洞')
    except:
        print('[-]不存在用友NC_RCE漏洞')


def YPONCrce(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

