def split_array_as_list(self, values):
    values = np.asarray(values)
    values = values[self.index.sorter]
    return np.split(values, self.index.slices[1:-1], axis=0)