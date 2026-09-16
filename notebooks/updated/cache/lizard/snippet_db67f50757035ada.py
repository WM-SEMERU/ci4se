def schema(self):
    if not self._schema:
        try:
            self._load_info()
            self._schema = _schema.Schema(self._info['schema']['fields'])
        except KeyError:
            raise Exception('Unexpected table response: missing schema')
    return self._schema