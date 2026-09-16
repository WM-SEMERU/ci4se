def export_asset_risk_csv(ekey, dstore):
    writer = writers.CsvWriter(fmt=writers.FIVEDIGITS)
    path = '%s.%s' % (sanitize(ekey[0]), ekey[1])
    fname = dstore.export_path(path)
    md = extract(dstore, 'exposure_metadata')
    tostr = {'taxonomy': md.taxonomy}
    for tagname in md.tagnames:
        tostr[tagname] = getattr(md, tagname)
    arr = extract(dstore, 'asset_risk').array
    arefs = dstore['assetcol/asset_refs'].value
    rows = []
    lossnames = sorted(name for name in arr.dtype.names if 'loss' in name)
    perilnames = sorted(name for name in arr.dtype.names if name.upper() ==
        name)
    expnames = [name for name in arr.dtype.names if name not in md.tagnames and
        'loss' not in name and name not in perilnames and name not in 'lon lat'
        ]
    colnames = ['asset_ref'] + sorted(md.tagnames) + ['lon', 'lat'
        ] + expnames + perilnames + lossnames
    assert len(colnames) == len(arr.dtype.names) + 1
    for aref, rec in zip(arefs, arr):
        row = [aref]
        for name in colnames[1:]:
            value = rec[name]
            try:
                row.append('"%s"' % tostr[name][value])
            except KeyError:
                row.append(value)
        rows.append(row)
    writer.save(rows, fname, colnames)
    return [fname]