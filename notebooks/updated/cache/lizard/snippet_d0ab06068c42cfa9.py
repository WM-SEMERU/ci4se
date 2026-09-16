def split_path(path):
    path = path.split(0, 1)[0]
    values = path.dimension_values(0)
    splits = np.concatenate([[0], np.where(np.isnan(values))[0] + 1, [None]])
    subpaths = []
    data = PandasInterface.as_dframe(path) if pd else path.array()
    for i in range(len(splits) - 1):
        end = splits[i + 1]
        slc = slice(splits[i], None if end is None else end - 1)
        subpath = data.iloc[slc] if pd else data[slc]
        if len(subpath):
            subpaths.append(subpath)
    return subpaths