def remove_lcr_regions(orig_bed, items):
    lcr_bed = tz.get_in(['genome_resources', 'variation', 'lcr'], items[0])
    if lcr_bed and os.path.exists(lcr_bed) and 'lcr' in get_exclude_regions(
        items):
        return _remove_regions(orig_bed, [lcr_bed], 'nolcr', items[0])
    else:
        return orig_bed