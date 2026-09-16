def _clean_regions(items, region):
    variant_regions = bedutils.population_variant_regions(items, merged=True)
    with utils.tmpfile() as tx_out_file:
        target = subset_variant_regions(variant_regions, region,
            tx_out_file, items)
        if target:
            if isinstance(target, six.string_types) and os.path.isfile(target):
                target = _load_regions(target)
            else:
                target = [target]
            return target