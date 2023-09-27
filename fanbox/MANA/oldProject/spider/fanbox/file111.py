import fanbox.file as Link
import requests
from bs4 import BeautifulSoup
import re
import wget
from subprocess import call
import os
import time

# 定义变量区域
downloadLink = []
linkPart = []
linkpart = []
LLink = []
downloadLink = []

# 类.方法,获取作品链接
link = Link.getLink()[1]
workLink = Link.getLink()[0]


print("link", link)
print("workLink", workLink)


def getWorkLink():
    class1 = "post__attachment-link"
    for i in range(len(link)):
    # for i in range(2):
        print("第", i, "页")
        # for i in range(1):
        url = link[i]  # 拿到页工作链接，带有页数
        response = requests.get(url, headers=Link.Headers)
        html = response.text
        bs = BeautifulSoup(html, "lxml")  # 建造bs对象，准备分析一页中的所有作品（有多页）
        # count = 0
        for k in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['fancy-link']):
            # print(k)
            data = re.findall('(?<=href=").*?(?=\")', str(k))
            # print("data", data)
            linkPart.append(data)
        for j in range(len(linkPart) - 1):
            LLink.append("https://kemono.party" + "".join(map(str, linkPart[j])))
        # print(LLink)
    return LLink
    # for l1 in range(len(data)-1):
    #     # print("l1", str(l1))
    #     linkPart.append(data[l1])
    # print(linkPart)
    #     for j in range(len(linkPart)):
    #         LLink.append("https://kemono.party" + "".join(map(str, linkPart[j])))
    #     print(LLink)
    # for h in range(len(LLink)-1):
    #     print(LLink[h])

    #     print(j)
    #     data = re.findall('(?<=href=").*?(?=\")', str(j))
    #     print(data)
    #     linkpart.append(data)
    #     downloadLink.append("https://kemono.party" + "".join(map(str, linkpart[count])))
    #     path = "./download"
    #     path1 = f"{count}.psd"
    #     # wget.download(downloadLink[count], path)
    #     # IDMDownload(path, downloadLink[count], path1)
    #     count += 1
    #     print(f"作品链接", {Link.getLink()[1]}, "具体作品链接", {url}, i, "项数", count)
    #     # time.sleep(5)
    # print(linkpart)
    # print(downloadLink)
    # print(bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['fancy-link']))

    # print(html)
    # f = open(f"./download/{count}.html", "w", encoding="utf-8")
    # f.write(html)
    # count += 1
    # return 0


def download():
    link1 = getWorkLink()
    # print(len(link1))
    link1 = set(link1)
    print(link1)

    print(len(link1))

    link = []
    for i in link1:
        print(i)
        if i == 'https://kemono.party" rel=':
            continue
        else:
            link.append(i)
    print("link", link)
    for i in range(len(link)):
        url = link[i]
        response = requests.get(url, headers=Link.Headers, proxies={"http": None, "https": None})
        html = response.text
        bs = BeautifulSoup(html, "lxml")
        count = 0
        for j in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['post__attachment-link']):
            # print(i)
            # print(j)
            data = re.findall('(?<=href=").*?(?=\")', str(j))
            # print(url, data)
    #     #     print(data)
            linkpart.append(data)
            downloadLink.append("https://kemono.party" + "".join(map(str, linkpart[count])))
            print(downloadLink)
            count += 1
    #         # time.sleep(1)
    #     # time.sleep(3)
    print("downloadLink", downloadLink)

    for l1 in range(len(set(downloadLink))):
        path = "./download"
        path1 = f"{count}.psd"
        IDMDownload(path, downloadLink[l1], path1)








    # for l1 in range(len(downloadLink)):
    #     path = "./download"
    #     path1 = f"{count}.psd"
    #     IDMDownload(path, downloadLink[l1], path1)





        #     # wget.download(downloadLink[count], path)
        #     # IDMDownload(path, downloadLink[count], path1)
        #     count += 1
        #     # time.sleep(3)
        # print(f"作品链接", {Link.getLink()[1]}, "具体作品链接", {url}, i, "项数", count)
        # time.sleep(5)
    # for i in range(len(link)):
    #     path = "./download"
    #     path1 = f"{i}.psd"
    #     IDMDownload(path, link[i], path1)
    # cnt = 0
    # for ee in link:
    #     print(str(re.findall('https://.*?rel\=', ee)))
    #     a = re.findall('https://.*?rel\=', ee)
    #     # print(ee)
    #     if str(ee) == a:
    #         # cnt += 1  # 统计元素e出现的次数
    #
    #         print("a")
    #     cnt += 1
    # print(cnt)
    # print(link)
    # count = 0
    # for i in link:
    #     print(i)
    #     # if i == 'https://kemono.party" rel=':
    #     #     link.remove(count)
    #     # count += 1
    #         # print(link[i])
    #     # if link[i] == 'https://kemono.party" rel=':
    #     #     print(len(link))
    #     #     del link[1]


# /d URL  #根据URL下载文件
# /f      #定义文件存储在本地的文件名
# /p      #定义文件要存储在本地的地址
def IDMDownload(filepath, url, filename):
    IDMPath = "C:\Program Files (x86)\Internet Download Manager"
    IDM = "IDMan.exe"
    os.chdir(IDMPath)
    call([IDM, '/d', url, '/p', filepath, '/f', filename, '/a'])
    call([IDM, '/s'])
    return 0


if __name__ == "__main__":
    # getWorkLink()
    download()
