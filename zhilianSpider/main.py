from scrapy import cmdline

# cmdline.execute('scrapy crawl zhilianjob'.split())
import os

os.chdir('zhilian/spiders')
cmdline.execute('scrapy runspider zhilianjob.py'.split())