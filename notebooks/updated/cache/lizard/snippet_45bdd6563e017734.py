def create_index(self, keys, **kwargs):
    keys = helpers._index_list(keys)
    name = kwargs.setdefault('name', helpers._gen_index_name(keys))
    self.__create_index(keys, kwargs)
    return name