#coding=utf-8
import itchat, time
from itchat.content import *
import urllib

url = "https://www.hotpoor.com/api/comment/submit_secret_for_hackathon?aim=HACKATHON&content="

# @itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
# def text_reply(msg):
#     msg.user.send('%s: %s' % (msg.type, msg.text))

# @itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
# def download_files(msg):
#     msg.download(msg.fileName)
#     typeSymbol = {
#         PICTURE: 'img',
#         VIDEO: 'vid', }.get(msg.type, 'fil')
#     return '@%s@%s' % (typeSymbol, msg.fileName)

# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')

@itchat.msg_register([TEXT,RECORDING], isGroupChat=True)
def text_reply(msg):
    if msg.Type == "Text":
        print msg.user["NickName"]
        print u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text)
        # urlt = url + urllib.parse.quote(msg.text)
        content = "%s"%msg.text
        print content
        urlt = url + urllib.quote(content)
        urllib.urlopen(urlt)

    else:
        print msg.user["NickName"]
        print u"@%s\u2005I Listened: %s" % (msg.actualNickName, msg.fileName)
        # msg.download(msg.fileName)

itchat.auto_login(hotReload=True)
itchat.run(True)