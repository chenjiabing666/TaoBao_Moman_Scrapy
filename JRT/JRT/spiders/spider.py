# -*- coding: utf-8 -*-
import scrapy
import re
from JRT.items import JrtItem
from bs4 import BeautifulSoup
import json

class SpiderSpider(scrapy.Spider):
    name = "spider"
    pattern_user_id=re.compile(r'user_id=(\d+)')
    pattern_ablum_id = re.compile(r'album_id=(\d+)')
    #allowed_domains = ["dou.com"]
    url='https://mm.taobao.com/json/request_top_list.htm?page={0}'
    url_ablum = 'https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20={0}&page={1}'  # 带有相册页面的url
    url_ablum_json='https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id={0}&album_id={1}&top_pic_id=0&page={2}&_ksTS=1493654931946_405'
    # start_urls = ['https://mm.taobao.com/json/request_top_list.htm?page=1']
    #start_urls = ['https://mm.taobao.com/self/album/open_album_list.htm?_charset=utf-8&user_id%20=687471686&page=1']

    def start_requests(self):
        for i in range(1,1000):
            yield scrapy.Request(self.url.format(i))


    ##解析user_id，根据user_id请求
    def parse(self, response):
        # print response.body
        print response.status
        ps=response.xpath('//p[@class="top"]')
        print "*****************************************"
        for p in ps:
            item=JrtItem()
            href=p.xpath('a/@href').extract()
            if href:
                item['user_id']=self.pattern_user_id.findall(href[0])[0]
                for i in range(1,6):
                    yield scrapy.Request(self.url_ablum.format(item['user_id'],i),meta={'item':item},callback=self.parse_ablum_id)

    ## 解析得到ablum_id，根据ablum_id解析请求出每一个相册的json数据
    def parse_ablum_id(self,response):
        if response.status==200:
            print response.url
            item = response.meta['item']
            # print item['user_id']
            soup = BeautifulSoup(response.text, 'lxml')
            divs = soup.find_all('div', class_='mm-photo-cell-middle')
            for div in divs:
                href = div.find('h4').find('a').get('href')
                items = self.pattern_ablum_id.findall(href)
                if items:
                    # print items[0]  # ablum_id  接下来就是请求相册了
                    for i in range(1,6):    #这里只请求6个相册
                        yield scrapy.Request(self.url_ablum_json.format(item['user_id'], items[0],i),meta={'item':item},
                                         callback=self.parse_ablum_json)


# https://mm.taobao.com/album/json/get_album_photo_list.htm?user_id=176817195&album_id=10651284&top_pic_id=0&cover=%2F%2Fimg.alicdn.com%2Fimgextra%2Fi4%2F17195022103384289%2FT1wCHrXXRvXXXXXXXX_!!176817195-0-tstar.jpg&page=4&_ksTS=1493654931946_405&callback=jsonp406

    def parse_ablum_json(self,response):
        if response.status==200:
            print '**********************************************************'
            print response.url
            try:
                results = json.loads(response.text)

                if results.get('picList'):
                    for result in results.get('picList'):
                        item = response.meta['item']
                        for field in item.fields:

                            if field in result.keys():
                                item[field] = result.get(field)
                        yield item
                        print '*******************************************************'
                else:
                    print "----------------------------------------------------------------------------------------------"

            except Exception:
                print '**********************EORR_******************************************************************************************'


















