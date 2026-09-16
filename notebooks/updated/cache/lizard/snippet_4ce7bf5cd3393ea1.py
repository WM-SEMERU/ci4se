def read_file(path):
    if os.path.isabs(path):
        with wrap_file_exceptions():
            with open(path, 'rb') as stream:
                return stream.read()
    with wrap_file_exceptions():
        stream = ca_storage.open(path)
    try:
        return stream.read()
    finally:
        stream.close()