def save_features_and_arrays(features, arrays, prefix, compressed=False,
    link_features=False, overwrite=False):
    if link_features:
        if isinstance(features, pybedtools.BedTool):
            assert isinstance(features.fn, basestring)
            features_filename = features.fn
        else:
            assert isinstance(features, basestring)
            features_filename = features
        if overwrite:
            force_flag = '-f'
        else:
            force_flag = ''
        cmds = ['ln', '-s', force_flag, os.path.abspath(features_filename),
            prefix + '.features']
        os.system(' '.join(cmds))
    else:
        pybedtools.BedTool(features).saveas(prefix + '.features')
    if compressed:
        np.savez_compressed(prefix, **arrays)
    else:
        np.savez(prefix, **arrays)