#!/usr/bin/env python
# coding=utf-8
#小皮面版xss，linuxRCE，多处任意文件上传
import requests, threading
from termcolor import colored
requests.packages.urllib3.disable_warnings()  #忽略证书报错

results = ''
def pscan_vuln2(url):
    urls = url
    global results
    i = 0
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    for rs in range(2):
        if rs == 0:
            try:
                response = requests.get(url + 'service/app/databases.php', headers=headers, verify=False,timeout=20)
                if '1001' in response.text:
                    i = i +1
            except:
                pass
        elif rs == 1:
            try:
                response = requests.get(url + 'service/app/files.php', headers=headers, verify=False)
                if '1001' in response.text:
                    i = i + 1
                    if i == 2 or i == 1:
                        print(colored('[+]小皮面版1day可能存在xss，linuxRCE，多处任意文件上传', 'red'))
                        results = f'{urls}-->小皮面版1day可能存在xss，linuxRCE，多处任意文件上传'
                else:
                    print('[-]不存在小皮面版xss，linuxRCE，多处任意文件上传')
            except:
                print('[-]不存在小皮面版xss，linuxRCE，多处任意文件上传')
    return f'123'



def xiaopi2(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln2, args=(urls,))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results

