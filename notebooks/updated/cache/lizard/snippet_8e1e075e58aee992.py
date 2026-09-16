def read(cls, filename, offset=None, encoding='iso-8859-1'):
    with fileutil.opened(filename, 'rb') as file:
        if offset is None:
            file.seek(-128, 2)
        else:
            file.seek(offset)
        data = file.read(128)
        return cls.decode(data, encoding=encoding)