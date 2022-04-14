import re

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ..items import PosterscheduleItem
from scrapy.crawler import CrawlerProcess


class ScheduleSpider(CrawlSpider):
    name = 'test'

    start_urls = ['http://kinoteatr.megamag.by/index.php?cPath=323766']
    allowed_domains = ['kinoteatr.megamag.by']
    rules = (Rule(LinkExtractor(allow=('newsdesk_id=',), deny=(
        '/howto_pay', '/howto_rules', '/contact_us', '/auth/', '/create_account', '/#box-region', '/vyixodnoj',
        '/?VIEW=TABLE',
        '/?VIEW=',)), callback='parse', follow=True),)

    def parse(self, response):
        if len(response.url) <=62:
            text = response.xpath('//table[@class="Cinema_new_box_2_TemplateCenterPart"]/tr/td/table[@class="Cinema_new_box_2_Contents"]').getall()
            url = response.xpath('//td[@class="tableBoxArea1Contents"]/strong/a/text()').get()
            text_final = re.sub(r'<tr>|</tr>|\\n|\\t|<td>|</td>|</table>|</a>|cellspacing="0"|width="100%"|height="1"|cellpadding="2"|border="0"|cellpadding="0"|cellpadding="3"|<strong>|</strong>|<td width="45"|</p>|</div>', '', str(text))
            text_final1 = re.sub(r'<table     class="Cinema_new_box_2_Contents">        <img src="images/pixel_trans.gif"  alt=""  >|           <td class="Cinema_new_box_2_BoxText">|<div id="sh_cart"><!-- shopping_cart --><table cellpadding="1"   ><td align="left" class="main">Корзина пуста<!-- shopping_cart eof -->           <img src="images/pixel_trans.gif"  alt=""  >|<table     class="Cinema_new_box_2_Contents">        <img src="images/pixel_trans.gif"  alt=""  >           <td align="center" class="Cinema_new_box_2_BoxText"><table cellpadding="1"   ><td align="left" class="main">           <img src="images/pixel_trans.gif"  alt=""  >    |<table     class="Cinema_new_box_2_Contents"><td class="main"><table    align="right"  style="border-collapse: collapse"><table    ><table    ><td  class="main" valign="top"><table     height="33"><tr class="tableBoxArea1Row"><td class="tableBoxArea1Contents">Анонсы / |<td valign="top"><table    ><td class="main"><td class="main" colspan="3" style="padding:4px 4px 4px 15px; background:#222222; color: #ffff00;">Кинозал<td class="main" width="195" style="padding:4px 4px 4px 15px; background:#444444; color: #ffffff;">', '', text_final)
            text_final2 = re.sub(r'<a href="http://kinoteatr.megamag.by/newsdesk_info.php\?newsdesk_id=\d\d\d\d|class="tableBoxArea2Contents" align="right"><img src="templates/Cinema-new/images/show.png"  alt="">', '', text_final1)
            text_final3 = re.sub(r'\d\d\d\d class="tableBoxArea2Contents" align="right"><img src="images/icons/comments\.png"  alt="">#comments">\d<table    ><td  class="main" valign="top"><table    ><td  class="main" valign="top"><table    ><td class="main"><div style="display: table-row">', '', text_final2)
            text_final4 = re.sub(r'<p>|<br>', '\n', text_final3)
            text_final5 = re.sub(r'<div style="position:relative;"><a href="http://dl.megamag.by/files/\w*\.\d*\.\w*" class="dl_video"><img src="images/icons/icon_video_play\.gif"  alt="Кликните по иконке\(ам\) для просмотра видеофайлов:" title=" Кликните по иконке\(ам\) для просмотра видеофайлов: "><div style="position:absolute;top:5px;left:25px;">|<a href="http://dl\.megamag\.by/files/\w*\.\w*\.\w*"|<div style="display: table-row">Кликните по иконке\(ам\) для просмотра видеофайлов:', '', text_final4)
            text_final6 = re.sub(r' class="dl_video">|<table cellpadding="4"   ><tr style="background:#666666;"><td class="main" style="padding:25px;" align="center">Для того, чтобы оставить отзыв нужно пройти &amp;action=relogin" style="font-weight:bold;text-decoration:underline;">авторизацию\.|<img src="images/pixel_trans\.gif"  alt="" width="1" >|<table     class="Cinema_new_box_2_Contents"><td class="main"><table    align="right"  style="border-collapse: collapse"><table    ><table cellpadding="4"    id="reviews_content"><tr style="background:#d2d2d2;"><td class="main" colspan="2" style="padding:25px;text-align:center', '', text_final5)
            text_final7 = re.sub(r'<a href="images/newsdesk_img/\w*\.jpg" class="image-popup-fit-width">|<img src="images/newsdesk_img/\w*\.jpg"|" align="left" class="news_img">|', '', text_final6)
            text_final8 = re.sub(r'<td class="main">|<td width="70" class="main" align="center" style="padding:4px; background:#444444;"><a class="open_widget " style="color:#ffffff;" |href="http://kinoteatr\.megamag\.by/seance\.php\?id=\d*">|<td style="background:#444444">|;">К настоящему времени нет отзывов, Вы можете стать первым\.|<td width="70" class="main " align="center" style="padding:4px;color:#777777; background:#444444;">', ' ', text_final7)
            text_final9 = re.sub(r"\[|',|'|\\r", '', text_final8)
            text_final10 = re.sub(r']|      ">|">  alt="|" title="', '', text_final9)
            text_final11 = re.sub(r'К-р Юность ', '\n\n<b>К-р Юность </b>', text_final10)
            text_final12 = re.sub(str(url), '', text_final11)
            text_final12 = '<b>'+url+'</b>' + text_final12
            text_final13 = re.sub(r'Год:', '\nГод:', text_final12)
            text_final14 = re.sub(r'<td valign="top"><table    > <td class="main" colspan="\d" style="padding:4px 4px 4px 15px; background:#222222; color: #ffff00;">|', '', text_final13)
            text_final15 = re.sub(r'<td class="main" width="195" style="padding:4px 4px 4px 15px; background:#444444; color: #ffffff;">|<td class="main" width="195" style="padding:4px 4px 4px 15px; background:#333333; color: #ffffff;">', '\n', text_final14)
            text_final16 = re.sub(r'<td width="\d*" class="main" align="center" style="padding:\dpx; background:#333333;">|<td style="background:#333333">|<a class="open_widget " style="color:#ffffff;"', '', text_final15)
            text_final17 = re.sub(r' ">\d* class="tableBoxArea2Contents" align="right"><img src="images/icons/comments\.png"  alt="">|#comments">\d*<table    ><td  class="main" valign="top"><table    ><td  class="main" valign="top"><table    > <div style="display: table-row|<td width="70" class="main" align="center" style="padding:4px; background:#444444;">|<a class="open_widget seance_asterisk" style="color:#ffffff;"|\xa0', '', text_final16)
            text_final19 = re.sub(r'</b>.*\n\nГод', '</b>\n\nГод', text_final17)
            text_final20 = re.sub(r':.*xa0|', '', text_final19)
            text_final21 =re.sub(r'</b>.*newsdesk_id=\d*', '</b>', text_final20)
            text_final22 =re.sub(r'<table.*', '', text_final21)
            if 'К-р Юность ' in text_final11:
                quoleItem = PosterscheduleItem(text=text_final22, url=url)
                yield quoleItem

