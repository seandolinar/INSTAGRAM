
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

keyword_list = ['cityscape', 'love', 'selfie']

for keyword in keyword_list:
    url = 'http://websta.me/tag/%s' % keyword
    headers = { 'User-Agent' : 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_2_1 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8G4 Safari/6533.18.5' }

    req = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(req)
    outfile = content.read().decode('utf-8')



    with io.open('%s_%s.txt' % (keyword, time), 'w', encoding='utf-8') as file:
        file.write(outfile)



