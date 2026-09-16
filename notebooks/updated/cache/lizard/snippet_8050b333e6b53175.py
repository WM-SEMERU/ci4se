def updateRecordValues(self):
    record = self.record()
    if not record:
        return
    tree = self.treeWidget()
    if not isinstance(tree, XTreeWidget):
        return
    for column in record.schema().columns():
        c = tree.column(column.displayName())
        if c == -1:
            continue
        elif tree.isColumnHidden(c):
            continue
        else:
            val = record.recordValue(column.name())
            self.updateColumnValue(column, val, c)
    if not record.isRecord():
        self.addRecordState(XOrbRecordItem.State.New)
    elif record.isModified():
        self.addRecordState(XOrbRecordItem.State.Modified)