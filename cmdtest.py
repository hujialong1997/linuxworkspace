import os
import json
import urllib2
score=0
homepath=os.environ['HOME']
jsondata={}
#os.path.expanduser('$HOME')
os.chdir(homepath)
if os.path.exists("testdir"):
    os.chdir("testdir")
    score=score+1
    jsondata["testdir"]=1
else:
    jsondata["testdir"]=0
if os.path.exists("mydir"):
    score=score+1
    jsondata["mydir"]=1
else:
    jsondata["mydir"]=0
if os.path.isfile("passwd"):
    score=score+1
    jsondata["passwd"]=1
else:
    jsondata["passwd"]=0
myurl="http://localhost"
port="8888"
route="login"
j_data=json.dumps(jsondata)
headers={'Content-Type':'application/json'}
def jsonPost(url):
    req=urllib2.Request(url,j_data,headers)
    page=urllib2.urlopen(req)
    res=page.read()
    page.close()
    return res
print score
print jsondata
print j_data
res=jsonPost("%s:%s/%s"%(myurl,port,route))
print res
