import requests
from bs4 import BeautifulSoup
import re
from random import randint
import time
import urllib3


# Headers = {
#     'cookie': 'BIDUPSID=580FD855A26DCE31E1BEBB360D3772C1; PSTM=1633847655; __yjs_duid=1_24793f6b65b6620080c9b77e3ad3584c1633863356918; MCITY=-%3A; BAIDUID=763063B271DF62A4E6A6AA7F285E8ADD:FG=1; BDUSS=hhaVZDZEV-TDNXbjRQfnVDclVDSVk0alRwWHFZR0VYZUZyZHlDdlNlRXFyT0JpRVFBQUFBJCQAAAAAAQAAAAEAAABTx7AqTWFrb9zU19NfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACofuWIqH7lid1; BDUSS_BFESS=hhaVZDZEV-TDNXbjRQfnVDclVDSVk0alRwWHFZR0VYZUZyZHlDdlNlRXFyT0JpRVFBQUFBJCQAAAAAAQAAAAEAAABTx7AqTWFrb9zU19NfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACofuWIqH7lid1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=763063B271DF62A4E6A6AA7F285E8ADD:FG=1; ZFY=6tZvIKPr71ZQJI:AL9CzZV8UXOTgsK9rht51t7yidMmM:C; BA_HECTOR=2ka02gak21258k842h1hc21gc14; ___wk_scode_token=0RzJzAvDvqgQibh7RV3MBKMrHHl9SxwNQPTtGegoS7A%3D; lscaptain=srcactivitycaptainindexcss_91e010cf-srccommonlibsesljs_e3d2f596-srcactivitycaptainindexjs_a2e9c712; delPer=0; PSINO=1; ab_sr=1.0.1_MDU2M2VkMmYyZDAzNGY4OGE2YjlkN2Y1MDEzODYyMmMzMGU3Yzk2M2ZjYWQzMDU3NTU3YTQxNjlkOTYwYzY2ZmJlY2ZmMTUwNWEzZDUxYTQwNGE1NjQxZGEyZDE4ZDBmODlhMzU2NGU0MDBkMTg3MjJmMGI4OTA1NWUwN2Q1MTZmMjhhMjkxZGEzMzhkMGQ4ZDI1Y2RlZjRjOTljYWRhYw==; H_PS_PSSID=36550_36502_36454_36690_36165_36694_36698_36653_36775_36746_36763_36768_36766_26350_36469_36712_36651; Hm_lvt_68bd357b1731c0f15d8dbfef8c216d15=1655651590,1655651973,1656856116,1656894526; Hm_lpvt_68bd357b1731c0f15d8dbfef8c216d15=1656894526',
#     'referer': 'https://www.baidu.com/s?ie=UTF-8&wd=%E7%96%AB%E6%83%85',
#     'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-site',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
#     'Connection': 'close'
# }


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
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]

# random_agent = USER_AGENTS[randint(0, len(USER_AGENTS) - 1)]
# Headers = {
#     'User-Agent': random_agent,
#     'Connection': 'close'
# }

id = input("请输入作者id")
company = input("请输入对应平台，例：patreon、fanbox、gumroad、subscribestar、dlsite、discord、fantia")
writer = input("请输入作者名字")


