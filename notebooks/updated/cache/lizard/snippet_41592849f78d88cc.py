def uniquify_by(self, column, chooser=None, aggregate='MAX'):
    self.group_by.append(column)
    if chooser:
        i = self.columns.index(chooser)
        self.columns[i] = '{0}({1})'.format(aggregate, self.columns[i])