def getNucleotideCodon(sequence, x1):
    if x1 < 0 or x1 >= len(sequence):
        return None
    p = x1 % 3
    if p == 0:
        return sequence[x1:x1 + 3], 0
    elif p == 1:
        return sequence[x1 - 1:x1 + 2], 1
    elif p == 2:
        return sequence[x1 - 2:x1 + 1], 2