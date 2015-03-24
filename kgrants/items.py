# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KgrantsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    page = scrapy.Field()
    project = scrapy.Field()
    description = scrapy.Field()
    fiscal_agent = scrapy.Field()
    year = scrapy.Field()
    date_awarded = scrapy.Field()
    amount = scrapy.Field()
    grant_period = scrapy.Field()
    grant_period_start = scrapy.Field()
    grant_period_end = scrapy.Field()
    initiative = scrapy.Field()
    community = scrapy.Field()
    focus_area = scrapy.Field()
    grantee_contact_name = scrapy.Field()
    grantee_contact_email = scrapy.Field()
    grantee_contact_website = scrapy.Field()
    grantee_contact_location = scrapy.Field()
    grantee_contact_facebook = scrapy.Field()
    grantee_contact_twitter = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()


