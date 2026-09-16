def make_column_suffixes(self):
    if self.column_suffixes:
        return self.column_suffixes
    if len(self.columns) == 0:
        return ()
    elif len(self.columns) == 1:
        if self.formatters:
            return '_raw',
        else:
            return '',
    elif len(self.columns) == 2:
        if self.formatters:
            return '_id', '_raw'
        else:
            return '_id', ''
    else:
        raise BadIngredient(
            'column_suffixes must be supplied if there is more than one column'
            )