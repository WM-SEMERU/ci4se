def load_from_array(self, keys, data_array):
    if len(keys) != np.shape(data_array)[1]:
        raise ValueError('Key list does not match shape of array!')
    for i, key in enumerate(keys):
        if key in self.INT_ATTRIBUTE_LIST:
            self.data[key] = data_array[:, (i)].astype(int)
        else:
            self.data[key] = data_array[:, (i)]
        if key not in self.TOTAL_ATTRIBUTE_LIST:
            print('Key %s not a recognised catalogue attribute' % key)
    self.update_end_year()