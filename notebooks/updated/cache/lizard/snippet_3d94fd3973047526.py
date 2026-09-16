def fromgff3(filename, region=None):
    if region is None:
        table = etl.fromtsv(filename)
    else:
        table = etl.fromtabix(filename, region=region)
    return table.pushheader(GFF3_HEADER).skipcomments('#').rowlenselect(9
        ).convert('attributes', gff3_parse_attributes).convert(('start',
        'end'), int)