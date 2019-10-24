import inspect
import sys
import re
from Analyzer import Analyzer
from listeners import TcpListener
from InOut import FIleIO
from machinelearn import train_model
from machinelearn import test_clustering
import json

# if sys.argv[1] == 'TCP':
#     listener = TcpListener(0, 1, 'localhost', 14000);
# elif sys.argv[1] == 'UDP':
#     listener = TcpListener(0, 1, 'localhost', 14000);
# else:
#     raise Exception

# listener = TcpListener.TcpListener(FIleIO.FileWrite("/home/david/Downloads/", "testfile"), 1, 'localhost', 13000,0)
#
# listener.listen()
test_clustering(3,False)
analyzer = Analyzer('/home/david/Documents/trained_clustering.pkl', '/home/david/Documents/prediction',
                    '/home/david/Documents/trained_vectorizer.pkl', test_clustering(3, False))
print(analyzer.find_d_format(True))
