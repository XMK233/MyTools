# -*- coding:utf-8 -*-
from selenium import webdriver
from lxml import etree

## 要修改的参数
playListURL = "https://www.youtube.com/playlist?list=PLIx8QniXH-rEkJPV4dH-KobXtEp0EIS7r"
xPath_VideoURLs = "//a[@id='video-title']/@href"
# xPath_VideoTitles = "//a[@id='video-title']/@title"
chromeDriverPath = "C:\\Users\\XMK23\\Downloads\\chromedriver.exe"

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chromeDriverPath,
                                  chrome_options=chromeOptions)
driver.get(playListURL)
rendered_body = driver.page_source
page_source = etree.HTML(rendered_body)
links = page_source.xpath(xPath_VideoURLs)
# titles = page_source.xpath(xPath_VideoTitles)
# print(links)
with open("download.bat", "w", encoding="utf-8") as f:
    f.write("call activate py1\n")
    for link in links:
        # print(title)
        f.write("you-get https://www.youtube.com{}\n".format(link))
    f.write("pause\n")
