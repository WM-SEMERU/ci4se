def fstab(config='/etc/fstab'):
    ret = {}
    if not os.path.isfile(config):
        return ret
    with salt.utils.files.fopen(config) as ifile:
        for line in ifile:
            line = salt.utils.stringutils.to_unicode(line)
            try:
                if __grains__['kernel'] == 'SunOS':
                    if line[0] == '#':
                        continue
                    entry = _vfstab_entry.dict_from_line(line)
                else:
                    entry = _fstab_entry.dict_from_line(line, _fstab_entry.
                        compatibility_keys)
                entry['opts'] = entry['opts'].split(',')
                while entry['name'] in ret:
                    entry['name'] += '_'
                ret[entry.pop('name')] = entry
            except _fstab_entry.ParseError:
                pass
            except _vfstab_entry.ParseError:
                pass
    return ret