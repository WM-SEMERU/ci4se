def coding_sequence(rna):
    if isinstance(rna, coral.DNA):
        rna = transcribe(rna)
    codons_left = len(rna) // 3
    start_codon = coral.RNA('aug')
    stop_codons = [coral.RNA('uag'), coral.RNA('uga'), coral.RNA('uaa')]
    start = None
    stop = None
    valid = [None, None]
    index = 0
    while codons_left:
        codon = rna[index:index + 3]
        if valid[0] is None:
            if codon in start_codon:
                start = index
                valid[0] = True
        elif codon in stop_codons:
            stop = index + 3
            valid[1] = True
            break
        index += 3
        codons_left -= 1
    if valid[0] is None:
        raise ValueError('Sequence has no start codon.')
    elif stop is None:
        raise ValueError('Sequence has no stop codon.')
    coding_rna = rna[start:stop]
    return coding_rna