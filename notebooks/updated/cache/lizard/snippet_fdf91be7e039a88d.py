def setColumns(self, columns):
    self.__columns = {}
    for name, column in columns.items():
        self.__columns[name] = column
        column.setSchema(self)