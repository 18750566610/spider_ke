import fanbox.MANA.oldProject.spider.fanbox.MANA.file as ALLPage
import requests
from bs4 import BeautifulSoup
from subprocess import call
import os
import re
import time

# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.get("https://kemono.party/fanbox/user/6049901/post/1438388")
# text = driver.find_elements_by_class_name("post__content")
# print(text[0].text)
# driver.quit()


downloadLink = []
imgLink = []
AllLink = []
link1 = []


def transFrom():
    link = ALLPage.getLink()
    # link = ['https://kemono.party/fanbox/user/273185/post/4468387', 'https://kemono.party/fanbox/user/273185/post/4461391', 'https://kemono.party/fanbox/user/273185/post/4433399', 'https://kemono.party/fanbox/user/273185/post/4429224', 'https://kemono.party/fanbox/user/273185/post/4403493', 'https://kemono.party/fanbox/user/273185/post/4403313', 'https://kemono.party/fanbox/user/273185/post/4391057', 'https://kemono.party/fanbox/user/273185/post/4390971', 'https://kemono.party/fanbox/user/273185/post/4370111', 'https://kemono.party/fanbox/user/273185/post/4370079', 'https://kemono.party/fanbox/user/273185/post/4369535', 'https://kemono.party/fanbox/user/273185/post/4369601', 'https://kemono.party/fanbox/user/273185/post/4369513', 'https://kemono.party/fanbox/user/273185/post/4371793', 'https://kemono.party/fanbox/user/273185/post/4315442', 'https://kemono.party/fanbox/user/273185/post/4315388', 'https://kemono.party/fanbox/user/273185/post/4315301', 'https://kemono.party/fanbox/user/273185/post/4281517', 'https://kemono.party/fanbox/user/273185/post/4281414', 'https://kemono.party/fanbox/user/273185/post/4276764', 'https://kemono.party/fanbox/user/273185/post/4248910', 'https://kemono.party/fanbox/user/273185/post/4248889', 'https://kemono.party/fanbox/user/273185/post/4233651', 'https://kemono.party/fanbox/user/273185/post/4233081', 'https://kemono.party/fanbox/user/273185/post/4214581', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/4214495', 'https://kemono.party/fanbox/user/273185/post/4214262', 'https://kemono.party/fanbox/user/273185/post/4213966', 'https://kemono.party/fanbox/user/273185/post/4214152', 'https://kemono.party/fanbox/user/273185/post/4187801', 'https://kemono.party/fanbox/user/273185/post/4181035', 'https://kemono.party/fanbox/user/273185/post/4176076', 'https://kemono.party/fanbox/user/273185/post/4166465', 'https://kemono.party/fanbox/user/273185/post/4155248', 'https://kemono.party/fanbox/user/273185/post/4148478', 'https://kemono.party/fanbox/user/273185/post/4142771', 'https://kemono.party/fanbox/user/273185/post/4115408', 'https://kemono.party/fanbox/user/273185/post/4111403', 'https://kemono.party/fanbox/user/273185/post/4091909', 'https://kemono.party/fanbox/user/273185/post/4088788', 'https://kemono.party/fanbox/user/273185/post/4080376', 'https://kemono.party/fanbox/user/273185/post/4076954', 'https://kemono.party/fanbox/user/273185/post/4073838', 'https://kemono.party/fanbox/user/273185/post/4061083', 'https://kemono.party/fanbox/user/273185/post/4061049', 'https://kemono.party/fanbox/user/273185/post/4061059', 'https://kemono.party/fanbox/user/273185/post/4054194', 'https://kemono.party/fanbox/user/273185/post/4036855', 'https://kemono.party/fanbox/user/273185/post/4030538', 'https://kemono.party/fanbox/user/273185/post/4026388', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/4013878', 'https://kemono.party/fanbox/user/273185/post/4008520', 'https://kemono.party/fanbox/user/273185/post/3974845', 'https://kemono.party/fanbox/user/273185/post/3972410', 'https://kemono.party/fanbox/user/273185/post/3948211', 'https://kemono.party/fanbox/user/273185/post/3941850', 'https://kemono.party/fanbox/user/273185/post/3926163', 'https://kemono.party/fanbox/user/273185/post/3920812', 'https://kemono.party/fanbox/user/273185/post/3916752', 'https://kemono.party/fanbox/user/273185/post/3916505', 'https://kemono.party/fanbox/user/273185/post/3914277', 'https://kemono.party/fanbox/user/273185/post/3914424', 'https://kemono.party/fanbox/user/273185/post/3914462', 'https://kemono.party/fanbox/user/273185/post/3914251', 'https://kemono.party/fanbox/user/273185/post/3880683', 'https://kemono.party/fanbox/user/273185/post/3871482', 'https://kemono.party/fanbox/user/273185/post/3866457', 'https://kemono.party/fanbox/user/273185/post/3840967', 'https://kemono.party/fanbox/user/273185/post/3835424', 'https://kemono.party/fanbox/user/273185/post/3818296', 'https://kemono.party/fanbox/user/273185/post/3808274', 'https://kemono.party/fanbox/user/273185/post/3802981', 'https://kemono.party/fanbox/user/273185/post/3779078', 'https://kemono.party/fanbox/user/273185/post/3777510', 'https://kemono.party/fanbox/user/273185/post/3777269', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/3769078', 'https://kemono.party/fanbox/user/273185/post/3763918', 'https://kemono.party/fanbox/user/273185/post/3763939', 'https://kemono.party/fanbox/user/273185/post/3763873', 'https://kemono.party/fanbox/user/273185/post/3741766', 'https://kemono.party/fanbox/user/273185/post/3736644', 'https://kemono.party/fanbox/user/273185/post/3730863', 'https://kemono.party/fanbox/user/273185/post/3730842', 'https://kemono.party/fanbox/user/273185/post/3705055', 'https://kemono.party/fanbox/user/273185/post/3700401', 'https://kemono.party/fanbox/user/273185/post/3675192', 'https://kemono.party/fanbox/user/273185/post/3669580', 'https://kemono.party/fanbox/user/273185/post/3643137', 'https://kemono.party/fanbox/user/273185/post/3641148', 'https://kemono.party/fanbox/user/273185/post/3637282', 'https://kemono.party/fanbox/user/273185/post/3633129', 'https://kemono.party/fanbox/user/273185/post/3631233', 'https://kemono.party/fanbox/user/273185/post/3619754', 'https://kemono.party/fanbox/user/273185/post/3619727', 'https://kemono.party/fanbox/user/273185/post/3619747', 'https://kemono.party/fanbox/user/273185/post/3619808', 'https://kemono.party/fanbox/user/273185/post/3605230', 'https://kemono.party/fanbox/user/273185/post/3603941', 'https://kemono.party/fanbox/user/273185/post/3598754', 'https://kemono.party/fanbox/user/273185/post/3574235', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/3569658', 'https://kemono.party/fanbox/user/273185/post/3538764', 'https://kemono.party/fanbox/user/273185/post/3537461', 'https://kemono.party/fanbox/user/273185/post/3528442', 'https://kemono.party/fanbox/user/273185/post/3514530', 'https://kemono.party/fanbox/user/273185/post/3507609', 'https://kemono.party/fanbox/user/273185/post/3486955', 'https://kemono.party/fanbox/user/273185/post/3486894', 'https://kemono.party/fanbox/user/273185/post/3485837', 'https://kemono.party/fanbox/user/273185/post/3482276', 'https://kemono.party/fanbox/user/273185/post/3477838', 'https://kemono.party/fanbox/user/273185/post/3478275', 'https://kemono.party/fanbox/user/273185/post/3477722', 'https://kemono.party/fanbox/user/273185/post/3450880', 'https://kemono.party/fanbox/user/273185/post/3445919', 'https://kemono.party/fanbox/user/273185/post/3441231', 'https://kemono.party/fanbox/user/273185/post/3439535', 'https://kemono.party/fanbox/user/273185/post/3424737', 'https://kemono.party/fanbox/user/273185/post/3408482', 'https://kemono.party/fanbox/user/273185/post/3407190', 'https://kemono.party/fanbox/user/273185/post/3377291', 'https://kemono.party/fanbox/user/273185/post/3376226', 'https://kemono.party/fanbox/user/273185/post/3353715', 'https://kemono.party/fanbox/user/273185/post/3353702', 'https://kemono.party/fanbox/user/273185/post/3356579', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/3354934', 'https://kemono.party/fanbox/user/273185/post/3348921', 'https://kemono.party/fanbox/user/273185/post/3348772', 'https://kemono.party/fanbox/user/273185/post/3348858', 'https://kemono.party/fanbox/user/273185/post/3329634', 'https://kemono.party/fanbox/user/273185/post/3317115', 'https://kemono.party/fanbox/user/273185/post/3308359', 'https://kemono.party/fanbox/user/273185/post/3307019', 'https://kemono.party/fanbox/user/273185/post/3278268', 'https://kemono.party/fanbox/user/273185/post/3276463', 'https://kemono.party/fanbox/user/273185/post/3249854', 'https://kemono.party/fanbox/user/273185/post/3246530', 'https://kemono.party/fanbox/user/273185/post/3236922', 'https://kemono.party/fanbox/user/273185/post/3224653', 'https://kemono.party/fanbox/user/273185/post/3224555', 'https://kemono.party/fanbox/user/273185/post/3220252', 'https://kemono.party/fanbox/user/273185/post/3201691', 'https://kemono.party/fanbox/user/273185/post/3191438', 'https://kemono.party/fanbox/user/273185/post/3188569', 'https://kemono.party/fanbox/user/273185/post/3188579', 'https://kemono.party/fanbox/user/273185/post/3188527', 'https://kemono.party/fanbox/user/273185/post/3182837', 'https://kemono.party/fanbox/user/273185/post/3175827', 'https://kemono.party/fanbox/user/273185/post/3145465', 'https://kemono.party/fanbox/user/273185/post/3142924', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/3128511', 'https://kemono.party/fanbox/user/273185/post/3117165', 'https://kemono.party/fanbox/user/273185/post/3117124', 'https://kemono.party/fanbox/user/273185/post/3089338', 'https://kemono.party/fanbox/user/273185/post/3087775', 'https://kemono.party/fanbox/user/273185/post/3079167', 'https://kemono.party/fanbox/user/273185/post/3074726', 'https://kemono.party/fanbox/user/273185/post/3072073', 'https://kemono.party/fanbox/user/273185/post/3072124', 'https://kemono.party/fanbox/user/273185/post/3072020', 'https://kemono.party/fanbox/user/273185/post/3071723', 'https://kemono.party/fanbox/user/273185/post/3063078', 'https://kemono.party/fanbox/user/273185/post/3061876', 'https://kemono.party/fanbox/user/273185/post/3060735', 'https://kemono.party/fanbox/user/273185/post/3026224', 'https://kemono.party/fanbox/user/273185/post/3025255', 'https://kemono.party/fanbox/user/273185/post/3020734', 'https://kemono.party/fanbox/user/273185/post/2996310', 'https://kemono.party/fanbox/user/273185/post/2996177', 'https://kemono.party/fanbox/user/273185/post/2972793', 'https://kemono.party/fanbox/user/273185/post/2969945', 'https://kemono.party/fanbox/user/273185/post/2945012', 'https://kemono.party/fanbox/user/273185/post/2944998', 'https://kemono.party/fanbox/user/273185/post/2944971', 'https://kemono.party/fanbox/user/273185/post/2944905', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/2937386', 'https://kemono.party/fanbox/user/273185/post/2937199', 'https://kemono.party/fanbox/user/273185/post/2937413', 'https://kemono.party/fanbox/user/273185/post/2906140', 'https://kemono.party/fanbox/user/273185/post/2906039', 'https://kemono.party/fanbox/user/273185/post/2903230', 'https://kemono.party/fanbox/user/273185/post/2898563', 'https://kemono.party/fanbox/user/273185/post/2877436', 'https://kemono.party/fanbox/user/273185/post/2874833', 'https://kemono.party/fanbox/user/273185/post/2848927', 'https://kemono.party/fanbox/user/273185/post/2846514', 'https://kemono.party/fanbox/user/273185/post/2821781', 'https://kemono.party/fanbox/user/273185/post/2821776', 'https://kemono.party/fanbox/user/273185/post/2816857', 'https://kemono.party/fanbox/user/273185/post/2815823', 'https://kemono.party/fanbox/user/273185/post/2809483', 'https://kemono.party/fanbox/user/273185/post/2809441', 'https://kemono.party/fanbox/user/273185/post/2809918', 'https://kemono.party/fanbox/user/273185/post/2795507', 'https://kemono.party/fanbox/user/273185/post/2783578', 'https://kemono.party/fanbox/user/273185/post/2772610', 'https://kemono.party/fanbox/user/273185/post/2770100', 'https://kemono.party/fanbox/user/273185/post/2749146', 'https://kemono.party/fanbox/user/273185/post/2749111', 'https://kemono.party/fanbox/user/273185/post/2720583', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/2720561', 'https://kemono.party/fanbox/user/273185/post/2710369', 'https://kemono.party/fanbox/user/273185/post/2695213', 'https://kemono.party/fanbox/user/273185/post/2695196', 'https://kemono.party/fanbox/user/273185/post/2687990', 'https://kemono.party/fanbox/user/273185/post/2687952', 'https://kemono.party/fanbox/user/273185/post/2682473', 'https://kemono.party/fanbox/user/273185/post/2681505', 'https://kemono.party/fanbox/user/273185/post/2681460', 'https://kemono.party/fanbox/user/273185/post/2658093', 'https://kemono.party/fanbox/user/273185/post/2656230', 'https://kemono.party/fanbox/user/273185/post/2654430', 'https://kemono.party/fanbox/user/273185/post/2631127', 'https://kemono.party/fanbox/user/273185/post/2631015', 'https://kemono.party/fanbox/user/273185/post/2623044', 'https://kemono.party/fanbox/user/273185/post/2599591', 'https://kemono.party/fanbox/user/273185/post/2599517', 'https://kemono.party/fanbox/user/273185/post/2562072', 'https://kemono.party/fanbox/user/273185/post/2562061', 'https://kemono.party/fanbox/user/273185/post/2560399', 'https://kemono.party/fanbox/user/273185/post/2556848', 'https://kemono.party/fanbox/user/273185/post/2548113', 'https://kemono.party/fanbox/user/273185/post/2548147', 'https://kemono.party/fanbox/user/273185/post/2548216', 'https://kemono.party/fanbox/user/273185/post/2528188', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/2526028', 'https://kemono.party/fanbox/user/273185/post/2518354', 'https://kemono.party/fanbox/user/273185/post/2513678', 'https://kemono.party/fanbox/user/273185/post/2503414', 'https://kemono.party/fanbox/user/273185/post/2499731', 'https://kemono.party/fanbox/user/273185/post/2470268', 'https://kemono.party/fanbox/user/273185/post/2470145', 'https://kemono.party/fanbox/user/273185/post/2441094', 'https://kemono.party/fanbox/user/273185/post/2441069', 'https://kemono.party/fanbox/user/273185/post/2435163', 'https://kemono.party/fanbox/user/273185/post/2432831', 'https://kemono.party/fanbox/user/273185/post/2427545', 'https://kemono.party/fanbox/user/273185/post/2427477', 'https://kemono.party/fanbox/user/273185/post/2427471', 'https://kemono.party/fanbox/user/273185/post/2427242', 'https://kemono.party/fanbox/user/273185/post/2419160', 'https://kemono.party/fanbox/user/273185/post/2404769', 'https://kemono.party/fanbox/user/273185/post/2401881', 'https://kemono.party/fanbox/user/273185/post/2383251', 'https://kemono.party/fanbox/user/273185/post/2379638', 'https://kemono.party/fanbox/user/273185/post/2349889', 'https://kemono.party/fanbox/user/273185/post/2349597', 'https://kemono.party/fanbox/user/273185/post/2339865', 'https://kemono.party/fanbox/user/273185/post/2322376', 'https://kemono.party/fanbox/user/273185/post/2322297', 'https://kemono.party" rel=', 'https://kemono.party/fanbox/user/273185/post/2318477', 'https://kemono.party/fanbox/user/273185/post/2317823', 'https://kemono.party/fanbox/user/273185/post/2305401', 'https://kemono.party/fanbox/user/273185/post/2305358', 'https://kemono.party/fanbox/user/273185/post/2278794', 'https://kemono.party/fanbox/user/273185/post/2278746', 'https://kemono.party/fanbox/user/273185/post/2278732', 'https://kemono.party/fanbox/user/273185/post/2276864', 'https://kemono.party/fanbox/user/273185/post/2265129', 'https://kemono.party/fanbox/user/273185/post/2250982', 'https://kemono.party/fanbox/user/273185/post/2251016', 'https://kemono.party/fanbox/user/273185/post/2224517', 'https://kemono.party/fanbox/user/273185/post/2224267', 'https://kemono.party/fanbox/user/273185/post/2199683', 'https://kemono.party/fanbox/user/273185/post/2199578', 'https://kemono.party/fanbox/user/273185/post/2196214', 'https://kemono.party/fanbox/user/273185/post/2192657', 'https://kemono.party/fanbox/user/273185/post/2182110', 'https://kemono.party/fanbox/user/273185/post/2181990', 'https://kemono.party/fanbox/user/273185/post/2181972', 'https://kemono.party/fanbox/user/273185/post/2182008', 'https://kemono.party/fanbox/user/273185/post/2165555', 'https://kemono.party/fanbox/user/273185/post/2165917', 'https://kemono.party/fanbox/user/273185/post/2162216', 'https://kemono.party/fanbox/user/273185/post/2147182']

    # print(str(link))
    for i in link:
        if i == 'https://kemono.party" rel=':
            continue
        else:
            link1.append(i)
    print(link1)
    return link1


