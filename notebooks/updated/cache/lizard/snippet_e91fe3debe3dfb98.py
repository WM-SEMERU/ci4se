def seqs_from_fastacmd(acc_list, blast_db, is_protein=True):
    fasta_cmd_res = fasta_cmd_get_seqs(acc_list, blast_db=blast_db,
        is_protein=is_protein)
    recs = FastaCmdFinder(fasta_cmd_res['StdOut'])
    result = {}
    for rec in recs:
        try:
            result[rec[0][1:].strip()] = ''.join(map(strip, rec[1:]))
        except IndexError:
            pass
    fasta_cmd_res.cleanUp()
    return result