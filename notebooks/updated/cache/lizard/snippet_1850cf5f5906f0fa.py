def set_scalar(self, indexer, value):
    try:
        value_code = self.reverse_categories[value]
    except KeyError:
        raise ValueError('%r is not in LabelArray categories.' % value)
    self.as_int_array()[indexer] = value_code