import requests
from lxml import html
import tqdm, time, requests, json
from lxml import etree
from selenium import webdriver
# from fake_useragent import UserAgent
import random, time, re, os

alreadyDownloaded = [fn.replace(".py", "") for fn in os.listdir(os.getcwd()) if len(fn) == 8]

## 初始化浏览器
chromeOptions = webdriver.ChromeOptions()
# chromeOptions.add_argument('--headless')  # use headless mode
driverSource = webdriver.Chrome(executable_path=r"C:\Users\XMK23\Downloads\chromedriver.exe",
                          chrome_options=chromeOptions)
driver = webdriver.Chrome(executable_path=r"C:\Users\XMK23\Downloads\chromedriver.exe",
                          chrome_options=chromeOptions)

driverSource.get("https://leetcode-cn.com/problemset/lcci/")   #"https://leetcode-cn.com/problemset/lcof/#page-{}".format(pageNum))
time.sleep(2)

## 爬虫加载的时间
loadTime = 10
## 首先是按页码，一页一页来。
while True:
    # try:
    rendered_body = driverSource.page_source
    page_source = etree.HTML(rendered_body)
    ## 获取一页上所有的url
    titles = [s.split()[-1] for s in page_source.xpath('//td[@value="[object Object]"][2]/text()')]
    urls = page_source.xpath('//div[@class="question-title"]/a/@href')
    ## 逐个url进行处理。
    counter = 0
    for title, url in tqdm.tqdm(zip(titles, urls)):
        if title in alreadyDownloaded:
            continue
        fullUrl = "https://leetcode-cn.com" +url
        driver.get(fullUrl)
        time.sleep(10)
        rendered_body = driver.page_source
        page_source = etree.HTML(rendered_body)
        texts = page_source.xpath('//div[@class="notranslate"]//text()')
        heheda = driver.find_element_by_xpath("//div[@class='notranslate']")
        ## 要等一下ho, 等他加载ho.
        ## 如果有加载失败的, 可以再调高这个等待的时间.
        time.sleep(10)
        ## 打印信息到文件里。
        try:
            pyFileName = re.findall("\d+.\d+", heheda.parent.title)[0] # heheda.parent.title.split(" ")[1][:-1].replace(".", "-")
            with open(pyFileName + ".py", "w", encoding="utf-8") as f:
                f.write("'''\n[{}]({})\n\n{}'''\n".format(heheda.parent.title, fullUrl, "".join(texts)))
        except:
            try:
                pyFileName = re.findall("\d+.\d+", driver.title)[0]
                with open(pyFileName + ".py", "w", encoding="utf-8") as f:
                    f.write("'''\n[{}]({})\n\n{}'''\n".format(driver.title, fullUrl, "".join(texts)))
            except:
                print(fullUrl)
        # break

    button = driverSource.find_element_by_xpath('//a[@class="reactable-next-page"]')

    button.click()
    time.sleep(2)
    # except:
    #     break


## 最后会崩掉，但是没事的。