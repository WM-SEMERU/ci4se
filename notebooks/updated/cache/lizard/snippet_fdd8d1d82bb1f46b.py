def unicode_decode(data, encoding_list):
    assert encoding_list, 'encodings must not be empty.'
    xs = distinct(encoding_list if isinstance(encoding_list, list) else [
        encoding_list])
    first_exp = None
    for i, encoding in enumerate(xs):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError as e:
            if i == 0:
                first_exp = e
    raise first_exp