#!/usr/bin/env python
# coding=utf-8
import time
from poc.xp.p import xiaopi
from poc.xp.p2 import xiaopi2
from poc.cms.szy.szy import szy1
from poc.cms.szy.szy2 import szy2
from poc.cms.szy.szysql import szysql
from poc.cms.szy.szysql2 import szysql2
from poc.cms.WeiPHP3 import WeiPHP3
from poc.OA.huatianOA import htOA
from poc.OA.wanghuOA.wanhuOAuploadfileUpload_controller import WHOA
from poc.OA.ypOA.youpong0Asql import YPOA
from poc.OA.ypOA.youpncdir import YPONCdir
from poc.OA.ypOA.youpncrce import YPONCrce
from poc.OA.ypOA.youpNCCloudFSfile import YPNCDILE
from poc.OA.ypOA.youpGRP_U8sql import YPGRPSQL
from poc.OA.ypOA.youpERP_NCNCFindWebdir import YPNCFILEDIR
from poc.OA.yimiOAdirdow import yimiOA
from poc.OA.zhiming import zhimingOA
from poc.OA.zhixianf0Asql import zhixiangOA
from poc.OA.jinghedirfile import jingheOAdile
from poc.OA.hongfangOA import hongfOAdile
from poc.OA.yuantainOA import yuantianOA
from poc.OA.jdOA.jdOAApusicApusic import jingdieOAApusic
from poc.OA.jdOA.jdOAserver_file import jingdieOAserver_file
from poc.OA.jixiangOAdile import jixiangOA
from poc.OA.langlingOA.langlingOARCE import langlingOARCE
from poc.OA.langlingOA.langlingAOfile import langlingAOfile
from poc.OA.langlingOA.langlingOARCEtreexml import langlingOARCEtreexml
from poc.OA.zhiyuan.zhiyuanOAstausfile import zyOAA8status
from poc.OA.zhiyuan.zhiyuanOAuploadfilehtmlofficeservlet import zhiyuanOAupload
from poc.OA.zhiyuan.zhiyuanOAA6SQLxiel import zhiyuanOAA6SQLxielou
from poc.OA.zhiyuan.zhiyuanOAA6YHXL import zhiyuanOA6YH
from poc.OA.zhiyuan.zhiyuanOAinitDataAssess import zhiyuanOAinitDataAssess
from poc.OA.zhiyuan.zhiyuanOAsetextnosql import zhiyuanOAsetextnosql
from poc.OA.zhiyuan.zhiyuanOA6config import zhiyuanOAconfig
from poc.OA.zhiyuan.zhiyuanOA6SQLtest import zhiyuanOAtestsql
from poc.OA.zhiyuan.zhiyuanOAuoload import zhiyuanOAuploadOAajax
from poc.OA.zhiyuan.zhiyuansessionOA import zhiyuanOAsession
from poc.OA.zhiyuan.zhiyuanOAwebmailfileupload import zhiyuanOAuoloadfile
from poc.OA.zhiyuan.zhiyuanOAwpsAessistServlet import zhiyuanOAwjuofile
from poc.OA.zhiyuan.zhiyuanOAReortServer import zhiyuanOAFANGml

a = 0


