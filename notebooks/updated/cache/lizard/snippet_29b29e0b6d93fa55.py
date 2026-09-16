def apply_karhunen_loeve_scaling(self):
    cnames = copy.deepcopy(self.jco.col_names)
    self.__jco *= self.fehalf
    self.__jco.col_names = cnames
    self.__parcov = self.parcov.identity