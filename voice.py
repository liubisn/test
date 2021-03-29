#coding:utf-8
from aip import AipSpeech

'''your APPID AK SK'''
APP_ID = '23814855'
API_KEY = 'saYGlZIVyX6hgIOv92B6fCAo'
SECRET_KEY = 'ZbSdVMdmohIdAK5pf4yrip1h0kffHayf'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)

s='你好，刘伊墨，我是你爸爸刘笔生，有什么困难可以来联系我'

speech = client.synthesis(s, 'zh',1)

if not isinstance(speech, dict):
    with open('myaudio.mp3','wb') as f:
        f.write(speech)
