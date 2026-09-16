def roles(self):
    if not self.__roles:
        self.__roles = Roles(self.__connection)
    return self.__roles