def _parse_conf(conf_file=default_conf):
    ret = {}
    with salt.utils.files.fopen(conf_file, 'r') as ifile:
        for line in ifile:
            line = salt.utils.stringutils.to_unicode(line).strip()
            if not line:
                continue
            if line.startswith('#'):
                continue
            splitline = line.split(' ', 1)
            ret[splitline[0]] = splitline[1]
    return ret