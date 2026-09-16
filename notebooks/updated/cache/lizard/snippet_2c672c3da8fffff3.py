def _longestCommonPrefix(seq1, seq2, start1=0, start2=0):
    len1 = len(seq1) - start1
    len2 = len(seq2) - start2
    if len1 < len2:
        seq1, seq2 = seq2, seq1
        start1, start2 = start2, start1
        len1, len2 = len2, len1
    if len2 == 0:
        return 0
    i = 0
    pos2 = start2
    for i in range(min(len1, len2)):
        if seq1[start1 + i] != seq2[start2 + i]:
            return i
    return i + 1