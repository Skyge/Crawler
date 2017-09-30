# -*- coding:UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup

import time
import random

article_url = 'http://www.kanunu8.com/book4/10204/'
content_url = int(226613)
while content_url < 226730:
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    url = article_url + str(content_url) + '.html'
    download_req = request.Request(url=url, headers=head)
    download_response = request.urlopen(download_req)
    bsObj = BeautifulSoup(download_response, 'html.parser')
    title = bsObj.font.string
    comment = bsObj.p.get_text()
    with open('ebook.txt', 'a', encoding='utf-8') as file:
        file.write(title)
        file.write(comment)
    content_url += 1
    num = random.randint(8, 13)
    time.sleep(num)
