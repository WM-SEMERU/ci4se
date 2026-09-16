def read_single(path, encoding='UTF-8'):
    assert isinstance(path, (str, _oldstr))
    data = []
    with smart_open_read(path, mode='rb', try_gzip=True) as fh:
        reader = csv.reader(fh, dialect='excel-tab', encoding=encoding)
        for l in reader:
            data.append(l[0])
    return data