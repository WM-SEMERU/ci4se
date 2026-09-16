def search(cls, five9, filters):
    return cls._name_search(five9.configuration.getDispositions, filters)