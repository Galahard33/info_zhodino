import psycopg2
from itemadapter import ItemAdapter


class ImageCinemaPipeline(object):
    def open_spider(self, spider):
        hostname = 'ec2-3-223-213-207.compute-1.amazonaws.com'
        username = 'grwusbywcvffav'
        password = 'f78c737b40f3de26588eb2dc63ee0b83cfa9d4a17c341cba0fe2509d2136b5e7'  # your password
        database = 'd2579bis4gp1rt'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        self.cur.execute("DELETE FROM test")

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute("insert into test(name, text) VALUES (%s, %s);",
                         (item['url'], item['text']))
        self.connection.commit()
        return item