def int_global_to_local(self, index, axis=0):
    if index >= self.__mask[axis].stop - self.__halos[1][axis]:
        return None
    if index < self.__mask[axis].start + self.__halos[0][axis]:
        return None
    return index - self.__mask[axis].start