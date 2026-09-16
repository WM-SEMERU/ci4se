def build_job_configs(self, args):
    job_configs = {}
    comp_file = args.get('comp', None)
    if comp_file is not None:
        comp_dict = yaml.safe_load(open(comp_file))
        coordsys = comp_dict.pop('coordsys')
        for v in comp_dict.values():
            v['coordsys'] = coordsys
    else:
        return job_configs
    datafile = args['data']
    if datafile is None or datafile == 'None':
        return job_configs
    NAME_FACTORY.update_base_dict(args['data'])
    inputfiles = create_inputlist(args['ft1file'])
    outdir_base = os.path.join(NAME_FACTORY.base_dict['basedir'],
        'counts_cubes')
    data_ver = NAME_FACTORY.base_dict['data_ver']
    for idx, infile in enumerate(inputfiles):
        key = '%06i' % idx
        key_scfile = '%03i' % (idx + 1)
        output_dir = os.path.join(outdir_base, key)
        try:
            os.mkdir(output_dir)
        except OSError:
            pass
        scfile = args['ft2file'].replace('.lst', '_%s.fits' % key_scfile)
        logfile = make_nfs_path(os.path.join(output_dir, 
            'scatter_mk_%s_%s.log' % (data_ver, key)))
        job_configs[key] = comp_dict.copy()
        job_configs[key].update(dict(ft1file=infile, scfile=scfile, comp=
            args['comp'], hpx_order_max=args['hpx_order_max'], outdir=
            outdir_base, outkey=key, logfile=logfile, pfiles=output_dir))
    return job_configs