def persist(name, value, config='/etc/sysctl.conf'):
    nlines = []
    edited = False
    value = six.text_type(value)
    with salt.utils.files.fopen(config, 'r') as ifile:
        for line in ifile:
            line = salt.utils.stringutils.to_unicode(line).rstrip('\n')
            if not line.startswith('{0}='.format(name)):
                nlines.append(line)
                continue
            else:
                key, rest = line.split('=', 1)
                if rest.startswith('"'):
                    _, rest_v, rest = rest.split('"', 2)
                elif rest.startswith("'"):
                    _, rest_v, rest = rest.split("'", 2)
                else:
                    rest_v = rest.split()[0]
                    rest = rest[len(rest_v):]
                if rest_v == value:
                    return 'Already set'
                new_line = _formatfor(key, value, config, rest)
                nlines.append(new_line)
                edited = True
    if not edited:
        nlines.append('{0}\n'.format(_formatfor(name, value, config)))
    with salt.utils.files.fopen(config, 'w+') as ofile:
        nlines = [(salt.utils.stringutils.to_str(_l) + '\n') for _l in nlines]
        ofile.writelines(nlines)
    if config != '/boot/loader.conf':
        assign(name, value)
    return 'Updated'