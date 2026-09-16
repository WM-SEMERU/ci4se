def extract_uhs(dstore, what):
    info = get_info(dstore)
    if what == '':
        sitecol = dstore['sitecol']
        mesh = get_mesh(sitecol, complete=False)
        dic = {}
        for stat, s in info['stats'].items():
            hmap = dstore['hmaps-stats'][:, (s)]
            dic[stat] = calc.make_uhs(hmap, info)
        yield from hazard_items(dic, mesh, investigation_time=info[
            'investigation_time'])
        return
    params = parse(what, info)
    periods = []
    for m, imt in enumerate(info['imtls']):
        if imt == 'PGA' or imt.startswith('SA'):
            periods.append(m)
    if 'site_id' in params:
        sids = params['site_id']
    else:
        sids = ALL
    if params['rlzs']:
        dset = dstore['hmaps-rlzs']
        for k in params['k']:
            yield 'rlz-%03d' % k, hdf5.extract(dset, sids, k, periods, ALL)[:,
                (0)]
    else:
        dset = dstore['hmaps-stats']
        stats = list(info['stats'])
        for k in params['k']:
            yield stats[k], hdf5.extract(dset, sids, k, periods, ALL)[:, (0)]
    yield from params.items()