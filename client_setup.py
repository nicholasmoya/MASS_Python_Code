import bluetooth
import sys, tty, termios
import subprocess

def client_setup():

    # Find the first remote bluetooth adapter's BD address
    address_info = subprocess.check_output(["hcitool", "scan"])
    address_index = address_info.find("Scanning") + 14
    address = address_info[address_index : address_index + 17]
    host = str(address)

    print "Remote Bluetooth Adapter BD Address: ", host

    port = 2

    # Create the client socket
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((host, port))

    return sock
