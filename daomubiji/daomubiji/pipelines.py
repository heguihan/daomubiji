# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo

class DaomubijiPipeline(object):
	def __init__(self):
		# print '进入pipel'
		connection = pymongo.MongoClient('localhost', 27017)
		db = connection['novel']
		self.collection = db['daomubiji']
		self.i = 0
	def process_item(self, item, spider):

		self.collection.insert(dict(item))


		return item
