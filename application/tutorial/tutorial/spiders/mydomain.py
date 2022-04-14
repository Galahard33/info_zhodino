from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import PosterscheduleItem
from scrapy.crawler import CrawlerProcess


class ScheduleSpider(CrawlSpider):
    name = 'schedule'

    start_urls = ['http://kinoteatr.magegam.by/index.php?cPath=323766']
    allowed_domains = ['kinoteatr.magegam.by']
    rules = (Rule(LinkExtractor(allow=('newsdesk_id=',), deny=(
        '/howto_pay', '/howto_rules', '/contact_us', '/auth/', '/create_account', '/#box-region', '/vyixodnoj',
        '/?VIEW=TABLE',
        '/?VIEW=',)), callback='parse', follow=True),)

    def parse(self, response):
        text = response.xpath('//td[@class="tableBoxArea1Contents"]/strong/a/text').get()
        url = response.url
        quoleItem = PosterscheduleItem(text=text, url=url)
        yield quoleItem
