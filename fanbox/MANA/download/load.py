import pymysql
from six import unichr
import random
import fanbox.MANA.sql.DOWNLOAD as download
from subprocess import call
import os
import urllib3
import requests
from bs4 import BeautifulSoup
import re
import json
import pymysql
import os

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='kemono_id',
    charset='utf8')

# 获取游标
cursor = db.cursor()


def strB2Q(ustring):
    """半角转全角"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # 半角空格直接转化
            inside_code = 12288
        elif 32 <= inside_code <= 126:  # 半角字符（除空格）根据关系转化
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring


def SQL_Select():
    sql1 = '''
        SELECT * FROM worklink
    '''
    cursor.execute(sql1)
    db.commit()
    result = cursor.fetchall()
    result = list(map(list, result))
    # print(result)
    return result


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


def titlecheck(title):  # 修改文件名不符合window的特殊字符
    char_list = ['*', '|', ':', '?', '/', '<', '>', '"', '\\']
    re_title_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
    news_title = ''
    for i in title:
        j = random.randint(0, 25)
        if i in char_list:
            news_title = news_title + re_title_list[j]
        else:
            news_title = news_title + i
    return news_title


def IDMDownload(filepath, url, filename):
    IDMPath = "C:\Program Files (x86)\Internet Download Manager"
    IDM = "IDMan.exe"
    os.chdir(IDMPath)
    call([IDM, '/d', url, '/p', filepath, '/f', filename, '/a'])
    call([IDM, '/s'])
    return 0


def downloadLink(lllink1):
    # lllink = ['https://kemono.party/data/78/25/7825f699efa17b64caf4b9103e9b8754819e4f56ba69a055af39fa1fe7e84193.zip?f=Yoimiya02_PT.zip', 'https://kemono.party/data/f9/18/f9184d402d57a3c25896f1fb2fac8e1f22db7877aa00d65d279569e3fe3d23e2.zip?f=Yoimiya02_PTss.zip', 'https://kemono.party/data/4b/4a/4b4a25ac7ce9e8dfe96054bbebba0eb3dbd3d2941c8c321c915b4538934ee057.zip?f=Yoimiya01_PT.zip', 'https://kemono.party/data/d5/c1/d5c1d1da0bdcdef533408b3bae46ad794dac234e5904cdd0f5e91e0515cda8d6.zip?f=Yelan_06.zip', 'https://kemono.party/data/f5/79/f579920a814585754c7a1d8c9bfd16f966ed499034f3d1436d29f3697b194f42.zip?f=Yelan_06ss.zip', 'https://kemono.party/data/9a/54/9a54b54a1b956017e730908d1820c3c18881fbe85ff56b78851f45edf2759524.zip?f=GBF_unc.zip', 'https://kemono.party/data/10/3f/103fca88290b1494d9c8e8c724793563c8fe5cb109498ff0914c0253434a2dcb.zip?f=Yelan_05_e_bns.zip', 'https://kemono.party/data/4e/1e/4e1e9ab0609a8b47840642b043ea474c6eeba537fb39b79c27035b9d0068af58.zip?f=Yelan_05_ab.zip', 'https://kemono.party/data/48/7e/487e3bde7974af3cb997978eb3185543f220e6c722363ea97aea981ed66534e2.zip?f=Yelan_05_cd.zip', 'https://kemono.party/data/88/b8/88b8475b8396ce7932cc372805b87187e8b8123b7a59ed02252fd7499cccf88e.zip?f=Yelan_05ss.zip', 'https://kemono.party/data/01/bc/01bca522794fbf94eff8adf03c8a22cc9575808e731aa2ebe5e8e1b02f75603e.zip?f=Yelan_04_c.zip', 'https://kemono.party/data/05/aa/05aa4543aea906a2d5585089a10c18cbac676d8123227371a60a5cb94d4c539e.zip?f=Yelan_04_ab.zip', 'https://kemono.party/data/64/fc/64fc0324ade0680b63738dea24753abad1f5bba06851990483e9aed33e08d05d.zip?f=Yelan_04_dex.zip', 'https://kemono.party/data/12/07/12075658b0e525964020ef63023d050c23c8439a8d872d35c43e75ac64a900b6.zip?f=Yelan_04_ss.zip', 'https://kemono.party/data/ac/70/ac7025c7a7b631d71566eeb39b63ea3352a635931bbea7e0437dcae163c26f0a.zip?f=Yelan_03ab.zip', 'https://kemono.party/data/3f/cd/3fcddcaf280f435304a93ba81b8d9ba5ac9ec1be7c1c7375e004ee2a9f785ee8.zip?f=Yelan_03cd.zip', 'https://kemono.party/data/6b/de/6bde68ce8afb77551228bd8e09f2947bb62ef46c6bd0695632ea9755d5a578c4.zip?f=Yelan_03ss.zip', 'https://kemono.party/data/15/42/15429a222020dd68ce2cd475ae1e47d1f4938450c18d8d6be8861ad3484763fd.zip?f=Yelan_02_FHD.zip', 'https://kemono.party/data/01/d0/01d054c7cbc6bb8fcf4a6f0a65c45f9eade67a69fd089f4a4d44352cc7eb9641.zip?f=Yelan_02_HD.zip', 'https://kemono.party/data/f0/55/f055d9f1eca9b026582dd468a0debbb8393c2f7087d24c306f93731ba9807ebd.zip?f=GCR4.zip', 'https://kemono.party/data/c1/18/c118544613301b1e38451936b8679cdb84d96be2fd1b30655b3260d0784340a5.zip?f=Yelan_01.zip', 'https://kemono.party/data/1b/61/1b6114b61cfccf74efc439040f4f22aa39eadd4212a965588aa49c8a188bdcf9.zip?f=Keqing_05.zip', 'https://kemono.party/data/43/2b/432b657bcdab7ce1bd8acdd403d482d18f912e73630ffbf5225cfabceeaba9db.zip?f=Keqing_05ss.zip', 'https://kemono.party/data/40/d8/40d871bc8e0367b2ee628f5cdc92cf527ad46ef5d938601f37b0190303f86127.zip?f=GCR3K_unc.zip', 'https://kemono.party/data/2f/9f/2f9f06c75597a4df53d8ea69728284aa812ee08e2f60ba5cc18c449adc54cdb9.zip?f=Keqing_04.zip', 'https://kemono.party/data/03/a8/03a8b8d46c5153c15d0ed60e7360e7889aa5fc5be1a7de9dd81f495f8612fddd.zip?f=Keqing_04ss.zip', 'https://kemono.party/data/55/b3/55b3c3776f39808705113d4647f8191207151fa2a03b3fc6d372e5c3922c6717.zip?f=Keqing_03.zip', 'https://kemono.party/data/1e/87/1e87e97dfed2a75ac2f68c0b4a0a6ca664df3cbba77bfbd090a4c5b4a486bae9.zip?f=Keqing_03ss.zip', 'https://kemono.party/data/c2/99/c299967e96c0cbe5bc11ef02ecf6f39cc153883d0d8787340e4d50e018d5fa84.zip?f=Keqing_02.zip', 'https://kemono.party/data/57/42/57423d80ff089547c98af6375e843caf7f34dfa8858cc3478e24341cfb8c0fae.zip?f=Keqing_02ss.zip', 'https://kemono.party/data/18/95/1895ffd5ea70790fd42ba7a7bcfe61d50673d53e5381011b5765d8047abbdb6f.zip?f=GCR3A_unc.zip', 'https://kemono.party/data/0c/ee/0cee244d52c08bb1b9488ca41311cb7dc3fd5605dea55caa2dcf54b3c04827d3.zip?f=Keqing_01.zip', 'https://kemono.party/data/7e/af/7eaf946b4bed01b7daa8f73ba9c826143408c906a1268fa2865208ab0f70ce6d.zip?f=Keqing_01ss.zip', 'https://kemono.party/data/4b/bd/4bbd1bab2de6fb6ae2f1896b690620744812b0ec330e04424d299f88504a5ea5.zip?f=MIKO_04.zip', 'https://kemono.party/data/78/f8/78f8491608951ed62acbb3d60adae2e9f2c265ccbb0d86369ce37f2dc5e36325.zip?f=MIKO_04ss.zip', 'https://kemono.party/data/ea/83/ea83ac5d9d2cc056ed6081bdf60036c48a5edc2c848d1215dfdb3c6d7c1c62c6.zip?f=MIKO_03.zip', 'https://kemono.party/data/b3/cc/b3cca761b29fe9269faef6f82f1b5cfe67e103efa649fa9b0a3877c9e3d795cd.zip?f=MIKO_03ss.zip', 'https://kemono.party/data/6d/50/6d50998748b5d83a6a66d0ab2134cd1cdee305e6095ae559dee60d6e4c0b8d87.zip?f=MIKO_02.zip', 'https://kemono.party/data/17/f9/17f93d797b368a2c96c97930431296018aeb00ea9307991f35cc48c13c8644bc.zip?f=MIKO_02ss.zip', 'https://kemono.party/data/49/a6/49a6325ec9233061fba66020c0b2c8867c2f1372b7eaa299d39e4b497fb8b989.zip?f=GCR2K_unc.zip', 'https://kemono.party/data/20/ac/20ac51412e124db7e7f9229fc45cd03dee2d4cdfbb537c04382626ff2ceec403.zip?f=MIKO_01.zip', 'https://kemono.party/data/8d/07/8d078b4121cbc538ca81ac7475afdfa2454eb0a20a93c277c54c2d19b1f67999.zip?f=EULA%2BAMBER_04.zip', 'https://kemono.party/data/64/b7/64b714eb7dd5cdeeb705e5a4407e374abd271e5a9354bd6d7cdc4ea6d15ee0f6.zip?f=EULA%2BAMBER_04_ss.zip', 'https://kemono.party/data/75/c6/75c6d5bd10e6e37ce1a83f8b0510bfa5d7ef5cbf6b8438a37aa87e8dbd970a72.zip?f=EULA%2BAMBER_03.zip', 'https://kemono.party/data/bc/c7/bcc766ab990ca54b3a4e681c78eff734bd3350528586c6d976a286130f8b8672.zip?f=EULA%2BAMBER_03_ss.zip', 'https://kemono.party/data/19/8f/198f87c65e6659041e25d3c04b26f443dfe601b0c15bda0954bb7c6a9d9a14be.zip?f=EULA%2BAMBER_02.zip', 'https://kemono.party/data/fd/93/fd937f84dd879f0916f00d7e62f1f4506db70c7b8e13f9a0941208e44f962128.zip?f=EULA%2BAMBER_02_ss.zip', 'https://kemono.party/data/89/3f/893f455a338985d472955abbb9c8088e763547e8b20bb725242cca0ac722ae93.zip?f=EULA%2BAMBER_01.zip', 'https://kemono.party/data/de/97/de97e8c331b7c7f22977b708156fae70895d063feff2ea82add77f3474ef1d96.zip?f=Shenhe04.zip', 'https://kemono.party/data/a4/a2/a4a2ce3739095c75280c278ae0c5b5f0949a8f07fe8841cbfd3bae149843f4d0.zip?f=Shenhe04_ss.zip', 'https://kemono.party/data/0d/3d/0d3d092c4e2570b20a5ab00b654683882069e2510d7b10df1d0ccdb67df180be.zip?f=Shenhe03.zip', 'https://kemono.party/data/6b/30/6b30440b987f3f0cef9660182d2cab9270262771b6f418a9f33658fa51e07450.zip?f=Shenhe03_ss.zip', 'https://kemono.party/data/c6/47/c647ed57418af4a6201a5be5fc3f2a58acc73a5a01e1c56c5d2a220cab905a7b.zip?f=Patreon.zip', 'https://kemono.party/data/bf/6c/bf6c08db68849b11256978c93ef7b5da03ccb7b7a8000b7bf1191e21a513948e.zip?f=Patreon_s.zip', 'https://kemono.party/data/82/5e/825ef087fbda7d9dcc6286d001183ade905a6af2151518e36c0fd1d0eee01561.zip?f=GCR_unc.zip', 'https://kemono.party/data/76/fc/76fc1fd27db8e862a6de71d9f1d8baabd189e1118a63f92cbcac59ec4a947fcd.zip?f=Shenhe02.zip', 'https://kemono.party/data/53/dd/53dd668e08e2671052185a7837d2882af48e985a2fe904a6f626b03452e4614a.zip?f=Shenhe02_ss.zip', 'https://kemono.party/data/11/81/118153fb97ab3d1f620312363554c04ae671c5dd16cc7605a4d0ad51e118c930.zip?f=Shenhe01.zip', 'https://kemono.party/data/bc/aa/bcaa79f9c5cc93bae141a3f9a897deeec35387bbb4a82f21c086e77e2aca24b5.zip?f=Ganyu05_JPG.zip', 'https://kemono.party/data/3f/94/3f949f6a72fdbb5139f564ababc3762af6d3b315810476b35ddbfd670fabc6b9.mp4?f=Ganyu05_B1.mp4', 'https://kemono.party/data/c1/aa/c1aa605d7a9b51c17b0e3010a5d26283f3a44be3e80d27526706a5cc7613f029.mp4?f=Ganyu05_A1.mp4', 'https://kemono.party/data/a4/aa/a4aadfd7f8924af68c1d5b5869baa730e229581476b31573021070a3df27bfe7.mp4?f=Ganyu05_A2.mp4', 'https://kemono.party/data/2f/80/2f80decf853c45e0634b29204f846f58d061fc79e88fefbe873dedc1b647864e.mp4?f=Ganyu05_B2.mp4', 'https://kemono.party/data/7e/75/7e75ae059c3cdcfcc9beb6cab0a15d0ab951a33098b3c303fc6cfdf22931b076.mp4?f=Ganyu05_C1.mp4', 'https://kemono.party/data/ea/bd/eabdbe911ff5006967afb553a33b6fcf015bab0b2136698eba37a5904f58d63c.mp4?f=Ganyu05_ex.mp4', 'https://kemono.party/data/d9/93/d993518518739d4fcfdf74f0bc32883e3d937bf0358277e80d328197090314c2.txt?f=txt5.txt', 'https://kemono.party/data/b3/ca/b3caf54e008c868cb42e623a7e4cef6e50201d9c9088fce0e5c043c9fcbc244f.zip?f=Ganyu05_JPG.zip', 'https://kemono.party/data/4d/df/4ddf29d41245c46000468ebf9ab752a7d6ea800eceeeb09bba982868108f3dbb.mp4?f=Ganyu05_A1.mp4', 'https://kemono.party/data/1f/8a/1f8a7a46e4a1f71dbbb101cb7f1e187ab06c235a4fa5d66f6f86240f92651831.mp4?f=Ganyu05_A2.mp4', 'https://kemono.party/data/59/4e/594eefed9612ea1c7b9c038295d2a65310a83fb290e78dbc52c51cc8ab80fe90.mp4?f=Ganyu05_B1.mp4', 'https://kemono.party/data/60/36/603686b68e53dea268c02408a11847dd4ae1d10fd77e24ec2b24ed4878c39870.mp4?f=Ganyu05_B2.mp4', 'https://kemono.party/data/b1/0b/b10b10e144dfecd434d350446ee2559714fad26bf60ed5ed2dc249b6845c71a1.mp4?f=Ganyu05_C1.mp4', 'https://kemono.party/data/41/1f/411fcfd5e5a7f79bc79b6fb0fec95c79ae445491f2430278d372b4c353538d95.mp4?f=Ganyu05_ex.mp4', 'https://kemono.party/data/ec/9c/ec9c9f4e52c1de76f25eb4edc047e112d0dc22f3f999b2cc2225430bccc31f80.zip?f=Ganyu04.zip', 'https://kemono.party/data/3d/5b/3d5b4ca43cf25920e7f0595a28127043657cc3eaa5434edcbb445622f841cac2.zip?f=Ganyu04_ss.zip', 'https://kemono.party/data/71/1c/711c4e0c96747f2c5ee11ed109d43a18ce81ad9d6b5445a816b9d16e81b09c2a.zip?f=EulaX.zip', 'https://kemono.party/data/77/3e/773e0380f5f07fb9b8d6ee2a9b66b80c923b0045f7f7dbad08d060070d319dc5.zip?f=EulaX_JPG.zip', 'https://kemono.party/data/e9/d3/e9d32145e5ef36be9fc935d608bff42d04d9f5c9d8fa7e79ab1e771fdab44cd5.zip?f=Ganyu03.zip', 'https://kemono.party/data/4f/d9/4fd92c3d139aba0062c2743339d4c7890eb04ab52cc5afc6651b2c551bd6a31c.zip?f=Ganyu03_jpg.zip', 'https://kemono.party/data/80/0b/800b2a2400c67c3570ea46f5f355df0e6c308b4fee30d40d75d72b3185974bd4.zip?f=Ganyu02e.zip', 'https://kemono.party/data/ea/c5/eac5270dfe362f2f5def2823e4b385f632d5e5f053d6c07a4a3b5a1a8c71337f.zip?f=Ganyu02cd.zip', 'https://kemono.party/data/a7/4a/a74adf4a5fd0f8c43dc1a594308a86616b2d5c1bd82fca59aa325b6036c9ba01.zip?f=Ganyu02ab.zip', 'https://kemono.party/data/38/f2/38f21753d6b5c3ccd539d634243005791bf75ffee4895a16dc2372bfb64a6b9a.zip?f=Ganyu02_JPG.zip', 'https://kemono.party/data/83/cb/83cb83301b6666fd0dd8b75bb0b4bf43504046cb301572ec955aa4321be11b05.zip?f=Ganyu01.zip', 'https://kemono.party/data/c1/a4/c1a4af8c191519b97dc620cfee77f89add6b63ee1350d5e9754a6a338d348c3b.zip?f=Hutao03c.zip', 'https://kemono.party/data/99/11/991121c45c08769b59ad5a9d88e78866db021e5637f0077920b6be2ba6920f35.zip?f=Hutao03b.zip', 'https://kemono.party/data/6a/b7/6ab7bf0ee428291ac0ced5abc778b79298a03d0751e3c3c5d7328b8cb54134d6.zip?f=Hutao03a.zip', 'https://kemono.party/data/75/bf/75bfcbe841d0443d763e4d7ca7725ae1442123d0d3229e716f6df9c117a31e0c.zip?f=Hutao03_JPG.zip', 'https://kemono.party/data/06/d4/06d463866adb0ed123af5283482481ab68183403698e2ab890c45c1db9e22cf3.zip?f=Hutao02.zip', 'https://kemono.party/data/e2/ce/e2ce5b82961da3105507507a4dc7929474d1aa6557e59c42f76f10d409423d6e.zip?f=Hutao02_jpg.zip', 'https://kemono.party/data/bf/6b/bf6bb41f2849336b3e8451e0b2b0276f7550a356b9bd237bfbeac1c6f4b98290.zip?f=Hutao01.zip', 'https://kemono.party/data/ca/4f/ca4f9c6e80442ea0ef6636e8d0987a81c95b94d224d7c966cd0cdbe3593b4db6.zip?f=Raiden_07.zip', 'https://kemono.party/data/8b/0a/8b0a658059cfc3769ad887e05947300031576314a6bf515f0eb5571e8add2729.zip?f=Raiden_07_jpg.zip', 'https://kemono.party/data/4e/1d/4e1d477b664a6233735d789dbbab9a0046cd2a0151c860b6b5c73412238d898d.zip?f=FGO5_unc.zip', 'https://kemono.party/data/ee/dc/eedc37a741cd26d076c21381c7d2f8334e48513956d8c8d403a0b1ea693ae8eb.zip?f=Raiden_06_abc.zip', 'https://kemono.party/data/5e/ca/5ecabde7fa35bef7bab1960581506a45c0812c6bfc7991ba60bdf1064bd1be4e.zip?f=Raiden_06_def.zip', 'https://kemono.party/data/20/95/2095c2eaf208a05d87ec12ff0fdd9ef6f2dbd410d4cb0536653bb9f2cefb0835.zip?f=Raiden_06.zip', 'https://kemono.party/data/da/09/da094cf944c0c71521b3ea46381d8f63a2cb1f6f2fddac39e8dd4cf8827c48c9.zip?f=chn.zip', 'https://kemono.party/data/a0/42/a0426d7440c1bbf52bb848bf1ad197a15fd714150a37797017af311e3599f8d1.zip?f=Raiden_05_Hr.zip', 'https://kemono.party/data/83/a9/83a9d16d279ca0fb88ea34bd4f44562a3a288d5fac0a961730800be3d4b0d205.zip?f=Raiden_05_jpg.zip', 'https://kemono.party/data/fe/92/fe92fb1b1b395f84ada599433584e0d80146b5043cdf88c2d77936303b0b0811.zip?f=Raiden_04_PNGTXT.zip', 'https://kemono.party/data/1e/ee/1eeec804a54dedb29927eba277c5d39f811659946de202d5b59632eb7d8bbbdf.zip?f=Raiden_03_PNGTXT.zip', 'https://kemono.party/data/a4/72/a47274c2ff0bb1e625805efd3a5900925c0a19367d6777144cfbe95d0fdafa90.zip?f=Raiden_03_JPG.zip', 'https://kemono.party/data/f6/bf/f6bfef3c6234ff70ead04770bde35c9c4add79ca8f2dd5921044f25fe204ab8a.zip?f=FGO4A_unc.zip', 'https://kemono.party/data/6b/89/6b890839e452f0c5789ae8b7ebaf62e80703bb5816d594a11a38f861821a7765.zip?f=Raiden_02v2_pngtxt.zip', 'https://kemono.party/data/f0/bb/f0bb663fdf089fa62d53b932b1055bcb2511fde39a7b290f61f8cd989e91786b.zip?f=Raiden_02v2_JPG.zip', 'https://kemono.party/data/cd/3a/cd3a6f8770e45c15b1482e234dad17f4b829f24c5c5f6459835ccbb4a73d37ab.zip?f=Raiden_01_pngtxt.zip', 'https://kemono.party/data/86/00/8600294a86b26c0b669e588b80f66e04a66f455efa1671f04070c6ff1d73e31f.zip?f=Raiden_01_JPG.zip', 'https://kemono.party/data/3f/79/3f793e1ded9f9d974e73347b6157ac3dca4e7fece0774adaa3bad6c55b3a86c5.mp4?f=eula_l2d_02_Patreon_hd.mp4', 'https://kemono.party/data/1a/46/1a465bbb5ed6c1ba07c812263fb99d42c60b2b19c261140ae0082714e329c08b.mp4?f=eula_l2d_01_Patreon_hd.mp4', 'https://kemono.party/data/0e/cf/0ecf419c222c9016bda6709c7f5fee6b43e4c658a37fe1200ceb680d3dec6b8a.mp4?f=eula_l2d_01_patreon_FHD.mp4', 'https://kemono.party/data/e9/f9/e9f9f1b0740985ccda34188385b0762e35e5ad12ec10bf8a2a7f13e0316d512b.mp4?f=eula_l2d_02_patreon_FHD.mp4', 'https://kemono.party/data/42/8d/428d8c590d29d619c6a6b942c6fc8a31826e9bf8b452f4979b90850baa76e143.zip?f=FGO4L_unc.zip', 'https://kemono.party/data/30/b1/30b17d3b1f123e6eb6d60f74971397de0490915e64158981f8debb7f23d9d190.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt%20%282%29def.zip', 'https://kemono.party/data/7a/df/7adf89590fac67806b61b08feed73366c60b3a47e7f6d0d961ef85d6c0f44de4.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt%20%282%29ghi.zip', 'https://kemono.party/data/17/03/1703a16724adef3ae78ec05394f16bc1c6c1a505ad106593e0243f47c3d6cfa6.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt%20%282%29abc.zip', 'https://kemono.party/data/c2/e2/c2e265341cd9563747837ad3a3c2deaa9b4421033c8bb406ba47e9ddd2b4c91d.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt.z01', 'https://kemono.party/data/cb/cb/cbcbc849e696af64e4e23bcd119aff42ce152ab4ad9096c66c73d0f4758622b2.bin?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt.z02', 'https://kemono.party/data/1f/c9/1fc928eb5185cc9e4a401ce8405fb17b5a6208e324bfaf7cdbb088d3a24a1860.bin?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt.z03', 'https://kemono.party/data/54/91/5491ef9a3918624b963a9acdf1f4d7119d027b54884e775caa6523f23a98bd39.bin?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_pngtxt.zip', 'https://kemono.party/data/01/75/01759610e8627333536d080e7ed350a39b629312cf354ee1a6fa914e39514242.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A27_jpg.zip', 'https://kemono.party/data/57/d2/57d23eef0909abfbba659350b28f9457aa7b05f3e87a2adc3b32058c0bc40455.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A26_pngtxt.zip', 'https://kemono.party/data/c7/b6/c7b6c1c61a9004a905852975edeffbbc15abc0cfe364d61560bcb9c0d6d4d707.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A26_jpg.zip', 'https://kemono.party/data/57/36/5736ca900d0e37b01057f7f476cb082620809afe192c4158caed228a012a6b1d.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A25_pngtxt.zip', 'https://kemono.party/data/9e/34/9e349e2ff77feb68e6039836cd88aac7450045cdf4e30df693fd473b7797a92b.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A25_jpg.zip', 'https://kemono.party/data/88/6d/886d444b198e39b5e91830f2efb24914811f4ce6237616e2d15ce704108fb546.zip?f=FGO3A_unc.zip', 'https://kemono.party/data/39/9b/399b5a21fe250c8f876ef56f29568bc7618671ecd1910c9e4bd0dde9220dd498.txt?f=txt.txt', 'https://kemono.party/data/a9/c6/a9c602c54ec0d431b912674d3395c8d6ad69f3e0ae069249ea30ad41fb88d810.txt?f=txt.txt', 'https://kemono.party/data/3c/df/3cdfb391bf8f7c6d58fe01b4fe9883f0ef99d6f7094f76cb183ab0834afe9d21.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A24_pngtxt2.zip', 'https://kemono.party/data/bd/f4/bdf40ff6fb76cf60f3f751fd961eefe34b48369d176af1a6d32987841000378a.zip?f=%E3%82%A8%E3%82%A6%E3%83%AB%E3%82%A24_jpg.zip', 'https://kemono.party/data/ab/f2/abf26f340083e6419577aa479c209da57c8585c87120ce41336d0f604544d7cf.zip?f=miko2.zip', 'https://kemono.party/data/2e/a9/2ea9f30cf661dc969b2c67d5f5683a6e9b8ecfcac1b51d59e7557dcc3909bd1b.zip?f=miko1.zip', 'https://kemono.party/data/b8/bd/b8bdca42bdde396112bb6bf109881a7971b4ed7046d2e8d2e6d5816293461f43.zip?f=FGO3L_unc.zip', 'https://kemono.party/data/54/0b/540bad59c7def7cb1367b30465871857e495853b6ee887be449f2ae25930c624.zip?f=pt_EU_05C.zip', 'https://kemono.party/data/e1/f4/e1f42389c76464b289df6aefdc11b1c5f56edd26349c937afdce9b86f3690abf.zip?f=FGO2_unc.zip', 'https://kemono.party/data/5b/e9/5be972a9fd62af9acba85f932a322118f7cf671dea8fe581ae88111b80ab3d75.zip?f=sui02.zip', 'https://kemono.party/data/48/1a/481a0a0d62c40332e119baf5c74149ac9a919fcfe99530213dd5ba55d6e83c5e.zip?f=sui01.zip', 'https://kemono.party/data/ad/2a/ad2a116d25a44b06e3855ab9aca3847446101035e2c462f775a5d058756d0390.mp4?f=Jxh_01.mp4', 'https://kemono.party/data/a6/48/a6482cf926508fbe77578d295537224a97790476fb10c7c19c0f712538015c41.mp4?f=Jxh_02.mp4', 'https://kemono.party/data/e7/16/e71654c75953a4abd0203b25b2fc29fa6e726eb882e308cbdb0b4bfe4e9f3a6e.mp4?f=Jxh_03.mp4', 'https://kemono.party/data/c0/1c/c01c9659e519c65b567ff5f092ad6c014c082c25935cee903766d16d5708fe70.zip?f=FGO1_unc.zip', 'https://kemono.party/data/4c/09/4c0920edafb1469fd6da43658a1b723762cb315075d7f9e016d7d5791511527e.mp4?f=g1.mp4', 'https://kemono.party/data/55/20/5520a7e7fc5a0be7357c058604245d6c4e8ffeef24e69049bc4717be36e883f4.mp4?f=g1b_fin.mp4', 'https://kemono.party/data/1d/67/1d67a9f04bbf89b211ab64d18c638979d113d26e8f54995978316430bb4322bf.mp4?f=g2.mp4', 'https://kemono.party/data/ac/70/ac707a451514503dfa64a160f3af79878b1027a815beb4b8687ea870f7977b16.mp4?f=g1b_fin_b.mp4', 'https://kemono.party/data/56/16/5616591d5922276f91ec3824780cec7af8a3828a7d7c928395706cc0a49d579f.zip?f=cv_h.zip', 'https://kemono.party/data/71/2d/712db9042ec89ecc12f1d579cbe7686ecc41f2e012da6c8b851601293495ceba.zip?f=GBF4_unc.zip', 'https://kemono.party/data/68/c6/68c667a4bfc144b8f9a3e2073de6cb9d7a64d242aa9ba4477a97736aa4dfedfd.zip?f=GBF3_unc_v2.zip', 'https://kemono.party/data/39/89/3989ff134cbe64fd40ebef6625977d6f6291fa31985d3cbc48fea0831de4f4c5.mp4?f=08_after_cam.mp4', 'https://kemono.party/data/e5/92/e5921072fd97d62518e53e9153a31340efbb2cee9720ac2556c54cff43b12add.zip?f=Ganyu_hr.zip', 'https://kemono.party/data/7c/01/7c016ebbdaf32062b594786b0d0b25606ac749544af3d52b7daa55c7ef6c6461.mp4?f=01_a_1.mp4', 'https://kemono.party/data/67/19/671965f7dc3c8ee71bc6da796fd71cdaf6b539f328c54e0f88c539324d425358.mp4?f=01_b_1.mp4', 'https://kemono.party/data/69/52/6952733a605e0133ebdc8f1e8d31bd6aaad645fc9ad70d6b34c5bdf59e105f7a.mp4?f=01_c_1.mp4', 'https://kemono.party/data/06/43/0643d5ff892f93a57e314ef007598f4cbee0cf8b2d98a7cb7b24700bcc8b6521.zip?f=Amber_hr.zip', 'https://kemono.party/data/7b/8b/7b8b41700421cde7d809af0db760eeb537ef27b7df4a85fe0cff04459cac060d.mp4?f=sn206.mp4', 'https://kemono.party/data/f3/90/f3903cac471c7bcb1b327dea3131556ec76d9eb903eb35b78d300aa449a58696.mp4?f=sn203.mp4']
    # print(lllink1)
    downloadLink = []

    for i in range(len(lllink1)):

        # print(i)
        print("lllink1:", lllink1[i])
        # for l1 in range(len(lllink1[i])):

        response1 = SendRequests(10000, lllink1[i][1], download.Headers)
        # response = requests.get(lllink1[i][1], headers=download.Headers)
        html = response1
        # print(html)
        bs = BeautifulSoup(html, "lxml")
        title = bs.select('h1 > span')[0].text
        # time = bs.select('.post__published > time')[0].text
        # time = str(time)
        # time = time.strip().lstrip()
        # title = "\\teamboobs\Makima | Tier 1 | ~2022/1/25\\4622..zip"
        # title1 = "默认"
        title.strip().lstrip()
        news_title = titlecheck(title)
        # time = titlecheck(time)
        # for str1 in title.split():
        #     print(str1)
        #     # if title[str1] == "?" or str1 == "/" or str1 == "\\" or str1 == "*" or str1 == ":" or str1 == '"' or str1 == "<" or str1 == ">" or str1 == "|":
        #     #     title1 = "命名错误默认命名"
        #
        #     #     break
        print(news_title)
        # print(time)
        # dataname = bs.find("a", {"class": ""})
        try:

            count3 = 0
            path333 = f"F:/色色区/画集（新新新）/{lllink1[i][0]}/{news_title}/text"
            path333 = str(path333).replace(" ", "").replace("\n", "").strip().lstrip()
            if not os.path.exists(path333):
                os.makedirs(path333)
            # 必须先文字，再图片，后链接，因为try：catch在发生异常时不会继续执行而是跳过然后执行下一个，所以让有异常的循环直接在最后即可
            for l1 in bs.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['post__content']):
                # for j in bs.find_all(lambda tag: tag.name == 'div'):
                # print("l", l1)
                print(path333)

                txt1 = l1.text
                print(txt1)
                print(i)
                text = open(f"{path333}/{count3}.txt", "w+", encoding="utf-8")
                text.write(txt1)
                text.write("\n")
                text.close()
                count3 += 1
        except Exception as aaa:
            print(aaa)

        try:
            artist_name = bs.find(attrs={'class': 'post__attachment-link'}).text
            artist_name = titlecheck(artist_name)
            link = bs.find_all("a", {"class": "post__attachment-link"})[0].get("href")
            # data = re.findall('(?<=href=").*?(?=\")', str(j))

            # print(time)

            # path = f"F:\\色色区\\画集（新新新）\\{lllink1[i][0]}\\{artist_name}"
            count1 = 0
            path111 = f"F:\\色色区\\画集（新新新）\\{lllink1[i][0]}\\{news_title}\\img"
            path111 = str(path111).replace(" ", "").replace("\n", "").strip().lstrip()
            if not os.path.exists(path111):
                os.makedirs(path111)
            imglink = []
            for k in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['fileThumb']):
                data1 = re.findall('(?<=href=").*?(?=\")', str(k))
                imglink.append(data1)
                for ji in range(len(imglink)):
                    link = "https://kemono.party" + "".join(map(str, imglink[ji]))
                    path7 = f"{str(link)[len(link) - 4]}"
                    path8 = f"{str(link)[len(link) - 3]}"
                    path9 = f"{str(link)[len(link) - 2]}"
                    path10 = f"{str(link)[len(link) - 1]}"
                    path16 = path7 + path8 + path9 + path10
                    print("path16", path16)
                    path16 = f"{count1}.{path16}"
                    IDMDownload(path111, link, path16)
                    count1 += 1
        except Exception as aaaa:
            print(aaaa)

        try:
            count = 0
            path = f"F:\\色色区\\画集（新新新）\\{lllink1[i][0]}\\{news_title}"
            path = str(path).replace(" ", "").replace("\n", "").strip().lstrip()
            if not os.path.exists(path):
                os.makedirs(path)
            datalink= []
            for j in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['post__attachment-link']):
                print(j)
                data = re.findall('(?<=href=").*?(?=\")', str(j))
                datalink.append(data)
                for ij in range(len(datalink)):
                    print(ij)
                    link = "https://kemono.party" + "".join(map(str, datalink[ij]))
                    print(link)
                    path1 = f"{str(link)[len(link) - 4]}"
                    path2 = f"{str(link)[len(link) - 3]}"
                    path3 = f"{str(link)[len(link) - 2]}"
                    path4 = f"{str(link)[len(link) - 1]}"
                    path6 = path1 + path2 + path3 + path4
                    print("path6", path6)
                    path6 = f"{count}.{path6}"
                    downloadLink.append("https://kemono.party" + "".join(map(str, data)))
                    IDMDownload(path, link, path6)
                    count += 1
                print("data:", data)

        except Exception as aaaaaa:
            print(aaaaaa)
            # path2 = f"{str(lllink[l1])[len(lllink[l1]) - 3]}"
            # path3 = f"{str(lllink[l1])[len(lllink[l1]) - 2]}"
            # path4 = f"{str(lllink[l1])[len(lllink[l1]) - 1]}"
            # IDMDownload()
            # for j in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['post__attachment-link']):
            #     # print(j)
            #
            #     # print("data:", data)
            #     # downloadLink.append("https://kemono.party" + "".join(map(str, data)))
            # file_name = bs.find_all("a", {"class": "post__attachment-link"}).get_text
            # print(artist_name.strip().lstrip())
            # link = "https://kemono.party" + "".join(map(str, link))
            # print("link", link)
            # print(file_name)


        # for j in bs.find_all(lambda tag: tag.name == 'a' and tag.get('class') == ['post__attachment-link']):
        #     # print(j)
        #     data = re.findall('(?<=href=").*?(?=\")', str(j))
        #     print("data:", data)
        #     downloadLink.append("https://kemono.party" + "".join(map(str, data)))
        # print(downloadLink)
        # path1 = f"{count}.{str1}"
        # IDMDownload(path, lllink1[l1], path1)
        # count += 1

    # count = 0


if __name__ == "__main__":
    SQL_Select()
    downloadLink(SQL_Select())
