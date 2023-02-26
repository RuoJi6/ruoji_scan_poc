#!/usr/bin/env python
# coding=utf-8
#用友_NCCloud_FS文件管理SQL注入
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/fs/', verify=False,timeout=20)
        if 'glyphicon glyphicon-user' in response.text:
            print(colored('[+]存在用友_NCCloud_FS文件管理SQL注入，可能存在', 'red'))
            results =  f'{urls}-->存在用友_NCCloud_FS文件管理SQL注入，可能存在'
        else:
            print('[-]不存在用友_NCCloud_FS文件管理SQL注入')
    except:
        print('[-]不存在用友_NCCloud_FS文件管理SQL注入')


def YPNCDILE(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
