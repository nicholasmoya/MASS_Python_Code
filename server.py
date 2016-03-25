import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

port = 2
server_sock.bind(("", port))
server_sock.listen(1)

# client sock is a BluetoothSocket object
# client address is a (host, channel) tuple, where host is the client adapter and channel is port
client_sock, client_address = server_sock.accept()
print "Client host and channel: ", client_address

try:
    while 1:
        data = client_sock.recv(1024)
        print("received [%s]" % data)
                          
except IOError:
    pass


client_sock.close()
server_sock.close()
