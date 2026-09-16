def match(self, xn):
    if all(map(lambda x: x.match(xn), self.conditions)):
        return self.outcomes
    return None