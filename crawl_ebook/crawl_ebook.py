from urllib import request
from bs4 import BeautifulSoup

import time
import random

article_url = 'http://www.kanunu8.com/book4/10204/'
content_url = int(226613)
while content_url < 226730:
    html = request.urlopen(article_url + str(content_url) + '.html')
    bsObj = BeautifulSoup(html, 'html.parser')
    title = bsObj.font.string
    comment = bsObj.p.get_text()
    with open('ebook.txt', 'a', encoding='utf-8') as file:
        file.write(title)
        file.write(comment)
    content_url += 1
    num = random.randint(5, 10)
    time.sleep(num)
