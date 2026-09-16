def addFilter(self, field, value):
    if '<' not in value or '>' not in value or '..' not in value:
        value = ':' + value
    if self.__urlFilters:
        self.__urlFilters += '+' + field + str(quote(value))
    else:
        self.__urlFilters += field + str(quote(value))