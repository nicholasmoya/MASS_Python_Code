import bluetooth
import sys, tty, termios
import subprocess

if sys.version < '3':
    input = raw_input

port = 2

# Find the local bluetooth adapter's BD address
address_info = subprocess.check_output(["hciconfig"])
address_index = address_info.find("BD") + 12
address = address_info[address_index : address_index + 17]
print "Local Bluetooth Adapter BD Address: ", address
host = str(address)

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

#we are connected, now we can type commands
print("connected.  type stuff")
while 1:
    data = sys.stdin.read(1)
    sock.send(data)

sock.close()
