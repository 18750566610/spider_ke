import fanbox.MANA.sql.getLink as Link  # 数据结构：[[1，2，3],[],[]]
import fanbox.MANA.sql.download as download
from subprocess import call
import os
import urllib3
import requests
from bs4 import BeautifulSoup
import re
import math


def get_Timestamp():
    # /***********************************************************************************************/
    # /************************************    Send Requests    **************************************/
    # /************************************       Action        **************************************/
    # /***********************************************************************************************/
    timeList_Manypart = []
    timeList_ALLpart = []
    link = Link.select()
    print(link)
    urllib3.disable_warnings()
    trycount = input("请输入重试次数")
    for i in range(len(link)):
        list1 = []
        dict1 = {}
        for j in range(0, 1000, 50):
            url = f"https://kemono.party/{link[i][2]}/user/{link[i][0]}?o={j}"
            # print(url)
            list1.append(url)
            for lk in range(int(trycount)):
                try:
                    proxies = None
                    response = requests.get(url, headers=download.Headers, verify=False, proxies=None, timeout=3)
                    if response.status_code == 200:
                        print('Code:{}'.format(response.status_code))
                        break
                except:
                    # logdebug('requests failed one time')
                    try:
                        proxies = None
                        response = requests.get(url, headers=download.Headers, verify=False, proxies=None, timeout=3)
                        if response.status_code == 200:
                            print('Code:{}'.format(response.status_code))
                            break
                    except:
                        # logdebug('requests failed two time')
                        print('requests failed two time')
            # /***********************************************************************************************/
            # /************************************    Send Requests    **************************************/
            # /************************************         END         **************************************/
            # /***********************************************************************************************/
            # 将获取到的响应转化为文本
            html = response.text

            # 创建bs对象
            bs = BeautifulSoup(html, "html.parser")

            # /***********************************************************************************************/
            # /************************************    Get Timestamp    **************************************/
            # /************************************       Action        **************************************/
            # /***********************************************************************************************/
            # 获取时间戳
            timeList_part = []
            timeList_part1 = []
            a = []

            yemian = bs.find_all(lambda tag: tag.name == 'time' and tag.get('class') == ['timestamp'])
            judgment = False
            count1 = 0
            for yemianCount in bs.select('time.timestamp'):
                yemian111 = yemianCount.get('datetime')
                timeList_part.append(yemian111)
            count1 += 1
            timeList_part.pop()
            # print("timelist", timeList_part)
            timeList_Manypart.extend(timeList_part)
            print(timeList_Manypart)
            count = len(list1) / 50
            count = math.ceil(count)
            print(count)
            if count1 == count:
                timeList_ALLpart.extend(list(timeList_Manypart))
                timeList_ALLpart.pop()
                timeList_Manypart = []
                break

            print(timeList_ALLpart)

            # /***********************************************************************************************/
            # /*************************************   Get Timestamp    **************************************/
            # /*************************************        END         **************************************/
            # /***********************************************************************************************/
    return timeList_Allpart


if __name__ == "__main__":
    get_Timestamp()
