def findPrimer(primer, seq):
    offsets = []
    seq = seq.upper()
    primer = primer.upper()
    primerLen = len(primer)
    discarded = 0
    offset = seq.find(primer)
    while offset > -1:
        offsets.append(discarded + offset)
        seq = seq[offset + primerLen:]
        discarded += offset + primerLen
        offset = seq.find(primer)
    return offsets