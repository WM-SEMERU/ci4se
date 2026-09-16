def get_input_files(oqparam, hazard=False):
    fnames = []
    for key in oqparam.inputs:
        fname = oqparam.inputs[key]
        if hazard and key not in ('site_model', 'source_model_logic_tree',
            'gsim_logic_tree', 'source'):
            continue
        elif key == 'gsim_logic_tree':
            gsim_lt = get_gsim_lt(oqparam)
            for gsims in gsim_lt.values.values():
                for gsim in gsims:
                    table = getattr(gsim, 'GMPE_TABLE', None)
                    if table:
                        fnames.append(table)
            fnames.append(fname)
        elif key == 'source_model':
            f = oqparam.inputs['source_model']
            fnames.append(f)
            fname = nrml.read(f).sourceModel.UCERFSource['filename']
            fnames.append(os.path.join(os.path.dirname(f), fname))
        elif key == 'exposure':
            for exp in asset.Exposure.read_headers(fname):
                fnames.extend(exp.datafiles)
            fnames.extend(fname)
        elif isinstance(fname, dict):
            fnames.extend(fname.values())
        elif isinstance(fname, list):
            for f in fname:
                if f == oqparam.input_dir:
                    raise InvalidFile('%s there is an empty path in %s' % (
                        oqparam.inputs['job_ini'], key))
            fnames.extend(fname)
        elif key == 'source_model_logic_tree':
            for smpaths in logictree.collect_info(fname).smpaths.values():
                fnames.extend(smpaths)
            fnames.append(fname)
        else:
            fnames.append(fname)
    return sorted(fnames)