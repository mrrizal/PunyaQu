#!/usr/bin/env python
# thx for Terry Yin : https://github.com/terryyin/google-translate-python
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE" (Revision 42):
# <terry.yinzhe@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a beer in return to Terry Yin.
#
# Now google has stop providing free translation API. So I have to switch to
# http://mymemory.translated.net/, which has a limit for 1000 words/day free
# usage.
#
# The original idea of this is borrowed from <mort.yao@gmail.com>'s brilliant work
#    https://github.com/soimort/google-translate-cli
#

import json
from textwrap import wrap
from urllib import request
from urllib.parse import quote

def getTranslate(text, fromLang, toLang):
    escaped_source = quote(text, '')
    headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.19\
            (KHTML, like Gecko) Chrome/18.0.1025.168 Safari/535.19'}
    api_url = "http://mymemory.translated.net/api/get?q=%s&langpair=%s|%s"
    req = request.Request(url=api_url % (escaped_source, fromLang, toLang), headers=headers)
    r = request.urlopen(req)
    return r.read().decode('utf-8')

def main():
    text = input('masukan text : ')
    fromLang = input('kode negara asal : ')
    toLang = input('kode negara tujuan : ')
    data = json.loads(getTranslate(text, fromLang, toLang))
    print(data['responseData']['translatedText'])

if __name__ == "__main__":
    main()
