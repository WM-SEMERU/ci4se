def fehalf(self):
    if self.__fehalf != None:
        return self.__fehalf
    self.log('fehalf')
    self.__fehalf = self.parcov.u * self.parcov.s ** 0.5
    self.log('fehalf')
    return self.__fehalf