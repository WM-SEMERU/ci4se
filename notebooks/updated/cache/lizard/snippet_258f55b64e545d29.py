def checkOneValue(self, v, strict=0):
    if v in [None, INDEF] or isinstance(v, str) and v[:1] == ')':
        return v
    elif v == '':
        return None
    elif self.choice is not None and v not in self.choiceDict:
        schoice = list(map(self.toString, self.choice))
        schoice = '|'.join(schoice)
        raise ValueError(
            'Parameter %s: value %s is not in choice list (%s)' % (self.
            name, str(v), schoice))
    elif self.min not in [None, INDEF] and v < self.min:
        raise ValueError(
            "Parameter %s: value `%s' is less than minimum `%s'" % (self.
            name, str(v), str(self.min)))
    elif self.max not in [None, INDEF] and v > self.max:
        raise ValueError(
            "Parameter %s: value `%s' is greater than maximum `%s'" % (self
            .name, str(v), str(self.max)))
    return v