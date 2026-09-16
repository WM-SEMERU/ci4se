def UNas(self, to='name_short'):
    if isinstance(to, str):
        to = [to]
    return self.data[self.data.UNmember > 0][to]