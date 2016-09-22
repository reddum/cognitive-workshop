import sys
import json
import urllib
import urllib2
import os

api = "https://westus.api.cognitive.microsoft.com/recommendations/v4.0/models/%(modelId)s/catalog?catalogDisplayName=%(catalogDisplayName)s"
file_path = "data/catalog.csv"

params = {
	"modelId": "a83472a8-153c-4518-9633-589b6c5d6a99",
	"catalogDisplayName": "CatalogFile1"
}

data = open(file_path, "rb").read()
req = urllib2.Request(api % params, data=data)
req.add_header('Ocp-Apim-Subscription-Key', "eb03c05b344a4149812bb7cf99fa0f0e")

response = urllib2.urlopen(req)
print json.dumps(json.loads(response.read()), indent=2, sort_keys=True)

# {
#   "errorLineCount": 0,
#   "errorSummary": [],
#   "importedLineCount": 2424,
#   "processedLineCount": 2424
# }

