def save(self, filename='classifier.dump'):
    ofile = open(filename, 'w+')
    pickle.dump(self.classifier, ofile)
    ofile.close()