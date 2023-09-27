import fanbox.MANA.sql.DOWNLOAD as artists_Link
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


def getTime():
    # Link = artists_Link.Get_Works_Link()
    # print("链接", Link)
    # print("链接总长度", len(Link))
    newInsert = []
    manynewInsert = []
    allnewInsert = []
    with open("./log.json", "r", encoding="utf-8") as link:
        LinkA = json.load(link)
        link666 = Link.select()
        len1 = len(link666)
        print(len1)
        for i in range(len(LinkA)):
            print("共有%d位画师" % len(LinkA))
            print("第%d位画师有%d页\n" % (i+1, len(LinkA[i])))
            # print(LinkA[i])

            for j in range(len(LinkA[i]) - 1):
                # print(LinkA[i][j])
                for k in range(len(LinkA[i][j])):
                    # print(LinkA[i][j][k])
                    response1 = artists_Link.SendRequests(100000, LinkA[i][j][k], artists_Link.Headers)
                    html = response1
                    bs = BeautifulSoup(html, "html.parser")
                    # 获取时间戳
                    for link111, yemianCount in zip(link666, bs.select('time.timestamp')):
                        print(LinkA[i][j][k])
                        try:
                            content = bs.find("a", class_="post__user-name").contents[0]
                            time = yemianCount.get('datetime')
                            # time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                            content = str(content).replace(" ", "").replace("\n", "").strip().lstrip()
                            # print(content, LinkA[i][j][k], time)
                            # print(content)
                            # print(artists_Link.status)
                            status = artists_Link.SQLSave(content, LinkA[i][j][k], time)
                            print(status)
                            if status == "true":
                                newInsert.append(LinkA[i][j][k])
                            print("newinsert", newInsert)
                            break
                        except Exception as e:
                            print("发生错误，错误为：%s" % e)

                        # manynewInsert.append(newInsert)
                        # # print(allWorkLink, len(allWorkLink))
                        # f1 = open("./logtime.json", 'w')
                        # json.dump(manynewInsert, f1, indent=5)

                        break

                        # print(link666)
                        # for j111 in range(len1):
                        #     # print(link666[j111])
                    #     try:
                    #         content = bs.find("a", class_="post__user-name").contents[0]
                    #         time = yemianCount.get('datetime')
                    #         # time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                    #         content = str(content).replace(" ", "").replace("\n", "").strip().lstrip()
                    #         # print(content, LinkA[i][j][k], time)
                    #         # print(content)
                    #         # print(artists_Link.status)
                    #         status = artists_Link.SQLSave(content, LinkA[i][j][k], time)
                    #         print(status)
                    #         if status == "true":
                    #             newInsert.append(LinkA[i][j][k])
                    #         print("newinsert", newInsert)
                    #         break
                    #     except Exception as e:
                    #         print("发生错误，错误为：%s" % e)
                    #         continue
                    # manynewInsert.append(newInsert)
                    # # print(allWorkLink, len(allWorkLink))
                    # f1 = open("./logtime.json", 'w')
                    # json.dump(manynewInsert, f1, indent=5)

                    # print("manynewinsert", manynewInsert)
    return allnewInsert
                    # break
                    # try:
                    #     time = yemianCount.get('datetime')
                    #     time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                    #     print(link111[0], link111[1], link111[2], LinkA[i][j][k], time1)
                    #     artists_Link.SQLSave(link111[0], link111[1], link111[2], LinkA[i][j][k], time1)
                    #     break
                    # except:
                    #     continue

                    # print(link111[0], yemianCount)
                    # time = yemianCount.get('datetime')
                    # time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                    # # print(time1)
                    # artists_Link.SQLSave(link111[0], link111[1], link111[2], LinkA[i][j][k], time1)
                    # # print(link111[0], link111[1], link111[2], LinkA[i][j][k], time1)
                    # break
                    #     try:
                    #         time = yemianCount.get('datetime')
                    #         time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                    #         print(time1)
                    #         artists_Link.SQLSave(LinkA[i][j][k], time1)
                    #         break
                    #     except:
                    #         continue

                    # try:
                    #     time1 = datetime.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
                    #     # time1 = time
                    #     # new_list.append(time1)
                    #     print(time1)
                    #     artists_Link.SQLSave(newnewlink[0], newnewlink[1], newnewlink[2], LinkA[i][j], time1)
                    #     break
                    # except:
                    #     continue
                    # break


if __name__ == "__main__":
    getTime()
