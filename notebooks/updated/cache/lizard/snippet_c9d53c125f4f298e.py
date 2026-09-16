def read_fastq(filename):
    if not filename:
        return itertools.cycle((None,))
    if filename == '-':
        filename_fh = sys.stdin
    elif filename.endswith('gz'):
        if is_python3:
            filename_fh = gzip.open(filename, mode='rt')
        else:
            filename_fh = BufferedReader(gzip.open(filename, mode='rt'))
    else:
        filename_fh = open(filename)
    return stream_fastq(filename_fh)