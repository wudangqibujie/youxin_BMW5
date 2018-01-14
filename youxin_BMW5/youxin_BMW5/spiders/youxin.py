import scrapy
from youxin_BMW5.items import YouxinBmw5Item

class YouxinBMWSpider(scrapy.Spider):
    name = "BMW"
    start_urls = ["https://www.xin.com/quanguo/baoma/baoma5xi/i{page}/"]

    def start_requests(self):
        for i in range(1,2):
            yield scrapy.Request(url=self.url.format(page =i),callback=self.parse_one)

    def parse_one(self,response):
        item = YouxinBmw5Item()
        goods = response.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
        for one in goods:
            item['model'] = one.xpath('div[@class="across"]/div/h2/a/text()').extract()
            item['info'] = one.xpath('div[@class="across"]/div/span[1]/text()').extract()
            item['price'] = one.xpath('div[@class="across"]/div/p/em/text()').extract()
            yield item
        # print(one)