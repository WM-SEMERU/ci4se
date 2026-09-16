def update_many(self, table, columns, values, where_col, where_index):
    for row in values:
        wi = row.pop(where_index)
        self.update(table, columns, row, (where_col, wi))