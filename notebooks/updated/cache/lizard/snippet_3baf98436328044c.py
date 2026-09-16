def fetcher_with_object(cls, parent_object, relationship='child'):
    fetcher = cls()
    fetcher.parent_object = parent_object
    fetcher.relationship = relationship
    rest_name = cls.managed_object_rest_name()
    parent_object.register_fetcher(fetcher, rest_name)
    return fetcher