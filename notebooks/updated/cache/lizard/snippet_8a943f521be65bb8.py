def read_index(fn):
    index = None
    with open(fn, 'rb') as i_file:
        if i_file.read(len(_CHECK_STRING)) != _CHECK_STRING:
            raise ValueError('{}: not a valid index file'.format(fn))
        index = pd.read_csv(io.StringIO(zlib.decompress(i_file.read()).
            decode(encoding='utf-8')))
    return index