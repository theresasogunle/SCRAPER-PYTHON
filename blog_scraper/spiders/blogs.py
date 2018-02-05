from scrapy.spider import BaseSpider,Rule
from scrapy.selector import Selector
from ..items import BlogScraperItem
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
 
 
class MyBlogSpider(BaseSpider):
    name = 'mouse'
    start_urls = ['https://www.vanguardngr.com/2015/01/01/page/1/','https://www.vanguardngr.com/2015/01/01/page/2/','https://www.vanguardngr.com/2015/01/01/page/3/',
    'https://www.vanguardngr.com/2015/01/01/page/4/','https://www.vanguardngr.com/2015/01/01/page/5/','https://www.vanguardngr.com/2015/01/01/page/6/','https://www.vanguardngr.com/2015/01/01/page/7/'
    'https://www.vanguardngr.com/2015/01/01/page/8/'

    ]
    def parse(self, response):
        
        item = BlogScraperItem()
      
        titles = response.xpath('//div[2]/header/h2/a/text()').extract()
        contents = response.xpath('//div[2]/div/p/text()').extract()
        dates = response.xpath('//div[2]/header/div/span[1]/a/time/text()').extract()

        item['link']=response.url
        item['title']=titles
        item['content']= contents
        item['date']=dates

        return item


        



