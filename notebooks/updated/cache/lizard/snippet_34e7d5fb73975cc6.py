def fields(self):
    return {k: getattr(self, k, None) for k in self.schema.fields}