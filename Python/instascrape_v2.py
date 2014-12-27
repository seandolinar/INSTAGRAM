
import urllib2
import htmllib
import formatter
import sys
import re
from bs4 import BeautifulSoup
import io
import datetime
import time
import calendar
import os

os.chdir('/Users/seandolinar/stats_seandolinar_com/12_December/INSTAGRAM/files')

time = str(calendar.timegm(time.gmtime()))


url = 'http://websta.me/n/elliegoulding' #'http://websta.me/tag/love'
headers = { 'User-Agent' : 'Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3' }

req = urllib2.Request(url, headers=headers)
content = urllib2.urlopen(req)
outfile = content.read().decode('utf-8')



with io.open('test_%s.txt' % time, 'w', encoding='utf-8') as file:
    file.write(outfile)


from selenium import webdriver
from selenium.webdriver.common.keys import Keys


profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override","Mozilla/5.0 (iPad; CPU OS 5_1 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B176 Safari/7534.48.3")
driver = webdriver.Firefox(profile)
driver.get("http://websta.me/n/elliegoulding")
driver.find_element_by_link_text("more comments").click()
print driver.page_source