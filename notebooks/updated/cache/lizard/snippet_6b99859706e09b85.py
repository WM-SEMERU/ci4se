def split_sequence(seq, n):
    tokens = []
    while seq:
        tokens.append(seq[:n])
        seq = seq[n:]
    return tokens