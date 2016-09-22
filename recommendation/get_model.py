########### Python 2.7 #############
import httplib, urllib, base64, json

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'eb03c05b344a4149812bb7cf99fa0f0e',
}

params = urllib.urlencode({
	"id": "a83472a8-153c-4518-9633-589b6c5d6a99"
})

try:
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/recommendations/v4.0/models/{id}?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print json.dumps(json.loads(data), indent=2, sort_keys=True)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))