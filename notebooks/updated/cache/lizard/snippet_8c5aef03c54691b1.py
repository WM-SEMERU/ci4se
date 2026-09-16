def unpack_scalar(cls, dataset, data):
    if np.isscalar(data) or len(data) != 1:
        return data
    key = list(data.keys())[0]
    if len(data[key]) == 1 and key in dataset.vdims:
        return data[key][0]