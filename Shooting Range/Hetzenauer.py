"""
Python Sniping Bot
❤
Maximilian
20.11.2023
"""

# Imports
import time
import config
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from requests_html import HTMLSession, AsyncHTMLSession



base_url = "https://www.vicinityclo.de/"

def get_product_links():
    '''
    Returns list of elements "items",
    each containing a link to product detail page
    '''
    base_shop = base_url
    session = HTMLSession()
    r = session.get(base_shop)
    items = r.html.find('#shop-scroller', first=True).find('li')
    return items, session