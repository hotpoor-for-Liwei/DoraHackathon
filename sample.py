# -*- coding: utf-8 -*-
import urllib
import jieba
import json

address = 'https://www.hotpoor.com/api/comment/submit_secret_for_hackathon?'
mydict = {'aim_id':'0cd8429c1da249b6935d7eef72d7fc0b'}

def onQQMessage(bot, contact, member, content):
    if not bot.isMe(contact, member):
        mylist = jieba.lcut(content)
        print(mylist)

        # Writing JSON data
        with open('data.json', 'w') as f:
            json.dump(mylist, f)
       
        mydict['content'] = content
        urllib.request.urlopen(address+urllib.parse.urlencode(mydict))