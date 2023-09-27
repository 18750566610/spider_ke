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
    link1 = []
    allPage = []
    link = []
    url = "https://kemono.party/patreon/user/12281898?o=0"

    # 解析文本
    for k in range(0, 600, 25):
        # print(f"https://kemono.party/patreon/user/12281898?o={k}")
        # 获取所有页面
        url = f"https://kemono.party/fanbox/user/871625?o={k}"
        # 使用列表接收所有作品页面链接
        link1.append(url)
        # 获取相对页面响应
        response = requests.get(url, headers=Headers)
        # 转文本
        html = response.text
        # 创建bs对象
        bs = BeautifulSoup(html, "lxml")
        # 这个循环只有是一个页面，这是获取所有页面内作品的循环
        yemian = bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['fancy-link'])
        # print(yemian)
        # [<a class="fancy-link" href="/fanbox/user/273185/post/4468387" rel="noopener noreferrer" target="_blank">
        for i in range(len(yemian)):
            # print(yemian[i])
            # print(yemian)
            data = re.findall('(?<=href=").*?(?=\")', str(yemian[i-1]))
            # print(data)
            if data == "', '\" rel=":
                continue
            else:
                allPage.append("".join(data))
                # print(allPage)
    allPage.pop(0)
    print(allPage)
    for j in range(len(allPage)):
        link.append("https://kemono.party" + "".join(map(str, allPage[j])))
    print(link)
    return link








if __name__ == "__main__":
    getLink()
