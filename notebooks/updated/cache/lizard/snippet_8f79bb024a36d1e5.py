def read_file(fname):
    assert os.path.exists(fname
        ), "\n--%s-- Warning: File `%s' does not exist. . ." % (current_time
        (), fname)
    with open(fname, 'rb') as fp:
        return fp.read().decode('utf-8')