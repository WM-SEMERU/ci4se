def read(fnames, calculation_mode='', region_constraint='',
    ignore_missing_costs=(), asset_nodes=False, check_dupl=True, tagcol=
    None, by_country=False):
    if by_country:
        prefix2cc = countries.from_exposures(os.path.basename(f) for f in
            fnames)
    else:
        prefix = ''
    allargs = []
    tagcol = _minimal_tagcol(fnames, by_country)
    for i, fname in enumerate(fnames, 1):
        if by_country and len(fnames) > 1:
            prefix = prefix2cc['E%02d_' % i] + '_'
        elif len(fnames) > 1:
            prefix = 'E%02d_' % i
        else:
            prefix = ''
        allargs.append((fname, calculation_mode, region_constraint,
            ignore_missing_costs, asset_nodes, check_dupl, prefix, tagcol))
    exp = None
    for exposure in parallel.Starmap(Exposure.read_exp, allargs, distribute
        ='no'):
        if exp is None:
            exp = exposure
            exp.description = 'Composite exposure[%d]' % len(fnames)
        else:
            assert exposure.cost_types == exp.cost_types
            assert exposure.occupancy_periods == exp.occupancy_periods
            assert exposure.insurance_limit_is_absolute == exp.insurance_limit_is_absolute
            assert exposure.retrofitted == exp.retrofitted
            assert exposure.area == exp.area
            exp.assets.extend(exposure.assets)
            exp.asset_refs.extend(exposure.asset_refs)
            exp.tagcol.extend(exposure.tagcol)
    exp.exposures = [os.path.splitext(os.path.basename(f))[0] for f in fnames]
    return exp