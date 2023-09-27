import fanbox.MANA.sql.getLink as Link  # 数据结构：[[1，2，3],[],[]]
from subprocess import call
import os
import urllib3
import requests
from bs4 import BeautifulSoup
import re
import json
import pymysql
import datetime
import traceback

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='kemono_id',
    charset='utf8')

# 获取游标
cursor = db.cursor()

urllib3.disable_warnings()
global response
Headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': '__ddg1_=gOGskCMPIGzpbP6my7yP; _pk_id.1.5bc1=7fc603afa5d8ed26.1664024743.; _pk_id.2.5bc1=b2c2551aa7f9d854.1666008560.; _pk_ses.1.5bc1=1',
    'sec-ch-ua': '"Microsoft Edge";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.26'
}


def SQLSave(name, link, time):
    status = "false"
    data = (name, link, time)
    sql1 = '''
            insert into workLink(name, link, time) value("%s","%s","%s")
            '''
    cursor.execute(sql1 % data)
    db.commit()
    status = "true"
    print("insert success")
    return status


def SQL_Select():
    sql1 = '''
        SELECT COUNT(a.`name`) FROM (SELECT name from worklink GROUP BY name) AS a
    '''
    cursor.execute(sql1)
    db.commit()
    result = cursor.fetchall()
    result = list(map(list, result))

    return result
def SQL_Delete():
    sql1 = '''
    TRUNCATE worklink
    '''
    cursor.execute(sql1)
    db.commit()


def SendRequests(trycount, url, Headers):
    # html = ""
    global html
    # response = requests.get(url, headers=Headers, verify=False, proxies=None, timeout=3)
    # html = response.text
    for lk in range(int(trycount)):
        try:
            proxies = None
            response = requests.get(url, headers=Headers, verify=False, proxies=None, timeout=3)
            if response.status_code == 200:
                print('Code:{}'.format(response.status_code))
                html = response.text
                break
        except:
            # logdebug('requests failed one time')
            try:
                proxies = None
                response = requests.get(url, headers=Headers, verify=False, proxies=None, timeout=3)
                if response.status_code == 200:
                    print('Code:{}'.format(response.status_code))
                    html = response.text
                    break
            except:
                # logdebug('requests failed two time')
                print('requests failed two time')
    # 将response对象转化为文本

    return html


def Transform():
    sql_Link = Link.select()
    twoL = []
    for i in range(len(sql_Link)):
        # print(i)
        Page_All_Link = []
        for j in range(0, 2300, 50):
            url = f"https://kemono.party/{sql_Link[i][2]}/user/{sql_Link[i][0]}?o={j}"
            # print(url)
            Page_All_Link.append(url)
        twoL.append(Page_All_Link)
        print(len(twoL))
    return twoL


global id
global artist
global company


