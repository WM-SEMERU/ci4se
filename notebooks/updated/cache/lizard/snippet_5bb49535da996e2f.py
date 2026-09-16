def parse_config(file_name='/usr/local/etc/pkg.conf'):
    ret = {}
    if not os.path.isfile(file_name):
        return 'Unable to find {0} on file system'.format(file_name)
    with salt.utils.files.fopen(file_name) as ifile:
        for line in ifile:
            line = salt.utils.stringutils.to_unicode(line)
            if line.startswith('#') or line.startswith('\n'):
                pass
            else:
                key, value = line.split('\t')
                ret[key] = value
    ret['config_file'] = file_name
    return ret