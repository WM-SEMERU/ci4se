def to_archivable_dict(self, dialect, use_dirty=True):
    return {cn: utils.get_column_attribute(self, c, use_dirty=use_dirty,
        dialect=dialect) for c, cn in utils.get_column_keys_and_names(self) if
        c not in self.ignore_columns}