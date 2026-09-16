def data(self):
    if self.sort:
        xs = sorted(self.dataset, key=self.sort_key)
    elif self.shuffle:
        xs = [self.dataset[i] for i in self.random_shuffler(range(len(self.
            dataset)))]
    else:
        xs = self.dataset
    return xs