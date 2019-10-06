from socket import *
class udplisten:
  def __init__(self, write,listen_time):
    self.write = write
    self.listen_time = listen_time
    PORT = 12000


  def listen(self):
      serverSocket = socket(AF_INET, SOCK_DGRAM)

      # Assign IP address and port number to socket
      serverSocket.bind(('', self.PORT))

      while True:
          # Receive the client packet along with the address it is coming from
          message, address = serverSocket.recvfrom(1500)

