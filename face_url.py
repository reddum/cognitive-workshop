import sys
import json
import urllib2

api = "https://api.projectoxford.ai/face/v1.0/detect"
url = "http://www.mymypic.net/data/attachment/forum/201603/22/0820124f4x5ald665ndux5.jpg"

data = {
  "url": url
}

req = urllib2.Request(api)
req.add_header("Ocp-Apim-Subscription-Key", "")
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)