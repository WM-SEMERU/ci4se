def head(self, n=5):
    if n >= len(self.index):
        return self.copy()
    return self.__constructor__(query_compiler=self._query_compiler.head(n))