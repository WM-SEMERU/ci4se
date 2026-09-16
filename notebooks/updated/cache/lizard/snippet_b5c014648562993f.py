def load_features_and_arrays(prefix, mmap_mode='r'):
    features = pybedtools.BedTool(prefix + '.features')
    arrays = np.load(prefix + '.npz', mmap_mode=mmap_mode)
    return features, arrays