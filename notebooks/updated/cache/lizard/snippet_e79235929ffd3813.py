def DataProcessorsPost(self, parameters):
    if self.__SenseApiCall__('/dataprocessors.json', 'POST', parameters=
        parameters):
        return True
    else:
        self.__error__ = 'api call unsuccessful'
        return False