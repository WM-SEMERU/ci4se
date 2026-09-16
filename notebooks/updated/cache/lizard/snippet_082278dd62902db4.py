def nth(self, index):
    self.__prepare()
    return None if self.count() < math.fabs(index) else self._json_data[index]