def Get_Works_Link():
    link = Link.select()
    Artists_Link = Transform()
    timeList_Allpart = []
    allWorkLink = []

    for i in range(len(Artists_Link)):
        id = link[i][0]
        artist = link[i][1]
        company = link[i][2]
        manyWorkLink = []
        newLink = []
        for j in range(len(Artists_Link[i])):
            response1 = SendRequests(100000, Artists_Link[i][j], Headers)
            html = response1
            bs = BeautifulSoup(html, "html.parser")
            yemian = bs.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['card-list__items'])

            data_id = re.findall('(?<=data-id=").*?(?=")', str(yemian))
            link3 = []
            # 获取分析链接
            data_id_length = len(data_id)
            print(type(data_id_length))
            for k in range(data_id_length):
                # 一维列表，被后来的值覆盖
                link3.append(f"https://kemono.party/{company}/user/{id}/post/" + "".join(map(str, data_id[k])))
                if type(data_id_length) is None:
                    break
            newLink.append(link3)
            # print(len(newLink))
        allWorkLink.append(newLink)
        # print(allWorkLink, len(allWorkLink))
        f1 = open("./log.json", 'w')
        json.dump(allWorkLink, f1, indent=5)
            # if not newLink[-1]: # 相当于是：if newLink[-1] == []
            #     allWorkLink.append(newLink)
            #     f1 = open("./log.json", 'w')
            #     json.dump(allWorkLink, f1, indent=5)
            #     print("当前页页数：", len(newLink))
            #     print(newLink)
            #     print("Artists Count：", len(allWorkLink))
            #     print(allWorkLink)
            #     break
            # # print(allWorkLink)
    return allWorkLink

            # for k in range(len(data_id)):
            #     if company != "discord":
            #         link3.append(
            #             f"https://kemono.party/{company}/user/{id}/post/" + "".join(map(str, data_id[k])))
            #         newLink.append(
            #             f"https://kemono.party/{company}/user/{id}/post/" + "".join(map(str, data_id[k])))
            #         manyWorkLink.append(newLink)
            #
            #     # else:
            #     #     # newLink.append(f"https://kemono.party/{data_service}/user/{data_user}/post/" "".join(map(str, link3[i])))
            #     #     pass
            # # print(len(manyWorkLink))
            #     allWorkLink.append(manyWorkLink)
            #     break

            # print(allWorkLink)
            # with open("./log.json", 'w', encoding="utf-8") as aaa:
            # aaaa = json.load(aaa)



            # json.dump(manyWorkLink, f1, indent=5)

        #     # 获取时间戳
        #     timeList_part = []
        #     new_list = []
        #     for yemianCount in bs.select('time.timestamp'):
        #         time = yemianCount.get('datetime')
        #         try:
        #             # time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
        #             time1 = time
        #             new_list.append(time1)
        #         except:
        #             continue
        #     break
        #         # timeList_part.append(yemianCount.get('datetime'))
        #         # timeList_part.append(time1)
        #     # timeList_part.pop()
        #     # print(new_list)
        #
        #     # timeList_Allpart.append(new_list)
        #
        #     # print(allWorkLink)
        #     # print(len(allWorkLink))
        #     # print(len(timeList_Allpart))
        #     # print(timeList_Allpart)
        #     # for link, time in zip(allWorkLink, timeList_Allpart):
        #
        #         # for link1, timeUnpack in zip(range(len(allWorkLink[link])), range(len(timeList_Allpart[time]))):
        #         #     print(allWorkLink[link][link1])
        #             # for linkUnpack in range(len(allWorkLink[link])):
        #             #     print(allWorkLink[link][link1][linkUnpack])
        #             # print(timeList_Allpart[time][timeUnpack])
        #                 # SQLSave(id, artist, company, allWorkLink[link][linkUnpack],
        #                 #         timeList_Allpart[time][timeUnpack])  # id, name, company, link
        #
        #
        #     # timeList_Allpart.append(list(timeList_part))
        #     # for iii in allWorkLink:
        #     #     print(iii)
        #     # for jjj in timeList_Allpart:
        #     #     print(jjj)
        #
        #
        #     #
        #     #     break
        #
        #
        #
        #
        #
        #     # for time in range(len(timeList_Allpart)):
        #     # # for link, time in zip(newLink, timeList_Allpart):
        #     # #     print(timeList_Allpart[time])
        #     #     link111 = newLink[time]
        #     #     for time1 in range(len(timeList_Allpart[time])):
        #     #         print(link111)
        #     #         print(timeList_Allpart[time][time1])
        #     #         break
        #
        #         # link111 = newLink[link]
        #         # print(link111)
        #         # for timeUnpack in range(len(timeList_Allpart[time])):
        #         #     print(timeList_Allpart[time][timeUnpack])
        #         # #     SQLSave(id, artist, company, link111, timeList_Allpart[time][timeUnpack])  # id, name, company, link
        #     # break
        # # break


if __name__ == "__main__":
    Get_Works_Link()
    # Transform()
