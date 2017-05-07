# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JrtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    user_id=scrapy.Field()
    albumId=scrapy.Field()
    picHeight=scrapy.Field()
    picId=scrapy.Field()
    picUrl=scrapy.Field()
    picWidth=scrapy.Field()
    price=scrapy.Field()
    url=scrapy.Field()
    des=scrapy.Field()
    albumUserId=scrapy.Field()

