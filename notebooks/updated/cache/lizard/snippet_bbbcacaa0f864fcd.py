def set_index(self, schema, name, fields, **index_options):
    with self.transaction(**index_options) as connection:
        index_options['connection'] = connection
        self._set_index(schema, name, fields, **index_options)
    return True