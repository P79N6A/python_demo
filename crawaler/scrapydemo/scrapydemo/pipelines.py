# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapydemoPipeline(object):
    def open_spider(self, spider):
        self.f = open('test.txt', 'a')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(item) + "\n"
            self.f.write(line)
        except Exception as e:
            print(e)
