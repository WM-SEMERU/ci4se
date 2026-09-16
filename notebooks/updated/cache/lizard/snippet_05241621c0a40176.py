def global_set(self, key, value):
    key, value = map(self.pack, (key, value))
    try:
        return self.sql('global_insert', key, value)
    except IntegrityError:
        return self.sql('global_update', value, key)