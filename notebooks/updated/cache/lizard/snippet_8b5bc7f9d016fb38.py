def read_tracers_h5(xdmf_file, infoname, snapshot, position):
    xdmf_root = xmlET.parse(str(xdmf_file)).getroot()
    tra = {}
    tra[infoname] = [{}, {}]
    if position:
        for axis in 'xyz':
            tra[axis] = [{}, {}]
    for elt_subdomain in xdmf_root[0][0][snapshot].findall('Grid'):
        ibk = int(elt_subdomain.get('Name').startswith('meshYang'))
        if position:
            for data_attr in elt_subdomain.findall('Geometry'):
                for data_item, axis in zip(data_attr.findall('DataItem'), 'xyz'
                    ):
                    icore, data = _get_field(xdmf_file, data_item)
                    tra[axis][ibk][icore] = data
        for data_attr in elt_subdomain.findall('Attribute'):
            if data_attr.get('Name') != infoname:
                continue
            icore, data = _get_field(xdmf_file, data_attr.find('DataItem'))
            tra[infoname][ibk][icore] = data
    for info in tra:
        tra[info] = [trab for trab in tra[info] if trab]
        for iblk, trab in enumerate(tra[info]):
            tra[info][iblk] = np.concatenate([trab[icore] for icore in
                range(len(trab))])
    return tra