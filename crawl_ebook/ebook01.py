# -*- coding:utf-8 -*-
# version 1.1

from urllib import request
from bs4 import BeautifulSoup

import time
import random
import sys

article_url = 'http://dongyeguiwu.zuopinj.com/5512/'
content_url = int(201501)
index = 0
while content_url < 201547:
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    url = article_url + str(content_url) + '.html'
    download_req = request.Request(url=url, headers=head)
    download_response = request.urlopen(download_req)
    bsObj = BeautifulSoup(download_response, 'lxml')
    page_nums = bsObj.find(class_="h1title").get_text()
    comment_text = bsObj.find(id="htmlContent",class_="contentbox")
    comment = BeautifulSoup(str(comment_text), 'lxml')

    with open('ebook.txt', 'a', encoding='utf-8') as file:
        file.write(page_nums)
        #将\xa0,\u3000无法解码的字符删除
        file.write(comment.div.text.replace("\xa0", "\n").replace("\u3000","\n"))
    
    sys.stdout.write("已下载:%.3f%%" % float(index/46) + '\r')
    sys.stdout.flush()

    content_url += 1
    index += 1
    num = random.randint(5, 10)
    time.sleep(num)
