def mappings(self):
    return self.hg.mappings[np.unique(np.where(self.__matrix == 1)[1])]