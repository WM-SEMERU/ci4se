def round(self, decimals=0):
    return self.__class__(np.round(self, decimals=decimals))