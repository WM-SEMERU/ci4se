def automaster(config='/etc/auto_salt'):
    ret = {}
    if not os.path.isfile(config):
        return ret
    with salt.utils.files.fopen(config) as ifile:
        for line in ifile:
            line = salt.utils.stringutils.to_unicode(line)
            if line.startswith('#'):
                continue
            if not line.strip():
                continue
            comps = line.split()
            if len(comps) != 3:
                continue
            prefix = '/..'
            name = comps[0].replace(prefix, '')
            device_fmt = comps[2].split(':')
            opts = comps[1].split(',')
            ret[name] = {'device': device_fmt[1], 'fstype': opts[0], 'opts':
                opts[1:]}
    return ret