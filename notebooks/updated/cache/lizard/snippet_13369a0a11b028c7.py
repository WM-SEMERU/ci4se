def split(self, point=None):
    if point is None:
        point = len(self) / 2
    r1 = Sequence(self.name + '.1', self.sequenceData[:point])
    r2 = Sequence(self.name + '.2', self.sequenceData[point:])
    return r1, r2