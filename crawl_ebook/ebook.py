# -*- coding:utf-8 -*-
# version 1.2

from urllib import request
from bs4 import BeautifulSoup

import time
import random
import sys

article_url = 'http://dongyeguiwu.zuopinj.com/5512/'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
download_req = request.Request(url=article_url, headers=head)
download_response = request.urlopen(download_req)
bsObj = BeautifulSoup(download_response, "lxml")

title = bsObj.find(class_="infos").h1.get_text()
author = bsObj.find(class_="logo").a.get_text()

with open('ebook.txt', 'a', encoding='utf-8') as file:
    file.write(str(title).center(10)+"\n")
    file.write(str(author).center(25)+"\n\n")

book_list = bsObj.find(class_="book_list")
chapters_list = BeautifulSoup(str(book_list), "lxml")

total_chapters_nums = (len(chapters_list.ul.contents)-1)/2
current_chapters_nums = 1

for chapter in chapters_list.ul.children:
    if chapter != "\n":
        chapters_url = chapter.a.get("href")
        chapters_req = request.Request(url=chapters_url, headers=head)
        chapters_response = request.urlopen(chapters_req)
        soup = BeautifulSoup(chapters_response, "lxml")
        page_nums = soup.find(class_="h1title").get_text()
        comment_text = soup.find(id="htmlContent", class_="contentbox")
        comment = BeautifulSoup(str(comment_text), "lxml")

        with open('ebook.txt', 'a', encoding='utf-8') as file:
            file.write(str(page_nums).center(20))
            # 将\xa0,\u3000无法解码的字符删除
            parse_comment = comment.div.text.replace("\xa0", "\n").replace("\u3000","\n")
            file.write(parse_comment+"\n\n")

        sys.stdout.write("已下载:%.3f%%" % float(current_chapters_nums/total_chapters_nums) + '\r')
        sys.stdout.flush()

        current_chapters_nums += 1
        num = random.randint(5, 10)
        time.sleep(num)
print("下载完成")
