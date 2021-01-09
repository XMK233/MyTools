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

with open("Jianzhi_Problem_All.txt", "w", encoding="utf-8") as f:
    ## 首先是按页码，一页一页来。
    while True:
        # try:
        rendered_body = driverSource.page_source
        page_source = etree.HTML(rendered_body)

        ## 获取一页上所有的url
        titles = page_source.xpath('//div[@class="question-title"]/a/text()')
        urls = page_source.xpath('//div[@class="question-title"]/a/@href')
        # print(len(urls))

        # page = requests.get("https://leetcode-cn.com/problemset/lcof/")
        # print(page.text)
        # tree = html.fromstring(page.content)
        # lists = tree.xpath('//div[@class="question-title"]/a/text()')
        ## 逐个url进行处理。
        counter = 0
        for title, url in tqdm.tqdm(zip(titles, urls)):
            fullUrl = "https://leetcode-cn.com" +url
            driver.get(fullUrl)
            time.sleep(2)
            rendered_body = driver.page_source
            page_source = etree.HTML(rendered_body)
            _ = page_source.xpath('//div[@class="notranslate"]//text()')
            texts = _
            # texts = []
            # io_flag = False
            # for text in _:
            #     ## 下列操作是为什么呢？为了给输入输出的行增加一个前导\t。
            #     if "输入：" in text or "输入:" in text:
            #         io_flag = True
            #     if "\n\n" in text:
            #         io_flag = False
            #     if io_flag:
            #         if text[0] == "\n":
            #             text = text[1:]
            #         text = "\t" + text
            #     texts.append(text)
            # print(texts)
            heheda = driver.find_element_by_xpath('//div[@class="notranslate"]')
            ## 打印信息到文件里。
            f.write("# [{}]({})\n\n{}\n\n".format(heheda.parent.title, fullUrl, "".join(texts)))

            # counter += 1
            # if counter >= 3:
            #     break

        button = driverSource.find_element_by_xpath('//a[@class="reactable-next-page"]')
        # if button == None:
        #     break
        button.click()
        time.sleep(2)
        # except:
        #     break

## 最后会崩掉，但是没事的。