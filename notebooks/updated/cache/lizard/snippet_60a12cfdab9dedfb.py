def export_hcurves_csv(ekey, dstore):
    oq = dstore['oqparam']
    info = get_info(dstore)
    rlzs_assoc = dstore['csm_info'].get_rlzs_assoc()
    R = len(rlzs_assoc.realizations)
    sitecol = dstore['sitecol']
    sitemesh = get_mesh(sitecol)
    key, kind, fmt = get_kkf(ekey)
    fnames = []
    checksum = dstore.get_attr('/', 'checksum32')
    hmap_dt = oq.hmap_dt()
    for kind in oq.get_kinds(kind, R):
        fname = hazard_curve_name(dstore, (key, fmt), kind, rlzs_assoc)
        comment = _comment(rlzs_assoc, kind, oq.investigation_time)
        if key in ('hmaps', 'uhs'
            ) and oq.uniform_hazard_spectra or oq.hazard_maps:
            hmap = extract(dstore, 'hmaps?kind=' + kind)[kind]
        if key == 'uhs' and oq.poes and oq.uniform_hazard_spectra:
            uhs_curves = calc.make_uhs(hmap, info)
            writers.write_csv(fname, util.compose_arrays(sitemesh,
                uhs_curves), comment=comment + ', checksum=%d' % checksum)
            fnames.append(fname)
        elif key == 'hmaps' and oq.poes and oq.hazard_maps:
            fnames.extend(export_hmaps_csv(ekey, fname, sitemesh, hmap.
                flatten().view(hmap_dt), comment + ', checksum=%d' % checksum))
        elif key == 'hcurves':
            hcurves = extract(dstore, 'hcurves?kind=' + kind)[kind]
            fnames.extend(export_hcurves_by_imt_csv(ekey, kind, rlzs_assoc,
                fname, sitecol, hcurves, oq, checksum))
    return sorted(fnames)