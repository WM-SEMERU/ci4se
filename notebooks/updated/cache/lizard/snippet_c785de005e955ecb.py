def recarray(self):
    return numpy.rec.fromrecords(self.records, names=self.names)