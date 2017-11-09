#coding:utf-8

from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import Request
from daomubiji.items import DaomubijiItem
import time



# http://www.daomubiji.com/

class daomubiji(BaseSpider):
	name = "daomubiji"
	allowed_domains = ['daomubiji.com']
	start_urls = ['http://www.daomubiji.com/']

	def parse(self, response):
		with open('daomu.html','wb') as f:
			f.write(response.body)
		hxp = Selector(response)
		# /html/body/section/article/a[1]
		first_urls = hxp.select("//article[@class='article-content']/p/a/@href").extract()
		for url in first_urls:
			print url
			yield Request(first_urls[0], callback=self.parse_item)

	def parse_item(self, response):
		with open('first.html','wb') as f:
			f.write(response.body)

		hxp = Selector(response)
		urls = hxp.select("//div[@class='excerpts-wrapper']/div[@class='excerpts']/article/a/@href").extract()
		titles = hxp.select("//div[@class='excerpts-wrapper']/div[@class='excerpts']/article/a/text()").extract()
		item = DaomubijiItem()
		print '=========================='
		for url in titles:
			print url.split(' ')[1]
		for i in range(len(urls)):
			print 'i ===汉字是多少'+ str(i)
			arr = titles[i].split(' ')
			item['url'] = urls[0]
			item['chapter'] = arr[0]
			item['chapter_num'] = arr[1]
			item['section'] = arr[2]
			item['name'] = '盗墓笔记'
			# time.sleep(1)
			yield item

		print '=========================='

		

