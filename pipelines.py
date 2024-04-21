# -*- coding: utf-8 -*-
import datetime
import json
import os.path
import time
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class JsonWriterPipeline(object):   
    def __init__(self):
        if not os.path.exists('output'):
            os.mkdir('output')
    
    def open_spider(self, spider):
        print('======Spider Opened======')
        file_name = spider.filename.replace('keyword', 'updatinguserinfo')
        spider.file_name = file_name
        spider.file_path = f'output/{file_name}'
        spider.file_path_with_format = spider.file_path
        check_file_path = spider.file_path_with_format.replace('updatinguserinfo','updateduserinfo')
        if not os.path.exists(check_file_path):
            spider.file = open(spider.file_path_with_format, 'at', encoding='utf-8')


    def close_spider(self, spider):
        spider.file.close()
        old_file_path = spider.file_path_with_format
        new_file_path = 'output/'+spider.file_name.replace('updatinguserinfo', 'updateduserinfo')
        os.rename(old_file_path, new_file_path)

        

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        spider.file.write(line)
        spider.file.flush()
        return item