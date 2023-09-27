import requests
from bs4 import BeautifulSoup
import re

Headers = {
    'cookie': 'BIDUPSID=580FD855A26DCE31E1BEBB360D3772C1; PSTM=1633847655; __yjs_duid=1_24793f6b65b6620080c9b77e3ad3584c1633863356918; MCITY=-%3A; BAIDUID=763063B271DF62A4E6A6AA7F285E8ADD:FG=1; BDUSS=hhaVZDZEV-TDNXbjRQfnVDclVDSVk0alRwWHFZR0VYZUZyZHlDdlNlRXFyT0JpRVFBQUFBJCQAAAAAAQAAAAEAAABTx7AqTWFrb9zU19NfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACofuWIqH7lid1; BDUSS_BFESS=hhaVZDZEV-TDNXbjRQfnVDclVDSVk0alRwWHFZR0VYZUZyZHlDdlNlRXFyT0JpRVFBQUFBJCQAAAAAAQAAAAEAAABTx7AqTWFrb9zU19NfAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACofuWIqH7lid1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=763063B271DF62A4E6A6AA7F285E8ADD:FG=1; ZFY=6tZvIKPr71ZQJI:AL9CzZV8UXOTgsK9rht51t7yidMmM:C; BA_HECTOR=2ka02gak21258k842h1hc21gc14; ___wk_scode_token=0RzJzAvDvqgQibh7RV3MBKMrHHl9SxwNQPTtGegoS7A%3D; lscaptain=srcactivitycaptainindexcss_91e010cf-srccommonlibsesljs_e3d2f596-srcactivitycaptainindexjs_a2e9c712; delPer=0; PSINO=1; ab_sr=1.0.1_MDU2M2VkMmYyZDAzNGY4OGE2YjlkN2Y1MDEzODYyMmMzMGU3Yzk2M2ZjYWQzMDU3NTU3YTQxNjlkOTYwYzY2ZmJlY2ZmMTUwNWEzZDUxYTQwNGE1NjQxZGEyZDE4ZDBmODlhMzU2NGU0MDBkMTg3MjJmMGI4OTA1NWUwN2Q1MTZmMjhhMjkxZGEzMzhkMGQ4ZDI1Y2RlZjRjOTljYWRhYw==; H_PS_PSSID=36550_36502_36454_36690_36165_36694_36698_36653_36775_36746_36763_36768_36766_26350_36469_36712_36651; Hm_lvt_68bd357b1731c0f15d8dbfef8c216d15=1655651590,1655651973,1656856116,1656894526; Hm_lpvt_68bd357b1731c0f15d8dbfef8c216d15=1656894526',
    'referer': 'https://www.baidu.com/s?ie=UTF-8&wd=%E7%96%AB%E6%83%85',
    'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    'Connection': 'close'
}


def getLink():
    # 定义变量区域
    linkpart = []  # 画师作品链接
    link = []  # 画师作品链接
    url = ""
    # 链接
    for k in range(0, 500, 25):
        # print(f"https://kemono.party/fanbox/user/273185?o={k}")
        url = f"https://kemono.party/fanbox/user/273185?o={k}"
        # 获取
        response = requests.get(url, headers=Headers, proxies={"http": None, "https": None})

        # 转文本
        html = response.text

        # 解析文本
        bs = BeautifulSoup(html, "lxml")

        # 取a标签
        html1 = bs.find_all("a")

        # 取画师作品页面链接(部分)
        for i in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['fancy-link']):
            # print(i)
            data = re.findall('(?<=href=").*?(?=\")', str(i))
            # print(data)
            linkpart.append(data)
        # print(linkpart)

        # 取画师作品页面链接（整体）
        for j in range(len(linkpart) - 1):
            link.append("https://kemono.party" + "".join(map(str, linkpart[j])))
        # print(link)
    list1 = [link, url]
    return list1


if __name__ == "__main__":
    getLink()
