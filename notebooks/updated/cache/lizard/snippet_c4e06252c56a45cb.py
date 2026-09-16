def should_filter(items):
    return vcfutils.get_paired(items) is not None and any('damage_filter' in
        dd.get_tools_on(d) for d in items)