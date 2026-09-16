def random(self, max_number=None):
    min_number = self.obj
    if max_number is None:
        min_number = 0
        max_number = self.obj
    return random.randrange(min_number, max_number)