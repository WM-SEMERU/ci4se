def problem_with_codon(codon_index, codon_list, bad_seqs):
    base_1 = 3 * codon_index
    base_3 = 3 * codon_index + 2
    gene_seq = ''.join(codon_list)
    for bad_seq in bad_seqs:
        problem = bad_seq.search(gene_seq)
        if problem and problem.start() < base_3 and problem.end() > base_1:
            return True
    return False