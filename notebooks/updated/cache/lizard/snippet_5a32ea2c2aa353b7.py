def add_not_null(self, model, *names):
    for name in names:
        field = model._meta.fields[name]
        field.null = False
        self.ops.append(self.migrator.add_not_null(model._meta.table_name,
            field.column_name))
    return model