# -*- coding: utf-8 -*-
import MySQLdb
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class YnzpPipeline(object):
    def __init__(self):

        self.conn = MySQLdb.connect(host='localhost', port=3306, user="root", password="123456", db="snick",charset="utf8")
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into rencaiwang values (%s,%s,%s,%s,%s,%s,%s,%s)"
        self.cursor.execute(sql,(item['name'],item['job'],item['sex'],item['age'],item['height'],item['marriage'],item['education'],item['Intention_job']))
        self.conn.commit()
        return item