def payload(url, one):
    if 'http://' in url or 'http://' in url:  # 判断接收过来的域名有没有http或者https
        pass
    else:
        url = 'http://' + url

    global a
    url_txt = []
    if one == '1':
        url_txt.append(xiaopi(url))  # 小皮面板1day存在未授权访问漏洞
    elif one == '2':
        url_txt.append(xiaopi2(url))  # 小皮面版1day可能存在xss，linuxRCE，多处任意文件上传
    elif one == '3':
        url_txt.append(szy1(url))  # 狮子鱼CMSCMSwxapp.php任意文件上传
    elif one == '4':
        url_txt.append(szy2(url))  # 2poc狮子鱼CMSimage_upload.php任意文件上传
    elif one == '5':
        url_txt.append(szysql(url))  # 狮子鱼CMSsql注入
    elif one == '6':
        url_txt.append(szysql2(url))  # 2poc狮子鱼CMSsql注入
    elif one == '7':
        url_txt.append(WeiPHP3(url))  # WeiPHP3.0任意文件上传
    elif one == '8':
        url_txt.append(htOA(url))  # 华天动力OA8000版sql注入
    elif one == '9':
        url_txt.append(WHOA(url))  # 万户OA任意文件上传
    elif one == '10':
        url_txt.append(YPOA(url))  # 用友U8OAsql注入
    elif one == '11':
        url_txt.append(YPONCdir(url))  # 用友NC任意文件读取漏洞
    elif one == '12':
        url_txt.append(YPONCrce(url))  # 用友NC_RCE漏洞
    elif one == '13':
        url_txt.append(YPNCDILE(url))  # 用友_NCCloud_FS文件管理SQL注入
    elif one == '14':
        url_txt.append(YPGRPSQL(url))  # 用友GRP-U8sql注入
    elif one == '15':
        url_txt.append(YPNCFILEDIR(url))  # 用友ERP-NCNCFindWeb目录遍历漏洞
    elif one == '16':
        url_txt.append(yimiOA(url))  # 一米OA任意文件读取漏洞
    elif one == '17':
        url_txt.append(zhimingOA(url))  # 智明SmartOA任意文件下载漏洞
    elif one == '18':
        url_txt.append(zhixiangOA(url))  # 致翔OASQL注入漏洞
    elif one == '19':
        url_txt.append(jingheOAdile(url))  # 金和OAC6任意文件读取漏洞
    elif one == '20':
        url_txt.append(hongfOAdile(url))  # 红帆OA任意文件读取漏洞
    elif one == '21':
        url_txt.append(yuantianOA(url))  # 源天OASQL注入漏洞
    elif one == '22':
        url_txt.append(jingdieOAApusic(url))  # 金蝶OAApusic应用服务器(中间件)server_file目录遍历漏洞
    elif one == '23':
        url_txt.append(jingdieOAserver_file(url))  # 金蝶OAserver_file目录遍历漏洞
    elif one == '24':
        url_txt.append(jixiangOA(url))  # 极限OA任意文件读取漏洞
    elif one == '25':
        url_txt.append(langlingOARCE(url))  # 蓝凌OAsysSearchMain.do远程命令执行漏洞
    elif one == '26':
        url_txt.append(langlingAOfile(url))  # 蓝凌OA任意文件读取漏洞
    elif one == '27':
        url_txt.append(langlingOARCEtreexml(url))  # 蓝凌OAtreexml远程命令执行漏洞
    elif one == '28':
        url_txt.append(zyOAA8status(url))  # 致远OAA8status.jsp信息泄露漏洞
    elif one == '29':
        url_txt.append(zhiyuanOAupload(url))  # 致远OAA8htmlofficeservlet任意文件上传漏洞
    elif one == '30':
        url_txt.append(zhiyuanOAA6SQLxielou(url))  # 致远OA A6 createMysql.jsp 数据库敏感信息泄露
    elif one == '31':
        url_txt.append(zhiyuanOA6YH(url))  # 致远OAA6DownExcelBeanServlet用户敏感信息泄露
    elif one == '32':
        url_txt.append(zhiyuanOAinitDataAssess(url))  # 致远OAA6initDataAssess.jsp用户敏感信息泄露
    elif one == '33':
        url_txt.append(zhiyuanOAsetextnosql(url))  # 致远OAA6setextno.jspSQL注入漏洞
    elif one == '34':
        url_txt.append(zhiyuanOAconfig(url))  # 致远OAA6config.jsp敏感信息泄漏漏洞
    elif one == '35':
        url_txt.append(zhiyuanOAtestsql(url))  # 致远OAA6test.jspSQL注入漏洞
    elif one == '36':
        url_txt.append(zhiyuanOAuploadOAajax(url))  # 致远OAajax.do任意文件上传CNVD-2021-01627
    elif one == '37':
        url_txt.append(zhiyuanOAsession(url))  # 致远OASession泄漏漏洞
    elif one == '38':
        url_txt.append(zhiyuanOAuoloadfile(url))  # 致远OAwebmail.do任意文件下载CNVD-2020-62422
    elif one == '39':
        url_txt.append(zhiyuanOAwjuofile(url))  # 致远OAwpsAssistServlet任意文件上传漏洞
    elif one == "40":
        url_txt.append(zhiyuanOAFANGml(url))  # 致远OA帆软组件ReportServer目录遍历漏洞
    else:
        url_txt.append(xiaopi(url))  # 小皮面板1day存在未授权访问漏洞
        url_txt.append(xiaopi2(url))  # 小皮面版1day可能存在xss，linuxRCE，多处任意文件上传
        url_txt.append(szy1(url))  # 狮子鱼CMSCMSwxapp.php任意文件上传
        url_txt.append(szy2(url))  # 2poc狮子鱼CMSimage_upload.php任意文件上传
        url_txt.append(szysql(url))  # 狮子鱼CMSsql注入
        url_txt.append(szysql2(url))  # 2poc狮子鱼CMSsql注入
        url_txt.append(WeiPHP3(url))  # WeiPHP3.0任意文件上传
        url_txt.append(htOA(url))  # 华天动力OA8000版sql注入
        url_txt.append(WHOA(url))  # 万户OA任意文件上传
        url_txt.append(YPOA(url))  # 用友U8OAsql注入
        url_txt.append(YPONCdir(url))  # 用友NC任意文件读取漏洞
        url_txt.append(YPONCrce(url))  # 用友NC_RCE漏洞
        url_txt.append(YPNCDILE(url))  # 用友_NCCloud_FS文件管理SQL注入
        url_txt.append(YPGRPSQL(url))  # 用友GRP-U8sql注入
        url_txt.append(YPNCFILEDIR(url))  # 用友ERP-NCNCFindWeb目录遍历漏洞
        url_txt.append(yimiOA(url))  # 一米OA任意文件读取漏洞
        url_txt.append(zhimingOA(url))  # 智明SmartOA任意文件下载漏洞
        url_txt.append(zhixiangOA(url))  # 致翔OASQL注入漏洞
        url_txt.append(jingheOAdile(url))  # 金和OAC6任意文件读取漏洞
        url_txt.append(hongfOAdile(url))  # 红帆OA任意文件读取漏洞
        url_txt.append(yuantianOA(url))  # 源天OASQL注入漏洞
        url_txt.append(jingdieOAApusic(url))  # 金蝶OAApusic应用服务器(中间件)server_file目录遍历漏洞
        url_txt.append(jingdieOAserver_file(url))  # 金蝶OAserver_file目录遍历漏洞
        url_txt.append(jixiangOA(url))  # 极限OA任意文件读取漏洞
        url_txt.append(langlingOARCE(url))  # 蓝凌OAsysSearchMain.do远程命令执行漏洞
        url_txt.append(langlingAOfile(url))  # 蓝凌OA任意文件读取漏洞
        url_txt.append(langlingOARCEtreexml(url))  # 蓝凌OAtreexml远程命令执行漏洞
        url_txt.append(zyOAA8status(url))  # 致远OAA8status.jsp信息泄露漏洞
        url_txt.append(zhiyuanOAupload(url))  # 致远OAA8htmlofficeservlet任意文件上传漏洞
        url_txt.append(zhiyuanOAA6SQLxielou(url))  # 致远OA A6 createMysql.jsp 数据库敏感信息泄露
        url_txt.append(zhiyuanOA6YH(url))  # 致远OAA6DownExcelBeanServlet用户敏感信息泄露
        url_txt.append(zhiyuanOAinitDataAssess(url))  # 致远OAA6initDataAssess.jsp用户敏感信息泄露
        url_txt.append(zhiyuanOAsetextnosql(url))  # 致远OAA6setextno.jspSQL注入漏洞
        url_txt.append(zhiyuanOAconfig(url))  # 致远OAA6config.jsp敏感信息泄漏漏洞
        url_txt.append(zhiyuanOAtestsql(url))  # 致远OAA6test.jspSQL注入漏洞
        url_txt.append(zhiyuanOAuploadOAajax(url))  # 致远OAajax.do任意文件上传CNVD-2021-01627
        url_txt.append(zhiyuanOAsession(url)) #致远OASession泄漏漏洞
        url_txt.append(zhiyuanOAuoloadfile(url))#致远OAwebmail.do任意文件下载CNVD-2020-62422
        url_txt.append(zhiyuanOAwjuofile(url))#致远OAwpsAssistServlet任意文件上传漏洞
        url_txt.append(zhiyuanOAFANGml(url))#致远OA帆软组件ReportServer目录遍历漏洞
    if a == 0:
        for i in range(len(url_txt)):  # 如果没有就不生成报告
            if url_txt[i] != None and url_txt[i] != "":
                a = a + 1
                with open('urls_value.txt', 'a+', encoding='utf-8') as fa:
                    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                    fa.write(f'-------------------------生成时间:{current_time}------------------------------\n')
    for i in range(len(url_txt)):  # 报告成txt文件
        if url_txt[i] != None and url_txt[i] != "":
            with open('urls_value.txt', 'a+', encoding='utf-8') as fp:
                fp.write(str(url_txt[i]) + '\n')


'''
url_txt为得到报告文件，存储在报告里面
前面if是判断指定漏洞扫描
后的else是默认扫描
'''
