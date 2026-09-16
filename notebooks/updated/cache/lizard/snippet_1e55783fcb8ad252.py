def _dir_size(directory):
    size = 0
    for elem in tf_v1.gfile.ListDirectory(directory):
        elem_full_path = os.path.join(directory, elem)
        stat = tf_v1.gfile.Stat(elem_full_path)
        size += _dir_size(elem_full_path) if stat.is_directory else stat.length
    return size