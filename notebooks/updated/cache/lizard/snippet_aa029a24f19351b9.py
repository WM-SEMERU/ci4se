def search(self, filters):
    records = self.__model__.search(self.__five9__, filters)
    return self.__class__(self.__five9__, self.__model__, records)