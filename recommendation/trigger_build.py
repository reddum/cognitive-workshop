import sys
import json
import urllib
import urllib2
import os

api = "https://westus.api.cognitive.microsoft.com/recommendations/v4.0/models/%(modelId)s/builds"
file_path = "data/UsageFile1.csv"

params = {
  "modelId": "a83472a8-153c-4518-9633-589b6c5d6a99",
}

req = urllib2.Request(api % params)
req.add_header('Ocp-Apim-Subscription-Key', "eb03c05b344a4149812bb7cf99fa0f0e")
req.add_header('Content-Type', 'application/json')

###
# https://azure.microsoft.com/en-us/documentation/articles/cognitive-services-recommendations-buildtypes/
###

data = {
  "description": "Simple recomendations build",
  "buildType": "recommendation",
  "buildParameters": {
    "recommendation": {
      "numberOfModelIterations": 10,
      "numberOfModelDimensions": 40,
      "itemCutOffLowerBound": 1,
      "itemCutOffUpperBound": 10,
      "userCutOffLowerBound": 0,
      "userCutOffUpperBound": 0,
      "enableModelingInsights": False,
      "useFeaturesInModel": False,
      "modelingFeatureList": "",
      "allowColdItemPlacement": False,
      "enableFeatureCorrelation": True,
      "reasoningFeatureList": "",
      "enableU2I": True
    }
  }
}

try:
  response = urllib2.urlopen(req, json.dumps(data))
  print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)
except Exception as e:
  print("[Errno {0}] {1}".format(e.errno, e.strerror))