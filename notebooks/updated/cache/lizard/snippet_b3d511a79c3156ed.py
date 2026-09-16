def convert(self, key, value):
    if key not in self._dtypes:
        self.read_types()
        if key not in self._dtypes:
            name = utils.name(value)
            serializer = utils.serializer(name)
            deserializer = utils.deserializer(name)
            self._dtypes[key] = name, serializer, deserializer
            with self.db:
                self.db.execute(
                    'replace into value_types (key, value_type) values (?, ?)',
                    (key, name))
    return self._dtypes[key][1](value)