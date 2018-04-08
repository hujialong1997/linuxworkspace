import web
import socket
#from outjson import index
import json
HOSTPORT='127.0.0.1',8888
listen_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listen_socket.bind(HOSTPORT)
listen_socket.listen(1)
#jsondata=index()
print 'Serving HTTP on port %s ...' %HOSTPORT[1]
while True:
    client_connection,client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    ''' print request
    http_response="""
    HTTP/1.1 200 OK
    Hello,World!
    """
    jsondata.GET()'''
    #web.header('context-type','text/html')
    
    client_connection.sendall(json.dumps({'one':'1'}).encode('utf-8'))
    #ttp_response)
    client_connection.close()
