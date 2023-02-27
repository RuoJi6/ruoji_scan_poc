# ruoji_scan_poc_1.0.[40]
![image](https://user-images.githubusercontent.com/79234113/221392574-080836b3-8925-4de7-8a4a-f2db70baa485.png)
![image](https://user-images.githubusercontent.com/79234113/221392589-b5b81cda-04c9-4c3a-9157-045eb3de7400.png)
![image](https://user-images.githubusercontent.com/79234113/220616400-ff15fb67-aba4-44e4-854f-853e981eaed6.png)
![image](https://user-images.githubusercontent.com/79234113/220616464-05f1c541-508f-4e03-a59e-e36129c09448.png)
![image](https://user-images.githubusercontent.com/79234113/220616640-9ad857be-49af-4de4-bc09-7099436bf98c.png)
![image](https://user-images.githubusercontent.com/79234113/220616789-343093a2-c9ff-4cf9-b570-b496e8f2e374.png)
![307257964BE294B8F7DFEFA65A896222](https://user-images.githubusercontent.com/79234113/221392610-def4338d-26b1-4bd7-b318-12aa096cc2ac.jpg)


## 用于红队漏洞检测，可以批量检测漏洞

单个资产漏洞检测批量检测
多个资产批量检测
用于快速进行漏洞打点，找到存在的漏洞

```
建议使用Windows Terminal启动命令行
在windows官方的微软商店下载

PS D:\ruoji_sacn_poc> python .\main.py            
usage: main.py [-h] [-u URL] [-t THREAD] [-s SUPPORT] [-b BATCH] [-o ONE]

ruoji_scan_poc_1.0.[40] by 弱鸡

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

python3 main.py -s 1 查看漏洞编号
python3 main.py -u http://example.com/#对单个url进行，进行指多个漏洞检测
python3 main.py -u http://example.com/ -o 1#对单个url进行，进行指定漏洞检测
python3 main.py -b u.txt #对多个url进行漏洞批量检测
python3 main.py -b u.txt -o 1  #对只指定漏洞批量检测
```
```
安装：
pip install -r requirement.txt
使用python3运行，兼容Linux与windows
```
目前支持
```
ruoji_scan_poc_1.0.[40] by 弱鸡 支持以下漏洞检测
[+]1、小皮面板未授权访问漏洞
[+]2、小皮面板xss，linuxRCE，多处任意文件上传
[+]3、狮子鱼CMSCMSwxapp.php任意文件上传
[+]4、狮子鱼CMSimage_upload.php任意文件上传
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
[+]24、极限OA任意文件读取漏洞
[+]25、蓝凌OAsysSearchMain.do远程命令执行漏洞
[+]26、蓝凌OA任意文件读取漏洞
[+]27、蓝凌OAtreexml远程命令执行漏洞
[+]28、致远OAA8status.jsp信息泄露漏洞
[+]29、致远OAA8htmlofficeservlet任意文件上传漏洞
[+]30、致远OAA6数据库敏感信息泄露
[+]31、致远OAA6DownExcelBeanServlet用户敏感信息泄露
[+]32、致远OAA6initDataAssess.jsp用户敏感信息泄露
[+]33、致远OAA6setextno.jspSQL注入漏洞
[+]34、致远OAA6config.jsp敏感信息泄漏漏洞
[+]35、致远OAA6test.jspSQL注入漏洞
[+]36、致远OAajax.do任意文件上传CNVD-2021-01627
[+]37、致远OASession泄漏漏洞
[+]38、致远OAwebmail.do任意文件下载CNVD-2020-62422
[+]39、致远OAwpsAssistServlet任意文件上传漏洞
[+]40、致远OA帆软组件ReportServer目录遍历漏洞
```

## 尽情期待
后续会支持漏洞利用，网站指纹识别

## 免责声明

本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。
在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。如果发现上述禁止行为，我们将保留追究您法律责任的权利。
如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
在安装并使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款。除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。
您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
程序仅提供对漏洞点的判断，并不存在恶意操作!若检测到程序发出危险流量请及时联系作者进行删除，程序内的所有Payload来源于网络.

## 有问题请提交issues
项目会一直维护
## 项目群聊
![20230224091605](https://user-images.githubusercontent.com/79234113/221068048-de1dca82-502d-4db7-8952-b84a32528cfd.png)
