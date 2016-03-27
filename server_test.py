import bluetooth
from server_setup import *

server_sock, client_sock = server_setup()

try:
    while 1:
        data = client_sock.recv(1024)
        print("Received [%s]" % data)
                          
except IOError:
    print "IOError"
    pass

client_sock.close()
server_sock.close()
