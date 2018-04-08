#coding=utf-8
import json
import urllib2
url="http://localhost:8888"
data=urllib2.urlopen(url).read()
value=json.loads(data.decode('utf-8'))
#value=value.encode('utf-8')
print value
