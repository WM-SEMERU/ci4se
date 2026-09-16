def _loadColumns(self, record, columnName, value):
    value = unwrapNone(value)
    item = self.findRecordItem(record)
    if item:
        item.updateColumnValue(record.schema().column(columnName), value,
            self.column(columnName))