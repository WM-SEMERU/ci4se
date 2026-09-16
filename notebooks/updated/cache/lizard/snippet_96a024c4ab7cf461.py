def is_full_overlap(self1):
    if len(self1.overs) == 0:
        return False
    if len(self1.dif1) > 0:
        if max(self1.dif1) != 1 or max(self1.dif2) != 1:
            return False
    if self1.start1 and self1.end1 and self1.start2 and self1.end2:
        return True
    return False