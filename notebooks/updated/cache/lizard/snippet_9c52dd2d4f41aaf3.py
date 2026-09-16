def import_from_nhmmer_table(hmmout_path):
    res = HMMSearchResult()
    res.fields = [SequenceSearchResult.QUERY_ID_FIELD, SequenceSearchResult
        .HMM_NAME_FIELD, SequenceSearchResult.ALIGNMENT_LENGTH_FIELD,
        SequenceSearchResult.QUERY_FROM_FIELD, SequenceSearchResult.
        QUERY_TO_FIELD, SequenceSearchResult.HIT_FROM_FIELD,
        SequenceSearchResult.HIT_TO_FIELD, SequenceSearchResult.
        ALIGNMENT_BIT_SCORE, SequenceSearchResult.ALIGNMENT_DIRECTION]
    for row in [x.rstrip().split() for x in open(hmmout_path) if not x.
        startswith('#')]:
        alifrom = int(row[6])
        alito = int(row[7])
        aln_length = (alito - alifrom if alito - alifrom > 0 else alifrom -
            alito)
        res.results.append([row[0], row[2], aln_length, int(row[4]), int(
            row[5]), alifrom, alito, row[13], alito > alifrom])
    return res