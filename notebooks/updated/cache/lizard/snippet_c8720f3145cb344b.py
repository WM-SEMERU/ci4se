def aa3_to_aa1(seq):
    if seq is None:
        return None
    return ''.join(aa3_to_aa1_lut[aa3] for aa3 in [seq[i:i + 3] for i in
        range(0, len(seq), 3)])