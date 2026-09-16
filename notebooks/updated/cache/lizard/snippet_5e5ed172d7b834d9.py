def __parse_aliases_line(self, raw_alias, raw_username):
    alias = self.__encode(raw_alias)
    username = self.__encode(raw_username)
    return alias, username