import requests
from lxml import html
import tqdm, time, requests, json
from lxml import etree
from selenium import webdriver
# from fake_useragent import UserAgent
import random, time

## 初始化浏览器
chromeOptions = webdriver.ChromeOptions()
# userAgent = UserAgent()
# if len(self.proxies) != 0:
#     print("Use old IP to fetch new IPs...")
#     chromeOptions.add_argument(f"--proxy-server={self.proxies}")
# chromeOptions.add_argument(random.choice(userAgent.data["browsers"][random.choice(userAgent.data_randomize)]))
# chromeOptions.add_argument('--headless')  # use headless mode
driverSource = webdriver.Chrome(executable_path=r"C:\Users\XMK23\Downloads\chromedriver.exe",
                          chrome_options=chromeOptions)
driver = webdriver.Chrome(executable_path=r"C:\Users\XMK23\Downloads\chromedriver.exe",
                          chrome_options=chromeOptions)

driverSource.get("https://leetcode-cn.com/problemset/lcof")   #"https://leetcode-cn.com/problemset/lcof/#page-{}".format(pageNum))
time.sleep(2)


## 首先是按页码，一页一页来。
while True:
    try:
        rendered_body = driverSource.page_source
        page_source = etree.HTML(rendered_body)
        ## 获取一页上所有的url
        titles = page_source.xpath('//div[@class="question-title"]/a/text()')
        urls = page_source.xpath('//div[@class="question-title"]/a/@href')
        ## 逐个url进行处理。
        counter = 0
        for title, url in tqdm.tqdm(zip(titles, urls)):
            fullUrl = "https://leetcode-cn.com" +url
            driver.get(fullUrl)
            time.sleep(1)
            rendered_body = driver.page_source
            page_source = etree.HTML(rendered_body)
            texts = page_source.xpath('//div[@class="notranslate"]//text()')
            heheda = driver.find_element_by_xpath('//div[@class="notranslate"]')
            ## 打印信息到文件里。
            pyFileName = heheda.parent.title.split(".")[0].replace("剑指", "Jianzhi").replace(" ", "")
            with open(pyFileName + ".py", "w", encoding="utf-8") as f:
                f.write("'''\n[{}]({})\n\n{}'''\n".format(heheda.parent.title, fullUrl, "".join(texts)))
            # break

        button = driverSource.find_element_by_xpath('//a[@class="reactable-next-page"]')

        button.click()
        time.sleep(2)
    except:
        break


## 最后会崩掉，但是没事的。