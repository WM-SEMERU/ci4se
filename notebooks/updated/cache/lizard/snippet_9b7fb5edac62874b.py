def ossos_release_parser(table=False, data_release=parameters.RELEASE_VERSION):
    names = ['cl', 'p', 'j', 'k', 'sh', 'object', 'mag', 'e_mag', 'Filt',
        'Hsur', 'dist', 'e_dist', 'Nobs', 'time', 'av_xres', 'av_yres',
        'max_x', 'max_y', 'a', 'e_a', 'e', 'e_e', 'i', 'e_i', 'Omega',
        'e_Omega', 'omega', 'e_omega', 'tperi', 'e_tperi', 'RAdeg', 'DEdeg',
        'JD', 'rate']
    if table:
        retval = Table.read(parameters.RELEASE_DETECTIONS[data_release],
            format='ascii', guess=False, delimiter=' ', data_start=0,
            comment='#', names=names, header_start=None)
    else:
        retval = []
        with open(data_release, 'r') as detectionsfile:
            for line in detectionsfile.readlines()[1:]:
                obj = TNO.from_string(line, version=parameters.
                    RELEASE_DETECTIONS[data_release])
                retval.append(obj)
    return retval