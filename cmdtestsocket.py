import os
import json
import urllib2
from socket import * 
import sys
import uuid
score=0
if len(sys.argv)!=3:
    print "student number or student name  error!"
    sys.exit()
def get_mac_address(): 
    mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
    return ":".join([mac[e:e+2] for e in range(0,11,2)])
def get_host_ip():
    try:
        s = socket(AF_INET, SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
#get host name
myname = gethostname( )
#get host ip
#myaddr = gethostbyname(myname)
myaddr=get_host_ip()
homepath=os.environ['HOME']
jsondata={}
jsondata["hostname"]=myname
jsondata["addr"]=myaddr
jsondata["mac"]=get_mac_address()
jsondata["stuno"]=sys.argv[1]
jsondata["stuname"]=sys.argv[2]
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
j_data=json.dumps(jsondata)
def start_tcp_client(ip,port):
    server_ip=ip
    server_port=port
    tcp_client=socket(AF_INET,SOCK_STREAM)
    try:
        tcp_client.connect((server_ip,server_port))
    except error:
        print 'fail to setup socket connection'
    else:
        tcp_client.sendall(j_data)
    tcp_client.close()
start_tcp_client("127.0.0.1",8888)
print score
print jsondata
print j_data
