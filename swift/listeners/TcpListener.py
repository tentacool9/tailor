import socket
import sys
import time


class TcpListener:
    # maximum
    def __init__(self, write, listen_time, address, port,maximum_data):
        self.write = write
        self.listen_time = listen_time
        self.port = port
        self.address = address
        self.maximum_data =maximum_data

    def listen(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bytesrecieved = 0
        # Assign IP address and port number to socket
        serversocket.bind((self.address, self.port))
        serversocket.listen(1)

        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = serversocket.accept()
        try:
            print(('connection from ' + client_address[0]))
            # time when started listening
            begin_time = time.time()

            # Receive the data in small chunks and retransmit it
            while True:
                if (time.time() - begin_time) > self.listen_time:
                    print("listening period over")
                    break
                data = connection.recv(64000)
                if data:
                    bytesrecieved += len(data)
                    self.write.write(data)
                else:
                    print("data stream ended")
                    break
            # check if listen time finished

        finally:
            # Clean up the connection
            print("%d KB/s" % (bytesrecieved / 1000 / self.listen_time))
            connection.close()
