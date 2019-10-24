import math
import socket
import sys
import time
# Create a TCP/IP socket
from random import random, randint

from numpy.matlib import rand

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 13000)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    f = open("/home/david/Downloads/text.json", "r")
    message = f.read()
    begintime = time.time()
    while (time.time() - begintime) < 100:
        if randint(0,1000) < 2:
            sock.sendall(message.encode('ascii'))
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        print(amount_expected)

finally:
    print (sys.stderr, 'closing socket')
    sock.close()