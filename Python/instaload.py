__author__ = 'seandolinar'

from pymongo import MongoClient
import numpy as np
from sklearn import linear_model
import pylab as pl
import csv
import os
import pandas as pd






class EmojiDict(object):

    def __init__(self, emoji_key):

        #intialize emoji count
        emoji_key['count'] = 0
        self.dict = emoji_key['count'].to_dict()

    def add_emoji_count(self, text):

        for emoji in self.dict.keys():
            if emoji in text:
                self.dict[emoji] += 1


    def __str__(self):
        return str(self.dict)








#loads emoji key
os.chdir('/Users/seandolinar/stats_seandolinar_com/12_December/INSTAGRAM/')
emoji_key = pd.read_csv('emoji_table.txt', encoding='utf-8', index_col=0)

a = EmojiDict(emoji_key)

a.add_emoji_count(u'test \U0001f475')
a.add_emoji_count(u'test \U0001f475')
a.add_emoji_count(u'test \U0001f475')

print a.dict

# def emoji_count(text):
#
#
#
#     for line in range(len(emoji_key)):
#         if re.search(emoji_key['emoji'][line], text):
#             print
#             print emoji_key.ix[line][1]

#
# client = MongoClient('localhost', 27017)
# db = client['mydb']
# collection = db['instagram_test']
#
# x = []
# y = []
# for i in collection.find():
#     x.append([i['user']['followers']])
#     y.append(i['likes_count'])
#
#
#
#
