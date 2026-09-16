def max_insertion(seqs, gene, domain):
    seqs = [i[2] for i in list(seqs.values()) if i[2] != [] and i[0] ==
        gene and i[1] == domain]
    lengths = []
    for seq in seqs:
        for ins in seq:
            lengths.append(int(ins[2]))
    if lengths == []:
        return 100
    return max(lengths)