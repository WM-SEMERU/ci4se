def merge(self, datasets=None, separate_datasets=False):
    self.logger.info('merging')
    if separate_datasets:
        warnings.warn(
            'The option seperate_datasets=True isnot implemented yet. Performing merging, butneglecting the option.'
            )
    else:
        if datasets is None:
            datasets = list(range(len(self.datasets)))
        first = True
        for dataset_number in datasets:
            if first:
                dataset = self.datasets[dataset_number]
                first = False
            else:
                dataset = self._append(dataset, self.datasets[dataset_number])
                for raw_data_file, file_size in zip(self.datasets[
                    dataset_number].raw_data_files, self.datasets[
                    dataset_number].raw_data_files_length):
                    dataset.raw_data_files.append(raw_data_file)
                    dataset.raw_data_files_length.append(file_size)
        self.datasets = [dataset]
        self.number_of_datasets = 1
    return self