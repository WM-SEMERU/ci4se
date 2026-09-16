def analyze_insertions(fa, threads=6):
    safe, sequences, id2name, names, insertions = analyze_fa(fa)
    seqs = seq_info(names, id2name, insertions, sequences)
    seqs, orfs = find_orfs(safe, seqs)
    seqs = find_introns(safe, seqs, sequences, threads)
    seqs = seqs2bool(seqs)
    seqs = annotate_orfs(orfs, seqs, threads)
    return seqs, id2name