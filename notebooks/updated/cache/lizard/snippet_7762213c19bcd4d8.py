def guess_path_encoding(file_path, default=DEFAULT_ENCODING):
    with io.open(file_path, 'rb') as fh:
        return guess_file_encoding(fh, default=default)