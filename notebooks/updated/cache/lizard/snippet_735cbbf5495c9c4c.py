def EU28as(self, to='name_short'):
    if type(to) is str:
        to = [to]
    return self.data[self.data.EU < 2015][to]