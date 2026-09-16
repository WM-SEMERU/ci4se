def round(self, decimals=0, *args, **kwargs):
    return self.__constructor__(query_compiler=self._query_compiler.round(
        decimals=decimals, **kwargs))