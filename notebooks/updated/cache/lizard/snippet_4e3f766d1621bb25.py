def check_dataset(dataset):
    if isinstance(dataset, numpy.ndarray) and not len(dataset.shape) == 4:
        check_dataset_shape(dataset)
        check_dataset_range(dataset)
    else:
        for i, d in enumerate(dataset):
            if not isinstance(d, numpy.ndarray):
                raise ValueError(
                    'Requires a NumPy array (rgb x rows x cols) with integer values in the range [0, 255].'
                    )
            try:
                check_dataset_shape(d)
                check_dataset_range(d)
            except ValueError as err:
                raise ValueError('{}\nAt position {} in the list of arrays.'
                    .format(err, i))