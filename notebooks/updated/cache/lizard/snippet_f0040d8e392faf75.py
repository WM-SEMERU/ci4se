def dict_load(self, ns_dict):
    for prefix, uri in ns_dict.items():
        self.bind(prefix, uri, override=False, calc=False)
    self.__make_dicts__