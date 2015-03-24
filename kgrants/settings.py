# -*- coding: utf-8 -*-

# Scrapy settings for kgrants project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

import datetime
BOT_NAME = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
USER_AGENT = 'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)'
COOKIES_ENABLED = True
LOG_FILE = 'log_'+ str(datetime.date.today())+'.txt'

SPIDER_MODULES = ['kgrants.spiders']
NEWSPIDER_MODULE = 'kgrants.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'kgrants (+http://www.yourdomain.com)'
