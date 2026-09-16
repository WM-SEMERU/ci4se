def merge(self, other, is_positive=True):
    other = self.coerce(other, is_positive)
    if self.is_equal(other):
        pass
    elif other.is_entailed_by(self):
        pass
    elif self.is_entailed_by(other):
        self.lower = other.lower
        self.upper = other.upper
        self.__values_computed = False
        return self
    elif self.is_contradictory(other):
        raise Contradiction('Cannot merge partial orders')
    else:

        def add_single_value(val, is_positive):
            if not is_positive:
                if not val in self.lower:
                    self.lower.add(val)
                    self.__values_computed = False
            elif not val in self.upper:
                self.upper.add(val)
                self.__values_computed = False
        for general in other.upper:
            add_single_value(general, True)
        for specific in other.lower:
            add_single_value(specific, False)
    if len(self) == 0:
        raise Contradiction('Partial Ordering has No Members')
    return self