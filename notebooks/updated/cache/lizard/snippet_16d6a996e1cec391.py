def load_file_or_directory(path):
    assert os.path.exists(path), '{0} does not exist!'.format(path)
    absolute_path = os.path.abspath(path)
    if not os.path.isdir(path):
        yield absolute_path
    else:
        for root, dirs, file_paths in os.walk(path):
            for file_path in file_paths:
                yield os.path.join(root, file_path)