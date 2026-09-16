def _galaxy_loc_iter(loc_file, galaxy_dt, need_remap=False):
    if 'column' in galaxy_dt:
        dbkey_i = galaxy_dt['column'].index('dbkey')
        path_i = galaxy_dt['column'].index('path')
    else:
        dbkey_i = None
    if os.path.exists(loc_file):
        with open(loc_file) as in_handle:
            for line in in_handle:
                if line.strip() and not line.startswith('#'):
                    parts = [x.strip() for x in line.strip().split('\t')]
                    if len(parts) == 1:
                        parts = [x.strip() for x in line.strip().split(' ') if
                            x.strip()]
                        if len(parts) > 1:
                            raise IOError(
                                'Galaxy location file uses spaces instead of tabs to separate fields: %s'
                                 % loc_file)
                    if dbkey_i is not None and not need_remap:
                        dbkey = parts[dbkey_i]
                        cur_ref = parts[path_i]
                    else:
                        if parts[0] == 'index':
                            parts = parts[1:]
                        dbkey = parts[0]
                        cur_ref = parts[-1]
                    yield dbkey, cur_ref