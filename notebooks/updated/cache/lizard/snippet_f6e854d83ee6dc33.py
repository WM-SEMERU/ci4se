def check_file_type(files):
    all_are_fasta = True
    all_are_reads = True
    all_are_empty = True
    if sys.version_info < (3, 0):
        if isinstance(files, (str, unicode)):
            files = [files]
    elif isinstance(files, str):
        files = [files]
    for file_ in files:
        debug.log('Checking file type: %s' % file_)
        if os.stat(file_).st_size == 0:
            continue
        else:
            all_are_empty = False
        with open_(file_) as f:
            fc = f.readline()[0]
            if fc != '@':
                all_are_reads = False
            if fc != '>':
                all_are_fasta = False
    if all_are_empty:
        return 'empty'
    elif all_are_fasta:
        return 'fasta'
    elif all_are_reads:
        return 'fastq'
    else:
        return 'other'