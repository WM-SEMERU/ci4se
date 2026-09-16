def build_job_configs(self, args):
    job_configs = {}
    components = Component.build_from_yamlfile(args['comp'])
    NAME_FACTORY.update_base_dict(args['data'])
    mktime = args['mktimefilter']
    for comp in components:
        zcut = 'zmax%i' % comp.zmax
        key = comp.make_key('{ebin_name}_{evtype_name}')
        name_keys = dict(zcut=zcut, ebin=comp.ebin_name, psftype=comp.
            evtype_name, irf_ver=NAME_FACTORY.irf_ver(), mktime=mktime,
            fullpath=True)
        outfile = NAME_FACTORY.bexpcube_sun(**name_keys)
        ltcube_sun = NAME_FACTORY.ltcube_sun(**name_keys)
        job_configs[key] = dict(infile=NAME_FACTORY.ltcube_sun(**name_keys),
            outfile=outfile, irfs=NAME_FACTORY.irfs(**name_keys), evtype=
            comp.evtype, emin=comp.emin, emax=comp.emax, enumbins=comp.
            enumbins, logfile=make_nfs_path(outfile.replace('.fits', '.log')))
    return job_configs