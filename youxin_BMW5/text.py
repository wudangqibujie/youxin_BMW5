import requests
from lxml import etree

url = "https://www.xin.com/quanguo/baoma/baoma5xi/i1/"
r = requests.get(url)
html = etree.HTML(r.text)
model = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li/div[@class="across"]/div/h2/a/text()')
year_age_loc = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li/div[@class="across"]/div/span[1]/text()')
price = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li/div[@class="across"]/div/p/em/text()')
print(len(price))
print(price)
price=list(price)
a=price[0]
print(type(a))
print(r.status_code)
