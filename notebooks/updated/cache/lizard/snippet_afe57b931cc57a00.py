def vcfunpackinfo(table, *keys):
    result = etl.unpackdict(table, 'INFO', keys=keys)
    return result