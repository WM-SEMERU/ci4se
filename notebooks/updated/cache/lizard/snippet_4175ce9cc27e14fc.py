def make_gene_info_df(fn):
    import itertools as it
    import HTSeq
    gff_iter = it.islice(HTSeq.GFF_Reader(fn), None)
    convD = dict()
    eof = False
    while not eof:
        try:
            entry = gff_iter.next()
            if entry.type == 'gene':
                convD[entry.attr['gene_id']] = [entry.attr['gene_name'],
                    entry.attr['gene_type'], entry.iv.chrom, entry.iv.start,
                    entry.iv.end, entry.iv.strand, entry.attr['gene_status'
                    ], entry.source, entry.attr['level']]
        except StopIteration:
            eof = True
    ind = ['gene_name', 'gene_type', 'chrom', 'start', 'end', 'strand',
        'gene_status', 'source', 'level']
    df = pd.DataFrame(convD, index=ind).T
    df.index.name = 'gene_id'
    return df