import scrapy

from spider_demo.taobaoitems import TaobaoItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']

    def start_requests(self):
        keywords=['手机','电脑']
        for keyword in keywords:
            for page in range(2):
                url=f'https://s.taobao.com/search?commend=all&ie=utf8&initiative_id=tbindexz_20170306&page={page}&preLoadOrigin=https%3A%2F%2Fwww.taobao.com&q={keyword}&search_type=item&sourceId=tb.index&spm=a21bo.jianhua%2Fa.search_manual.0&ssid=s5-e&tab=all'
                yield scrapy.Request(url=url)

    def parse(self, response):
        selectors=response.css('#content_items_wrapper >div.tbpc-col')
        for selector in selectors:
            item=TaobaoItem()
            item['price']=selector.css('div.mainPicAndDesc--Q5PYrWux > div.priceWrapper--dBtPZ2K1.adaptMod--uU2wpGzc > div > div.innerPriceWrapper--aAJhHXD4 > div.priceInt--yqqZMJ5a::text').extract_first()
            print(f"\033[31m{item['price']}\033[0m")
            yield item