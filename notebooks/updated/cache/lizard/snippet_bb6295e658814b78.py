def load(self, filename='classifier.dump'):
    ifile = open(filename, 'r+')
    self.classifier = pickle.load(ifile)
    ifile.close()