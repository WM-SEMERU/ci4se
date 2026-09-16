def drop(self, labels, dim=None):
    if utils.is_scalar(labels):
        labels = [labels]
    if dim is None:
        return self._drop_vars(labels)
    else:
        try:
            index = self.indexes[dim]
        except KeyError:
            raise ValueError('dimension %r does not have coordinate labels' %
                dim)
        new_index = index.drop(labels)
        return self.loc[{dim: new_index}]