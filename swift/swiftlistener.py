import inspect
import sys
import re

from InOut import FIleIO
from listeners.TcpListener import TcpListener

listener = TcpListener(FIleIO.FileWrite("/home/david/Downloads/", "data"),FIleIO.FileWrite("/home/david/Downloads/", "message"), 3, 'localhost', 13000, 0)
listener.listen()
