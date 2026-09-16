def _get_case_file_paths(tmp_dir, case, training_fraction=0.95):
    paths = tf.gfile.Glob('%s/*.jpg' % tmp_dir)
    if not paths:
        raise ValueError('Search of tmp_dir (%s) ' % tmp_dir,
            'for subimage paths yielded an empty list, ',
            "can't proceed with returning training/eval split.")
    split_index = int(math.floor(len(paths) * training_fraction))
    if split_index >= len(paths):
        raise ValueError(
            'For a path list of size %s and a training_fraction of %s the resulting split_index of the paths list, %s, would leave no elements for the eval condition.'
             % (len(paths), training_fraction, split_index))
    if case:
        return paths[:split_index]
    else:
        return paths[split_index:]