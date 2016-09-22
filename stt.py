import sys
import json
import urllib
import urllib2
import uuid
import os

tokenUri = "https://oxford-speech.cloudapp.net/token/issueToken"
speechUri = "https://speech.platform.bing.com/recognize"

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

def postAudio(token,path):
	
	info = {
		"appid": "D4D52672-91D7-4C74-8AD8-42B1D98141A5",
		"version": "3.0",
		"format": "json",
		"locale": "en-US",
		"device.os": "Windows OS",
		"scenarios": "ulm",
		"instanceid": "565D69FF-E928-4B7E-87DA-9A750B96D9E3",
		"requestid": str(uuid.uuid1())
	}

	data = open(path, 'rb').read()

	requstUrl = speechUri + "?" + urllib.urlencode(info)
	req = urllib2.Request(requstUrl, data)
	req.add_header("Authorization", "Bear " + token)
	req.add_header('Content-Type', 'audio/wav; codec=""audio/pcm""; samplerate=16000')


	response = urllib2.urlopen(req)
	print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)


def main():

	token = getAccessToken("8a3e89618533429aae5c45c64127fd1c")
	postAudio(token, "whatstheweatherlike.wav")

if __name__ == '__main__':
	main()
