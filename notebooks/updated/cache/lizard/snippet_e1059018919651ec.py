def close(self):
    files = self.__dict__.get('files')
    for key, value in iter_multi_items(files or ()):
        value.close()