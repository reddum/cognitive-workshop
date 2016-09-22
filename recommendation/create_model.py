
import sys
import json
import urllib
import urllib2
import os

api = "https://westus.api.cognitive.microsoft.com/recommendations/v4.0/models"

data = {
  "modelName": "recommend_demo",
  "description": "ct x wistron recommendation demo"
}

req = urllib2.Request(api)
req.add_header('Ocp-Apim-Subscription-Key', "eb03c05b344a4149812bb7cf99fa0f0e")
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, data=json.dumps(data))
print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)




