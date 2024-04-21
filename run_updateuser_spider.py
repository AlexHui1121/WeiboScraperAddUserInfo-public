import os
from scrapy.utils.project import get_project_settings
from spiders.UpdateUser import UpdateUserInfoSpider
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.crawler import CrawlerProcess


from scrapy.utils.log import configure_logging
import glob

if __name__ == '__main__':
    os.environ['SCRAPY_SETTINGS_MODULE'] = 'settings'
    settings = get_project_settings()
    process = CrawlerProcess(settings)
    runner = CrawlerRunner(settings)
    @defer.inlineCallbacks
    def crawl():
        path_to_directory = os.path.join('input', '*.jsonl')
        jsonl_files = glob.glob(path_to_directory)

        # Now you can loop through the files and process them one by one
        for jsonl_file in jsonl_files:
            filename = os.path.basename(jsonl_file)
            yield runner.crawl(UpdateUserInfoSpider, jsonl_file=jsonl_file, filename=filename)
            # the script will block here until the crawling is finished
        reactor.stop()


    crawl()
    reactor.run()  # the script will block here until the last crawl call is finishedA
    
    
    

