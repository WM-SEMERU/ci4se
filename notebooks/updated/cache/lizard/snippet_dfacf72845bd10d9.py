def traverse(self, visit, *args, **kwargs):
    if not self.__visited:
        visit(self, *args, **kwargs)
        self.__visited = True
        self._traverse(visit, *args, **kwargs)
        self.__visited = False