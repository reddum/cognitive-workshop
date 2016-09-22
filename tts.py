# -*- coding: UTF-8 -*-

import sys
import json
import urllib
import urllib2
import uuid
import os

tokenUri = "https://oxford-speech.cloudapp.net/token/issueToken"
speechUri = "https://speech.platform.bing.com/synthesize"

def getAccessToken(clientSecret):

  info =  { 
    "grant_type" : "client_credentials", 
    "client_id" : clientSecret, 
    "client_secret": clientSecret, 
    "scope": "https://speech.platform.bing.com"
  }

  req = urllib2.Request(tokenUri, data= urllib.urlencode(info))
  response = urllib2.urlopen(req)
  return json.loads(response.read())["access_token"]

def postText(text, token):
  
  name = "Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)"
  payload = "<speak version='1.0' xml:lang='zh-TW'><voice xml:lang='zh-TW' xml:gender='Female' name='Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)'>" + text + "</voice></speak>"
  contentType = "application/ssml+xml"

  req = urllib2.Request(speechUri, payload)
  req.add_header("Authorization", "Bear " + token)
  req.add_header('Content-Type', contentType)
  req.add_header('X-Microsoft-OutputFormat', "riff-8khz-8bit-mono-mulaw")

  response = urllib2.urlopen(req)
  writeStreamToFile(response)

def writeStreamToFile(response):
  CHUNK = 16 * 1024

  with open("output.wav", 'wb') as f:
    while True:
      chunk = response.read(CHUNK)
      if not chunk: 
        break
      f.write(chunk)  

def main():

  key = "8a3e89618533429aae5c45c64127fd1c"
  postText("很高興今天來到緯創", getAccessToken(key))

if __name__ == '__main__':
  main()