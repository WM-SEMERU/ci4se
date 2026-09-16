def EU27as(self, to='name_short'):
    if isinstance(to, str):
        to = [to]
    return self.data[self.data.EU < 2013][to]