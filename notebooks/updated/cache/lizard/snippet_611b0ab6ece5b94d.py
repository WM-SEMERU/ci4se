def get_rRNA(gtf):
    rRNA_biotypes = ['rRNA', 'Mt_rRNA', 'tRNA', 'MT_tRNA']
    features = set()
    with open_gzipsafe(gtf) as in_handle:
        for line in in_handle:
            if not 'gene_id' in line or not 'transcript_id' in line:
                continue
            if any(x in line for x in rRNA_biotypes):
                geneid = line.split('gene_id')[1].split(' ')[1]
                geneid = _strip_non_alphanumeric(geneid)
                geneid = _strip_feature_version(geneid)
                txid = line.split('transcript_id')[1].split(' ')[1]
                txid = _strip_non_alphanumeric(txid)
                txid = _strip_feature_version(txid)
                features.add((geneid, txid))
    return features