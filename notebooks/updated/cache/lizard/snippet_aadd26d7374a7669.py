def sam_pair_to_insert(s1, s2):
    if (s1.is_unmapped or s2.is_unmapped or s1.tid != s2.tid or s1.
        is_reverse == s2.is_reverse):
        return None
    if s1.is_reverse:
        end = s1.reference_end - 1
        start = s2.reference_start
    else:
        end = s2.reference_end - 1
        start = s1.reference_start
    if start < end:
        return end - start + 1
    else:
        return None