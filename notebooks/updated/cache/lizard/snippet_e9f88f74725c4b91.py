def add_column(self, name, type_name, options=None):
    column = Column(name, type_name, options)
    self._add_column(column)
    return column