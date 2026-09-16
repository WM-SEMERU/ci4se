def open_as_needed(filename):
    if hasattr(filename, 'read'):
        return filename
    if filename.endswith('.bz2'):
        return bz2.BZ2File(filename, 'rb')
    elif filename.endswith('.gz'):
        return gzip.GzipFile(filename, 'rb')
    else:
        return open(filename, 'rb')