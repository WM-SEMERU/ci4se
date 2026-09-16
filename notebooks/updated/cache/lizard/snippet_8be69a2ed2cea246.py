def in_same_dir(as_file, target_file):
    return os.path.abspath(os.path.join(os.path.dirname(as_file), target_file))