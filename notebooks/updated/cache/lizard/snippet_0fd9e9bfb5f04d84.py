def get_methods(self):
    if self.__cache_all_methods is None:
        self.__cache_all_methods = []
        for i in self.get_classes():
            for j in i.get_methods():
                self.__cache_all_methods.append(j)
    return self.__cache_all_methods