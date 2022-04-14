import psycopg2
from itemadapter import ItemAdapter


class ImageCinemaPipeline(object):
    def open_spider(self, spider):
        hostname = ''
        username = ''
        password = ''  # your password
        database = ''
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
