def fastaAlignmentRead(fasta, mapFn=lambda x: x, l=None):
    if l is None:
        l = _getMultiFastaOffsets(fasta)
    else:
        l = l[:]
    seqNo = len(l)
    for i in xrange(0, seqNo):
        j = open(fasta, 'r')
        j.seek(l[i])
        l[i] = j
    column = [sys.maxint] * seqNo
    if seqNo != 0:
        while True:
            for j in xrange(0, seqNo):
                i = l[j].read(1)
                while i == '\n':
                    i = l[j].read(1)
                column[j] = i
            if column[0] == '>' or column[0] == '':
                for j in xrange(1, seqNo):
                    assert column[j] == '>' or column[j] == ''
                break
            for j in xrange(1, seqNo):
                assert column[j] != '>' and column[j] != ''
                column[j] = mapFn(column[j])
            yield column[:]
    for i in l:
        i.close()