def writetofile(self, filename):
    f = open(filename, 'w')
    f.write(self.read())
    f.close()