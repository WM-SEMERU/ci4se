def variant_to_canonical_string(obj):
    acc = [DG_ALL_DESCRIPTORS.canonical_value(p) for p in variant_to_list(obj)]
    acc = sorted([a for a in acc if a is not None])
    return ' '.join(acc)