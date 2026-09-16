def get(self, default=None):
    if not self.__cancelled and self.__state == Job.SUCCESS:
        return self.__result
    else:
        return default