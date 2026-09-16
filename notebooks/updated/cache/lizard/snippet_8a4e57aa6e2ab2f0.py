def _pre_emphasis(self):
    self.data = numpy.append(self.data[0], self.data[1:] - self.
        emphasis_factor * self.data[:-1])