def _create_options(self, items):
    return OrderedDict(map(lambda x: (x.name, x), coerce_to_list(items,
        self.preprocess)))