import io
import os
from bs4 import BeautifulSoup
from pymongo import MongoClient
import urllib2


class instaPost(object):
    def __init__(self, Post=None):
        self.Post = Post
        self.id = self.Post['id'][5:]
        self.posted_time = self.Post.find('span', class_="posted_time").text.strip()
        self.user_name = self.Post.find(class_='username').text


    def get_likes(self):
        like_count = self.Post.find('span', { "id" : 'like_count_%s' % self.id })
        return int(like_count.text)

    def get_comments_count(self):
        comment_count = self.Post.find('span', { "id" : 'comment_count_%s' % self.id })
        return int(comment_count.text)


    def caption(self):
        caption_block = self.Post.find(class_='clearfix caption')
        caption_return = caption_block.text.replace(self.user_name, '')
        return caption_return.replace(self.posted_time, '')


    def comments(self):
        comment_block = self.Post.find_all(class_='clearfix comment_normal')
        comment_list = []

        if len(comment_block) > 0:

            for comment in comment_block:
                comment_user = comment.find('strong').get_text()
                comment_time = comment.find(class_='comment_time').get_text()

                comment_list.append({'text' : comment.text, 'user' : comment_user, 'post_time' : comment_time})

        return comment_list


class instaUser(object):
    def __init__(self, user_name=None):
        self.user_name = user_name

        url = 'http://websta.me/n/%s' % user_name

        req = urllib2.Request(url)
        content = urllib2.urlopen(req)
        soup = BeautifulSoup(content.read().decode('utf-8'))

        self.followers = int(soup.find(class_="counts_followed_by").text.replace(',', ''))
        self.following = int(soup.find(class_="following").text.replace(',', ''))




path = '/Users/seandolinar/stats_seandolinar_com/12_December/INSTAGRAM/files'
os.chdir('/Users/seandolinar/stats_seandolinar_com/12_December/INSTAGRAM/files')
files = os.listdir(path)

client = MongoClient('localhost', 27017)
db = client['mydb']
collection = db['instagram_test']




for file in files:
    if file != '.DS_Store':

        search_term = file.split('_')[0]
        print file
        url_soup = BeautifulSoup(io.open(file, encoding='utf-8').read())


        for i in url_soup.find_all('div', class_='photobox'):

            try:
                instagram_post = instaPost(i)
                instagram_user = instaUser(instagram_post.user_name)


                instagram_dict = dict(_id=instagram_post.id,
                                      user={'name': instagram_post.user_name, 'following': instagram_user.following,
                                            'followers': instagram_user.followers},
                                      posted_time=instagram_post.posted_time, likes_count=instagram_post.get_likes(),
                                      comment_count=instagram_post.get_comments_count(),
                                      caption=instagram_post.caption(), comments=instagram_post.comments(),
                                      search_term=search_term)

                print instagram_dict
            except:
                print '/n instagram failed'
                print
                pass

            try:
                collection.insert(instagram_dict)
            except:  #duplicate key
                pass


