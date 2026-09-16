def _sam_to_soft_clipped(self, sam):
    if sam.is_unmapped:
        raise Error('Cannot get soft clip info from an unmapped read')
    if sam.cigar is None or len(sam.cigar) == 0:
        return False, False
    return sam.cigar[0][0] == 4, sam.cigar[-1][0] == 4