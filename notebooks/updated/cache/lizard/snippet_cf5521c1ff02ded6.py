def del_sample(self, sample_id):
    if sample_id not in self.__data:
        warnings.warn(
            'Sample to delete not found in the dataset - nothing to do.')
    else:
        self.__data.pop(sample_id)
        self.__classes.pop(sample_id)
        self.__labels.pop(sample_id)
        print('{} removed.'.format(sample_id))