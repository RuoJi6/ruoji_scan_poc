# ruoji_scan_poc
![image](https://user-images.githubusercontent.com/79234113/220616193-a9091d15-755d-4922-a634-0f801ccd3e46.png)
![image](https://user-images.githubusercontent.com/79234113/220616230-5ce7d5a5-047d-473e-82c3-5b1aca8fe474.png)
![image](https://user-images.githubusercontent.com/79234113/220616400-ff15fb67-aba4-44e4-854f-853e981eaed6.png)
![image](https://user-images.githubusercontent.com/79234113/220616464-05f1c541-508f-4e03-a59e-e36129c09448.png)
![image](https://user-images.githubusercontent.com/79234113/220616640-9ad857be-49af-4de4-bc09-7099436bf98c.png)
![image](https://user-images.githubusercontent.com/79234113/220616789-343093a2-c9ff-4cf9-b570-b496e8f2e374.png)

用于红队漏洞检测，可以批量检测漏洞
单个资产漏洞检测批量检测
多个资产批量检测
用于快速进行漏洞打点，找到存在的漏洞

```
PS D:\ruoji_sacn_poc> python .\main.py            
usage: main.py [-h] [-u URL] [-t THREAD] [-s SUPPORT] [-b BATCH] [-o ONE]

ruoji_scan_poc_1.0 by 弱鸡

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     -u http://example.com/ or --url http://example.com/
  -t THREAD, --thread THREAD
                        -t 延迟 or --thread 延迟
  -s SUPPORT, --support SUPPORT
                        -s 1 or --support 1 [查看支持漏洞]
  -b BATCH, --Batch BATCH
                        -b 文件名 or --Batch 文件名 [txt文件]
  -o ONE, --one ONE     -o 漏洞号 or --one 漏洞号 [单个漏洞检测]

```
目前支持
```
ruoji_scan_poc_1.0 by 弱鸡支持以下漏洞检测
[+]1、小皮面板未授权访问漏洞
[+]2、小皮面板xss，linuxRCE，多处任意文件上传
[+]3、狮子鱼CMS任意文件上传
[+]4、poc2狮子鱼CMS任意文件上传
[+]5、狮子鱼CMSsql注入
[+]6、poc2狮子鱼CMSsql注入
[+]7、WeiPHP3.0文件上传
[+]8、华天动力OA 8000版sql注入
[+]9、万户OA任意文件上传
[+]10、用友U8OAsql注入
[+]11、用友NC任意文件读取漏洞
[+]12、用友NC_RCE漏洞
[+]13、用友_NCCloud_FS文件管理SQL注入
[+]14、用友GRP-U8QL注入
[+]15、用友ERP-NCNCFindWeb目录遍历漏洞
[+]16、一米OA任意文件读取
[+]17、智明SmartOA任意文件下载漏洞
[+]18、致翔OASQL注入漏洞
[+]19、金和OAC6任意文件读取漏洞
[+]20、红帆OA任意文件读取漏洞
[+]21、源天OASQL注入漏洞
[+]22、金蝶OAApusic应用服务器(中间件)server_file目录遍历漏洞
[+]23、金蝶OAserver_file目录遍历漏洞
```

## 尽情期待
## 免责声明
本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。
在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。如果发现上述禁止行为，我们将保留追究您法律责任的权利。
如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
在安装并使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款。除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。
您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
程序仅提供对漏洞点的判断，并不存在恶意操作!若检测到程序发出危险流量请及时联系作者进行删除，程序内的所有Payload来源于网络.