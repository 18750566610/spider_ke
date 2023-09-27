import fanbox.MANA.sql.getLink as Link  # 数据结构：[[1，2，3],[],[]]

from subprocess import call
import os
import urllib3
import requests
from bs4 import BeautifulSoup
import re
import json

link3 = []
listTHD = []
listTWD = []






def MainTransFrom():
    link = Link.select()
    print(link)
    list1 = []
    list6 = []
    dict1 = {}
    dict3 = {}
    list3 = []
    list4 = []
    # urllib3.disable_warnings()
    # trycount = input("请输入重试次数")
    # 遍历所有作者
    for i in range(len(link)):
        for j in


if __name__ == "__main__":
    # Download()
    MainTransFrom()
