def get_assets(dstore):
    assetcol = dstore['assetcol']
    tagnames = sorted(assetcol.tagnames)
    tag = {t: getattr(assetcol.tagcol, t) for t in tagnames}
    dtlist = [('asset_ref', (bytes, 100))]
    for tagname in tagnames:
        dtlist.append((tagname, (bytes, 100)))
    dtlist.extend([('lon', F32), ('lat', F32)])
    asset_data = []
    for aref, a in zip(assetcol.asset_refs, assetcol.array):
        tup = tuple(b'"%s"' % tag[t][a[t]].encode('utf-8') for t in tagnames)
        asset_data.append((aref,) + tup + (a['lon'], a['lat']))
    return numpy.array(asset_data, dtlist)