def normalize(self):
    self.__v = self.__v - np.amin(self.__v)
    self.__v = self.__v / np.amax(self.__v)