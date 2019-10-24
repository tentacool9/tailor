import socket
import sys
import time
from InOut import FIleIO


class TcpListener:
    # maximum
    def __init__(self, write_whole_data, write_first_message, listen_time, address, port, maximum_data):
        self.write_whole_data = write_whole_data
        self.write_first_message = write_first_message
        self.listen_time = listen_time
        self.port = port
        self.address = address
        self.maximum_data = maximum_data

    def listen(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        bytes_received = 0
        packets_received = 0
        # Assign IP address and port number to socket
        server_socket.bind((self.address, self.port))
        server_socket.listen(1)

        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = server_socket.accept()
        try:
            print(('connection from ' + client_address[0]))
            # time when started listening
            begin_time = time.time()
            seconds = int(begin_time)
            graph = []
            # Receive the data in small chunks and retransmit it
            while True:
                if (time.time() - begin_time) > self.listen_time:
                    print("listening period over")
                    break

                # receive max buffer size of tcp packet
                data = connection.recv(64000)

                # create the graph, each second append the size of the data to the graph array
                if seconds + 1 == int(time.time()):
                    print(int(time.time()))
                    seconds = int(time.time())
                    graph.append(len(data))
                # if the data is not null
                if data:
                    packets_received += 1
                    if packets_received == 1:
                        self.write_first_message.write(data)
                    bytes_received += len(data)
                    self.write_whole_data.write(data)
                else:
                    print("data stream ended")
                    break
            # check if listen time finished

        finally:
            # Clean up the connection
            print(graph)
            print("Messages received %d" % packets_received)
            print("%d KB/s" % (bytes_received / 1000 / self.listen_time))
            connection.close()
            return {"Graph": graph, "Messages": packets_received, "KB": (bytes_received / 1000 / self.listen_time)}
