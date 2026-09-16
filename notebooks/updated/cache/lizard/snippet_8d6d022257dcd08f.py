def updateColumnValue(self, column, value, index=None):
    if index is None:
        index = self.treeWidget().column(column.name())
    if type(value) == datetime.date:
        self.setData(index, Qt.EditRole, wrapVariant(value))
    elif type(value) == datetime.time:
        self.setData(index, Qt.EditRole, wrapVariant(value))
    elif type(value) == datetime.datetime:
        self.setData(index, Qt.EditRole, wrapVariant(value))
    elif type(value) in (float, int):
        if column.enum():
            self.setText(index, column.enum().displayText(value))
        else:
            self.setData(index, Qt.EditRole, wrapVariant(value))
    elif value is not None:
        self.setText(index, nativestring(value))
    else:
        self.setText(index, '')
    self.setSortData(index, value)
    try:
        mapper = self.treeWidget().columnMappers().get(column.columnName())
    except AttributeError:
        mapper = None
    if mapper is None:
        form = column.stringFormat()
        if form:
            mapper = form.format
    if mapper:
        self.setText(index, mapper(value))