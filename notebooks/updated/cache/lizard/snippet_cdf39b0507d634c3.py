def normalizeHSP(hsp, queryLen, diamondTask):
    queryGaps, subjectGaps = countGaps(hsp['btop'])
    queryStart = hsp['query_start'] - 1
    queryEnd = hsp['query_end']
    subjectStart = hsp['sbjct_start'] - 1
    subjectEnd = hsp['sbjct_end']
    queryReversed = hsp['frame'] < 0
    if queryStart >= queryEnd:
        if diamondTask == 'blastx' and queryReversed:
            queryStart = queryLen - (queryStart + 1)
            queryEnd = queryLen - (queryEnd - 1)
        else:
            _debugPrint(hsp, queryLen, locals(), 'queryStart >= queryEnd')
    if diamondTask == 'blastx':
        initiallyIgnored = abs(hsp['frame']) - 1
        queryLen = (queryLen - initiallyIgnored) // 3
        queryStart = (queryStart - initiallyIgnored) // 3
        queryEnd = (queryEnd - initiallyIgnored) // 3
    unmatchedQueryLeft = queryStart
    queryStartInSubject = subjectStart - unmatchedQueryLeft
    queryEndInSubject = queryStartInSubject + queryLen + queryGaps
    _sanityCheck(subjectStart, subjectEnd, queryStart, queryEnd,
        queryStartInSubject, queryEndInSubject, hsp, queryLen, subjectGaps,
        queryGaps, locals())
    return {'readStart': queryStart, 'readEnd': queryEnd,
        'readStartInSubject': queryStartInSubject, 'readEndInSubject':
        queryEndInSubject, 'subjectStart': subjectStart, 'subjectEnd':
        subjectEnd}