def isscalar(cls, dataset, dim):
    if not dataset.data:
        return True
    ds = cls._inner_dataset_template(dataset)
    isscalar = []
    for d in dataset.data:
        ds.data = d
        isscalar.append(ds.interface.isscalar(ds, dim))
    return all(isscalar)