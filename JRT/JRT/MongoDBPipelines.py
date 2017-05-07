from pymongo import MongoClient

class MongoDBPipelines(object):
    collection_name = 'taobao'
    def open_spider(self,spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['python']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self,item,spider):
        self.db[self.collection_name].update({'picId':item['picId']}, {'$set': dict(item)}, True)
        return item


