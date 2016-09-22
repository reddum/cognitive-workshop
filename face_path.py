import sys
import json
import urllib2
import os


api = "https://api.projectoxford.ai/face/v1.0/detect?returnFaceId=true&returnFaceAttributes=age,gender"
path = "sample.jpg"
data = open(path, "rb").read()

req = urllib2.Request(api, data=data)
req.add_header("Ocp-Apim-Subscription-Key", "")
req.add_header('Content-Type', 'application/octet-stream')

response = urllib2.urlopen(req)
print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)