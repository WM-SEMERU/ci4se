def add(self, entity):
    do_append = self.__check_new(entity)
    if do_append:
        self.__entities.append(entity)