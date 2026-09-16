def create(self, columns=None, type_map=None, overwrite=False):
    if self.count_bytes > 0:
        if overwrite:
            self.remove()
        else:
            raise Exception("File exists already at '%s'" % self)
    if columns is None:
        self.touch()
    else:
        self.add_table(self.main_table, columns=columns, type_map=type_map)