#!/usr/bin/env python
# coding=utf-8

from time import sleep
from termcolor import colored
from argparse import ArgumentParser
from pocz import zc
from scan import payload
import threading
import sys
import os
import time


if __name__ == '__main__':
    start_time = time.time()  # 程序开始时间
    try:
        name = colored('ruoji_scan_poc_1.0.[40] by 弱鸡', 'green')
        arg = ArgumentParser(description=name)
        arg.add_argument("-u",
                         "--url",
                         help=f"{colored('-u http://example.com/ or --url http://example.com/', 'green')}")
        arg.add_argument("-t",
                         "--thread",
                         help=f"{colored('-t 延迟 or --thread 延迟', 'green')}")
        arg.add_argument("-s",
                         "--support",
                         help=f"{colored('-s 1 or --support 1 [查看支持漏洞]', 'green')}")
        arg.add_argument("-b",
                         "--Batch",
                         help=f"{colored('-b 文件名 or --Batch 文件名 [txt文件]', 'green')}")
        arg.add_argument("-o",
                         "--one",
                         help=f"{colored('-o 漏洞号 or --one 漏洞号 [单个漏洞检测]', 'green')}")
        args = arg.parse_args()
        url = args.url
        support = args.support
        Batch = args.Batch
        thread = args.thread
        one=args.one
        if support != None:
            zc()
            sys.exit()
        if url == None and Batch == None:  # 判断是否输出参数
            name = os.path.basename(__file__)
            os.system(f'python {name} -h')
            sys.exit()
        if thread != None:  # 判断延迟
            thread = int(thread)
        else:
            thread = 0

        threads = []
        # 判断是不是指定漏洞
        if one == None:
            one = 0

        # 判断是不是url
        if url != None:
            t = threading.Thread(target=payload, args=(url,one,))
            threads.append(t)
            sleep(int(thread))
            t.start()
            for t in threads:
                t.join()

        # 判断是不是批量检测
        elif Batch!= None :
            urls = []
            for rs in open(f'{Batch}'):#读取文件存储在列表里面
                rs = rs.rstrip('\n')
                urls.append(rs)
            for rs in urls:
                if rs != "":#去空
                    print(colored(f'\n正在检测--> {rs}', 'green'))
                    t = threading.Thread(target=payload, args=(rs, one,))
                    threads.append(t)
                    sleep(int(thread))
                    t.start()
                    for t in threads:
                        t.join()

    except KeyboardInterrupt as error:
        print(colored(f'\n------------------------------------------', 'red'), '{', colored("程序终止", "green"), '}',
              colored(f'------------------------------------------', 'red'))
        sys.exit()
    except Exception as e:
        print(colored(f'\n------------------------------------------', 'red'), '{', colored("参数输入错误", "green"), '}',
              colored(f'------------------------------------------', 'red'))
        sys.exit()

    end_time = time.time()  # 程序结束时间
    run_time = end_time - start_time  # 程序的运行时间，单位为秒
    print(f'一共用了：{round(run_time,0)}秒')
    if os.path.exists('urls_value.txt'):
        print('urls_value.txt报告生成成功')
        for line in open('urls_value.txt',encoding='utf-8'):
            rs = line.rstrip('\n')
            print(colored(f'{rs}', 'magenta'))
    else:
        print('urls_value.txt报告生成失败')


'''
扫描模式批量所有
批量指定漏洞
扫描一个url

先mian接受参数以及模式，给到scan.py调用指定的模式进行扫描（调用指定的poc进行漏洞扫描，然后把返回的结果给scan.py文件，scan.p吧所有结果保存在本地的目录下面）
输入参数----》mian.py ----》scan.py -----》poc
poc---[结果]--->scan.py----》保存为urls_value.txt
'''