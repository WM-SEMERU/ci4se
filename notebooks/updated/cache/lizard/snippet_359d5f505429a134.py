def load_store(cls, store, decoder=None):
    variables, attributes = store.load()
    if decoder:
        variables, attributes = decoder(variables, attributes)
    obj = cls(variables, attrs=attributes)
    obj._file_obj = store
    return obj