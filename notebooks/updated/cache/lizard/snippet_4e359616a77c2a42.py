def __expire_files(self):
    self.__files = OrderedDict(item for item in self.__files.items() if not
        item[1].expired)