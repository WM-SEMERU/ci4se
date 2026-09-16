def fail(self):
    if self.failed is True:
        raise AttributeError('Cannot fail {} - it has already failed.'.
            format(self))
    else:
        self.failed = True
        self.time_of_death = timenow()
        self.network.calculate_full()
        for v in self.vectors():
            v.fail()
        for i in self.infos():
            i.fail()
        for t in self.transmissions(direction='all'):
            t.fail()
        for t in self.transformations():
            t.fail()