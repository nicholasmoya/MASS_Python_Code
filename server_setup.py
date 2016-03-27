import bluetooth

def server_setup():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    port = 2
    server_sock.bind(("", port))
    server_sock.listen(1)

    print("Listening on port %i" % port)

    # client sock is a BluetoothSocket object
    # client address is a (host, channel) tuple, where host is the client adapter and channel is port
    client_sock, client_address = server_sock.accept()

    print("Client connected to server.")
    print("Client host and channel: %s." % str(client_address))

    return server_sock, client_sock

    # client_sock.close()
    # server_sock.close()
