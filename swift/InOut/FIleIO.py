class FileWrite:

    def __init__(self, directory, filename):
        self.dir = directory
        self.filename = filename
        f = open(directory + filename, "w+")
        f.close()

    def write(self, data):
        f = open(self.dir + self.filename, 'a+')
        f.write(data.decode('UTF-8'))
        f.close()
