def codon2weight(self, codon):
    length = len(codon)
    retval = int(codon)
    return retval / 10 ** (length - 1) - 5.0