def getLink():
    link1 = []
    allPage = []
    link3 = []
    newLink = []
    # 解析文本
    count1 = 0
    trycount = input("请输入重试次数")
    urllib3.disable_warnings()  # 等价于requests.packages.urllib3.disable_warnings()
    for k in range(0, 1000, 50):
        # print(f"https://kemono.party/gumroad/user/3673970992772?o={k}")
        # 获取所有页面
        # url = f"https://kemono.party/{company}/user/{id}?o={k}"
        url = f"https://kemono.party/{company}/user/{id}?o={k}"
        # url = f"https://kemono.party/fantia/user/7?o={k}"
        # 使用列表接收所有作品页面链接
        link1.append(url)
        # 获取相对页面响应
        # response = requests.get(url, headers=Headers)
        # response = requests.get(url, headers=Headers)

        for lk in range(int(trycount)):

            try:
                proxies = None
                response = requests.get(url, headers=Headers, verify=False, proxies=None, timeout=3)
                if response.status_code == 200:
                    break
            except:
                # logdebug('requests failed one time')
                try:
                    proxies = None
                    response = requests.get(url, headers=Headers, verify=False, proxies=None, timeout=3)
                    if response.status_code == 200:
                        break
                except:
                    # logdebug('requests failed two time')
                    print('requests failed two time')
        # 转文本
        html = response.text
        # 创建bs对象
        bs = BeautifulSoup(html, "html.parser")
        # 这个循环只有是一个页面，这是获取所有页面内作品的循环
        # print(html)

        # yemian = bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['fancy-link'])
        # yemian = bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['pagination-mobile'])
        yemian = bs.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['card-list__items'])
        # article = yemian.find_all(lambda tag: tag.name == 'article' and tag.get('class') == ['post-card'])
        # yemian = bs.find_all(lambda tag: tag.name == 'article' and tag.get('data-id') == ['image-link'])
        # yemian = bs.find_all(lambda tag: tag.name == 'article' and tag.get('class') == ['image-link'])
        # print(yemian)
        data_id = re.findall('(?<=data-id=").*?(?=")', str(yemian))
        data_service = re.findall('(?<=data-service=").*?(?=")', str(yemian))
        data_service = company
        data_user = id
        # data_user = re.findall('(?<=data-user=").*?(?=")', str(html))
        # data_user = data_user[0]
        # print("output", data_id)
        # print("output", data_service)
        # print("output", data_user)
        count = 0
        for i in range(len(data_id)):
            if data_service[0] != "discord":
                link3.append(f"https://kemono.party/{data_service}/user/{data_user}/post/" + "".join(map(str, data_id[i])))
                newLink.append(f"https://kemono.party/{data_service}/user/{data_user}/post/" + "".join(map(str, data_id[i])))
            else:
                # newLink.append(f"https://kemono.party/{data_service}/user/{data_user}/post/" "".join(map(str, link3[i])))
                pass
        print(f"第{count1}页, 作品数量：{len(data_id)}", "当前数组长度：", len(newLink), "数组详情", link3)
        link3 = []
        count1 += 1
        # time.sleep(1)
    # time.sleep(3)
        # print(newLink)






        # print("output", article)
        # yemian1 = bs.find_all(lambda tag: tag.name == 'a')
        # print("yemian", yemian)
        # link3 = re.findall('(?<=data-id=").*?(?=")', str(html))
        # print(link3)
        # print(re.findall('(?<=href=").*?(?=")', str(yemian1)))
        # print("yemian", yemia1n)
        # count = 0
        # for i in range(len(link3)):
        #     if company != "discord":
        #         newLink.append(f"https://kemono.party/{company}/post/" + "".join(map(str, link3[i])))
        #     else:
        #         newLink.append(f"https://kemono.party/{company}/post/" "".join(map(str, link3[i])))
        # print(f"第{count}页")
        # print(link3)
        # count += 1
    #     print(yemian)
    #     # [<a class="fancy-link" href="/fanbox/user/273185/post/4468387" rel="noopener noreferrer" target="_blank">
    #     for i in range(len(yemian)):
    #         # print(yemian[i])
    #         # print(yemian)
    #         data = re.findall('(?<=href=").*?(?=\")', str(yemian[i-1]))
    #         # print(data)
    #         if data == "', '\" rel=":
    #             continue
    #         else:
    #             allPage.append("".join(data))
    #             # print(allPage)
    # allPage.pop(0)
    # print(allPage)
    # for j in range(len(allPage)):
    #     link.append("https://kemono.party" + "".join(map(str, allPage[j])))
    # print(link)


    return newLink








if __name__ == "__main__":
    getLink()
