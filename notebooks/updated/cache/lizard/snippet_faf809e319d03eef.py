def saveLogs(self, filename):
    f = open(filename, 'wb')
    cPickle.dump(self.logs, f)
    f.close()