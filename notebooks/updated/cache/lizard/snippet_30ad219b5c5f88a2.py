def compress_gz(fname):
    import shutil
    import gzip
    comp_fname = fname + '.gz'
    with codecs.open(fname, 'rb') as f_in, gzip.open(comp_fname, 'wb'
        ) as f_out:
        shutil.copyfileobj(f_in, f_out)
    os.remove(fname)
    return comp_fname