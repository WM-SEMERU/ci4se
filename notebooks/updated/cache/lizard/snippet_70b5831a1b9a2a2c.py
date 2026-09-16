def extend(self, sequence):
    self.__field.validate(sequence)
    return list.extend(self, sequence)