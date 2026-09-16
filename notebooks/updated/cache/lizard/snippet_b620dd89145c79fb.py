def randtuple(self):
    return tuple(self.randint for x in range(0, self.random.randint(3, 10)))