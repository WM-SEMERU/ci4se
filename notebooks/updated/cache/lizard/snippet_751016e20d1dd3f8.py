def options(name, conf_file=None):
    config = _read_config(conf_file)
    section_name = 'program:{0}'.format(name)
    if section_name not in config.sections():
        raise CommandExecutionError("Process '{0}' not found".format(name))
    ret = {}
    for key, val in config.items(section_name):
        val = salt.utils.stringutils.to_num(val.split(';')[0].strip())
        if isinstance(val, string_types):
            if val.lower() == 'true':
                val = True
            elif val.lower() == 'false':
                val = False
        ret[key] = val
    return ret