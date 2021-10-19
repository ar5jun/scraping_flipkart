# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3



class Flip2Pipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("testdb")
        self.curr = self.conn.cursor()

    def create_table(self):
        #self.curr.execute("""DROP TABLE IF EXISTS mob""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS mob(
            name VARCHAR(100),
            price VARCHAR(15),
            memory VARCHAR(100),
            camera VARCHAR(100),
            display VARCHAR(100),
            cpu VARCHAR(100),
            img_url VARCHAR(1000)
        )""")


    def process_item(self, item, spider):

        self.store_db(item)
        return item

    def store_db(self,item):

        self.curr.execute("""insert into mob values (?,?,?,?,?,?,?)""",
        (item['name'][0],item['price'][0],item['memory'][0],item['camera'][0],item['display'][0],item['cpu'][0],item['img_url'][0]
        ))
        self.conn.commit()