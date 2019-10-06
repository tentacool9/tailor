import socket
import sys
import time


class TcpListen:
    def __init__(self, write, listen_time, address, port):
        self.write = write
        self.listen_time = listen_time
        self.port = port
        self.address = address

    def listen(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bytesrecieved = 0
        # Assign IP address and port number to socket
        serversocket.bind((self.address, self.port))
        serversocket.listen(1)
        while True:
            # Wait for a connection
            print('waiting for a connection')
            connection, client_address = serversocket.accept()
            try:
                print(('connection from ' + client_address[0]))
                begin_time = time.time()

                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(64000)
                    if data:
                        bytesrecieved += len(data)
                        print(data)
                    else:
                        print("data stream ended")
                        break
                    if (time.time() - begin_time) > self.listen_time:
                        print("listening period over")
                        break
            finally:
                # Clean up the connection
                print(bytesrecieved)
                connection.close()
