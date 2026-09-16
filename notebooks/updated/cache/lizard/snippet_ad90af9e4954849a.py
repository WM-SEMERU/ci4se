def normalize_alleles_left(ref, start, stop, alleles, bound, ref_step,
    shuffle=True):
    normalized_alleles = namedtuple('shuffled_alleles', 'start stop alleles')
    if len(alleles) < 2:
        return normalized_alleles(start, stop, alleles)
    trimmed, alleles = trim_common_suffixes(alleles)
    stop -= trimmed
    trimmed, alleles = trim_common_prefixes(alleles)
    start += trimmed
    while shuffle and '' in alleles and start > bound:
        step = min(ref_step, start - bound)
        r = ref[start - step:start].upper()
        new_alleles = [(r + a) for a in alleles]
        trimmed, new_alleles = trim_common_suffixes(new_alleles)
        if not trimmed:
            break
        start -= trimmed
        stop -= trimmed
        if trimmed == step:
            alleles = new_alleles
        else:
            left = step - trimmed
            alleles = [a[left:] for a in new_alleles]
            break
    return normalized_alleles(start, stop, tuple(alleles))