def assessOligo(seq):
    hairpin_out = calcHairpin(seq)
    homodimer_out = calcHomodimer(seq)
    return hairpin_out, homodimer_out