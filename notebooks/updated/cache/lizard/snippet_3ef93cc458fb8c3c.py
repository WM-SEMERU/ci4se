def search_on(self, *fields, **query):
    clone = copy.deepcopy(self)
    clone.adapter.search_on(*fields, **query)
    return clone