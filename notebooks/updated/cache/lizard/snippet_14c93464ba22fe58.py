def ndim(self):
    try:
        return self.__ndim
    except AttributeError:
        ndim = len(self.coord_vectors)
        self.__ndim = ndim
        return ndim