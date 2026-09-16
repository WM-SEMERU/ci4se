def hasColumn(self, column, recurse=True, flags=0):
    return column in self.columns(recurse=recurse, flags=flags)