def drop_table(self, model, cascade=True):
    del self.orm[model._meta.table_name]
    self.ops.append(self.migrator.drop_table(model, cascade))