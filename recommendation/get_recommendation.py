import httplib, urllib, base64, json

headers = {
  'Ocp-Apim-Subscription-Key': 'eb03c05b344a4149812bb7cf99fa0f0e',
}

params = urllib.urlencode({
  'includeMetadata': False,
  'buildId': 1574081,
})

try:
  conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
  conn.request("GET", "/recommendations/v4.0/models/a83472a8-153c-4518-9633-589b6c5d6a99/recommend/item?itemIds=4XZ-00006&numberOfResults=3&minimalScore=0&%s" % params, "", headers)
  response = conn.getresponse()
  data = response.read()
  print json.dumps(json.loads(data), indent=2, sort_keys=True)
  conn.close()
except Exception as e:
    print e
