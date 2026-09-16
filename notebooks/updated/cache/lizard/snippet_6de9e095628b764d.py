def initializeColumns(self):
    tableType = self.tableType()
    if not tableType:
        return
    elif self._columnsInitialized or self.columnOf(0) != '1':
        self.assignOrderNames()
        return
    tschema = tableType.schema()
    columns = tschema.columns()
    names = [col.displayName() for col in columns if not col.isPrivate()]
    self.setColumns(sorted(names))
    self.assignOrderNames()
    self.resizeToContents()