from bluetooth import *
import sys, tty, termios

if sys.version < '3':
    input = raw_input

addr = None

if len(sys.argv) < 2:
    print("no device specified.  Searching all nearby bluetooth devices for")
    print("the BeagleBoneService")
else:
    addr = sys.argv[1]
    print("Searching for BeagleBoneServic e on %s" % addr)

# search for the Rover 5 service
uuid = "2779f017-40cc-4c14-8632-f562ad5b54c8"
service_matches = find_service( "BeagleBoneService", uuid )

if len(service_matches) == 0:
    print("couldn't find the Rover 5 service =(")
    sys.exit(0)

#If we found a match
first_match = service_matches[0]
# port = first_match["port"]
port = 2
name = first_match["name"]
host = first_match["host"]

print "Port McPorterson: ", port
print("connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setraw(sys.stdin.fileno())

#we are connected, now we can type commands
print("connected.  type stuff")
data = 0
while (data < 20):
    sock.send(data)
    data += 1
    time.sleep(1)
sock.close()
