def garbage_collect_exports(export_dir_base, exports_to_keep):
    if exports_to_keep is None:
        return
    version_paths = []
    for filename in tf_v1.gfile.ListDirectory(export_dir_base):
        path = os.path.join(tf.compat.as_bytes(export_dir_base), tf.compat.
            as_bytes(filename))
        if len(filename) == 10 and filename.isdigit():
            version_paths.append((int(filename), path))
    oldest_version_path = sorted(version_paths)[:-exports_to_keep]
    for _, path in oldest_version_path:
        try:
            tf_v1.gfile.DeleteRecursively(path)
        except tf.errors.NotFoundError as e:
            logging.warn('Can not delete %s recursively: %s', path, e)