def fastaWrite(fileHandleOrFile, name, seq, mode='w'):
    fileHandle = _getFileHandle(fileHandleOrFile, mode)
    valid_chars = {x for x in string.ascii_letters + '-'}
    try:
        assert any([isinstance(seq, unicode), isinstance(seq, str)])
    except AssertionError:
        raise RuntimeError('Sequence is not unicode or string')
    try:
        assert all(x in valid_chars for x in seq)
    except AssertionError:
        bad_chars = {x for x in seq if x not in valid_chars}
        raise RuntimeError(
            'Invalid FASTA character(s) see in fasta sequence: {}'.format(
            bad_chars))
    fileHandle.write('>%s\n' % name)
    chunkSize = 100
    for i in xrange(0, len(seq), chunkSize):
        fileHandle.write('%s\n' % seq[i:i + chunkSize])
    if isinstance(fileHandleOrFile, ''.__class__):
        fileHandle.close()