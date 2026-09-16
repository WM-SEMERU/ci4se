def all_address_target_pairs(cls, address_families):
    addr_tgt_pairs = []
    for af in address_families:
        addr_tgt_pairs.extend(af.addressables.items())
    return addr_tgt_pairs