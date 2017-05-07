# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class JrtPipeline(object):
#     def process_item(self, item, spider):
#         return item


# import urllib
# import re
# import requests
# import json
# from bs4 import BeautifulSoup
#
# #url='https://www.zhihu.com/api/v4/members/excited-vczh/followees'
# url='https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=176817195&album_id=10651284&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi4%2F17195022103384289%2FT1wCHrXXRvXXXXXXXX_!!176817195-0-tstar.jpg&page=4&_ksTS=1493654931946_405'
# url_ablum='https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20={0}&page={1}'   #带有相册页面的url
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'}
# user_id=[]
# pattern=re.compile(r'album_id=(\d+)')
#
# res=requests.get(url,headers=headers)
# results=json.loads(res.text)
# for result in results.get('picList'):
#     print result.get('userId')
#
# # res=requests.get(url,headers=headers)
# # results=json.loads(res.text)
# # for result in results.get('data').get('searchDOList'):
# #     user_id.append(result.get('userId'))
# #
# # for i in user_id:
# #     rq=requests.get(url_ablum.format(i,1),headers=headers)
# #     soup=BeautifulSoup(rq.text,'lxml')
# #     ablum_id=[]
# #     divs=soup.find_all('div',class_='mm-photo-cell-middle')
# #     for div in divs:
# #         href=div.find('h4').find('a').get('href')
# #         items=pattern.findall(href)
# #         if items:
# #             print items[0]
#
#
# # url='//mm.taobao.com/self/album_photo.htm?user_id=176817195&album_id=10000962815&album_flag=0'
# # pattern=re.compile('album_id=(\d+)')
# #
# # items=pattern.findall(url)
# # if items:
# #     for item in items:
# #         print item
#

import urllib
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db =client['python']['taobao']
cursor=db.find({},{'_id':0,'user_id':1}).limit(2)
print cursor.next().get('user_id')





