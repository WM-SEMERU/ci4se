def add_row(self, obj):
    row = {}
    for column in self.headers:
        value = ''
        if '__col__' in column:
            if isinstance(column['__col__'], ColumnProperty):
                value = self._get_column_cell_val(obj, column)
            elif isinstance(column['__col__'], RelationshipProperty):
                value = self._get_relationship_cell_val(obj, column)
        row[column['name']] = value
    self._datas.append(self.format_row(row))