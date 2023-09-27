from selenium import webdriver
import re

driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")

f1 = open("F:/色色区/画集全/中午茶会_fanbox/txt/中午茶会_0_content.txt", "r", encoding="utf-8")
link = f1.read()
print(link)


# driver.get(link[i])

