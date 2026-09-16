def get_split_datasets(self, X, y=None, **fit_params):
    dataset = self.get_dataset(X, y)
    if self.train_split:
        dataset_train, dataset_valid = self.train_split(dataset, y, **
            fit_params)
    else:
        dataset_train, dataset_valid = dataset, None
    return dataset_train, dataset_valid