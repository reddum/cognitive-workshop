import sys
import json
import urllib
import urllib2
import os


api = "https://api.projectoxford.ai/vision/v1.0/analyze?%s"

params = urllib.urlencode({
    'visualFeatures': 'Categories,Tags,Description,Faces',
    'details': 'Celebrities',
})

path = "sample.jpg"
data = open(path, "rb").read()

req = urllib2.Request(api % params, data=data)
req.add_header("Ocp-Apim-Subscription-Key", "169ca754705e4fb9bd187a876a807af9")
req.add_header('Content-Type', 'application/octet-stream')

response = urllib2.urlopen(req)
print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)


