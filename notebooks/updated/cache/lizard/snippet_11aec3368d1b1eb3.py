def _find_model(self, constructor, table_name, constraints=None, *, columns
    =None, order_by=None):
    data = self.find(table_name, constraints, columns=columns, order_by=
        order_by)
    return constructor(data) if data else None