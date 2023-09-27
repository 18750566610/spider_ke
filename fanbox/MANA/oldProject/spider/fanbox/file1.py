import fanbox.file as Link
import requests
from bs4 import BeautifulSoup
import re
import wget
from subprocess import call
import os
import time

# 类.方法
link = Link.getLink()[0]
print("link", link)
linkpart = []
downloadLink = []

print(link)


def getWork():
    class1 = "post__attachment-link"
    count1 = 0
    for i in range(len(link)):
        # for i in range(1):
        url = link[i]
        response = requests.get(url, headers=Link.Headers, proxies={"http": None, "https": None})
        html = response.text
        bs = BeautifulSoup(html, "lxml")
        count1 += 1
        count = 0
        for j in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['post__attachment-link']):
            # print(i)
            # print(j)
            data = re.findall('(?<=href=").*?(?=\")', str(j))
            print(data)
            linkpart.append(data)
            downloadLink.append("https://kemono.party" + "".join(map(str, linkpart[count])))
            path = "./download"
            path1 = f"{count}.psd"
            # wget.download(downloadLink[count], path)
            # IDMDownload(path, downloadLink[count], path1)
            count += 1
            # time.sleep(3)
        print(f"作品链接", {Link.getLink()[1]}, "具体作品链接", {url}, i, "项数", count)
        # time.sleep(5)
    print(linkpart)
    print(downloadLink)
    return 0


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
    getWork()
