def split_data(data, subset, splits):
    return dict([(k, data[k][splits[subset]]) for k in data])