def getWorkLink():
    link = transFrom()
    print("worklink:", link)
    trycount = input("请输入重试次数")
    for i in range(len(link)):
        print(i, "个info")
        url = link[i]
        # try:
        #     response = requests.get(url, headers=ALLPage.Headers)
        # except:
        #     response = requests.get(url, headers=ALLPage.Headers)

        for lk in range(int(trycount)):
            try:
                proxies = None
                response = requests.get(url, headers=ALLPage.Headers, verify=False, proxies=None, timeout=3)
                if response.status_code == 200:
                    print('Code:{}'.format(response.status_code))
                    break
            except:
                # logdebug('requests failed one time')
                try:
                    proxies = None
                    response = requests.get(url, headers=ALLPage.Headers, verify=False, proxies=None, timeout=3)
                    if response.status_code == 200:
                        print('Code:{}'.format(response.status_code))
                        break
                except:
                    # logdebug('requests failed two time')
                    print('requests failed two time')

        # print(response)

        # response = requests.get(url, headers=ALLPage.Headers, verify=False)
        html = response.text
        bs = BeautifulSoup(html, "lxml")
        # print(bs)
        # GetWorkLink
        count = 0
        for j in bs.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['post__content']):
            # for j in bs.find_all(lambda tag: tag.name == 'div'):
            # print("j", j)
            txt1 = j.text
            print(txt1)
            print(i)

            # print(type(txt1))
            # txt = "".format(j)
            # count += 1
            # print(txt)



            txt = open(f"./txt/{ALLPage.writer}_content.txt", "a", encoding="utf-8")
            count1 = i
            int(count1)
            print(count1)
            text1 = f"{count1}个info"
            # txt.write(str(count1))
            txt.write(text1)
            txt.write(txt1)
            txt.write("\n")
            count += 1


if __name__ == "__main__":
    # getWorkLink()
    # getImageLink()
    # downloadWorkLink()
    # downloadImgLink()
    getWorkLink()
