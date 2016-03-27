import bluetooth
import sys, time
from client_setup import *

if sys.version < '3':
   input = raw_input

sock = client_setup()

print "Client connected to server."

print "Type and hit enter to send."

while 1:
    data = sys.stdin.read(1)
    sock.send(data)

print "Closing connection."
sock.close()
