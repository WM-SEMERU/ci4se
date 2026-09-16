def eval(self, data, name, feval=None):
    if not isinstance(data, Dataset):
        raise TypeError('Can only eval for Dataset instance')
    data_idx = -1
    if data is self.train_set:
        data_idx = 0
    else:
        for i in range_(len(self.valid_sets)):
            if data is self.valid_sets[i]:
                data_idx = i + 1
                break
    if data_idx == -1:
        self.add_valid(data, name)
        data_idx = self.__num_dataset - 1
    return self.__inner_eval(name, data_idx, feval)