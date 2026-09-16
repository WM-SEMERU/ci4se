def list(self):
    schema = ImportSchema()
    resp = self.service.list(self.base)
    return self.service.decode(schema, resp, many=True)