#coding=utf-8
import os
import os.path
import itchat, time
from itchat.content import *
import urllib
import requests
from aip import AipSpeech
url = "https://www.hotpoor.com/api/comment/submit_secret_for_hackathon"

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
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

@itchat.msg_register([TEXT,RECORDING], isGroupChat=False)
def text_reply(msg):
    if msg.Type == "Text":
        print u"独立用户:%s"%msg.user.get("NickName",u"未知")
        print msg.keys()
        for k in msg.keys():
            print u"%s: %s"%(k,msg[k])
        values = {
            'aim_id': 'HACKATHON',
            'content': msg["Text"],
        }
        res = requests.get(url, values)
        print res.status_code
        print res.content

    else:
        print msg.user["NickName"]
        print u"获得语音"
        if msg.user["NickName"] == u"Helen小布熊":
            msg.download(msg.fileName)
            fileName_base = msg.fileName
            fileName_main = fileName_base.split(".")[0]
            os.system("ffmpeg -i %s -f wav -ar 16000 %s.wav"%(fileName_base, fileName_main))

            file_name = "%s.wav" % fileName_main
            file_type = "wav"
            file_rate = 16000

            APP_ID = "9082071"
            API_KEY = "PXirZpvwwZ9hsKqaLYcLXLzq"
            SECRET_KEY = "ef6788d39df2bb689437d0cb9b6dbda6"

            client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
            localfile = os.path.join(os.path.dirname(__file__), "%s" % file_name)
            result = client.asr(get_file_content(localfile), file_type, file_rate, {
                'dev_pid': 1536,
            })
            print result
            print u"======"
            values = {
                'aim_id': 'HACKATHON',
                'content': result.get("result",[u"语音识别失败"]),
            }
            res = requests.get(url, values)
    return

@itchat.msg_register([TEXT,RECORDING], isGroupChat=True)
def text_reply(msg):
    if msg.Type == "Text":
        print u"群名称:%s"%msg.user["NickName"]
        print u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text)
        # urlt = url + urllib.parse.quote(msg.text)
        # values = {
        #     'aim_id': 'HACKATHON',
        #     'content': msg["Text"],
        # }
        # res = requests.get(url, values)
        # print res.status_code
        # print res.content

    else:
        print msg.user["NickName"]
        print u"@%s\u2005I Listened: %s" % (msg.actualNickName, msg.fileName)
        # msg.download(msg.fileName)
    return
itchat.auto_login(hotReload=True)
itchat.run(True)