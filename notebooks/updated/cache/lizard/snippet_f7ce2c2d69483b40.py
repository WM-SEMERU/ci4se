def read_dimvalue(self, dimname, path='/', default=NO_DEFAULT):
    try:
        dim = self._read_dimensions(dimname, path=path)[0]
        return len(dim)
    except self.Error:
        if default is NO_DEFAULT:
            raise
        return default