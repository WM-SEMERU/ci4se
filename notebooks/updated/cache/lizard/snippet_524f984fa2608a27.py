def _read_file(name, encoding='utf-8'):
    with codecs.open(name, encoding=encoding) as f:
        return f.read()