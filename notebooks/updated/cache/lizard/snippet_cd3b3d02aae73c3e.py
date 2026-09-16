def strip_masked(fasta, min_len, print_masked):
    for seq in parse_fasta(fasta):
        nm, masked = parse_masked(seq, min_len)
        nm = ['%s removed_masked >=%s' % (seq[0], min_len), ''.join(nm)]
        yield [0, nm]
        if print_masked is True:
            for i, m in enumerate([i for i in masked if i != []], 1):
                m = ['%s insertion:%s' % (seq[0], i), ''.join(m)]
                yield [1, m]