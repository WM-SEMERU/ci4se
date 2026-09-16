def _get_supported_py_config(tops, extended_cfg):
    pymap = []
    for py_ver, tops in _six.iteritems(copy.deepcopy(tops)):
        py_ver = int(py_ver)
        if py_ver == 2:
            pymap.append('py2:2:7')
        elif py_ver == 3:
            pymap.append('py3:3:0')
    for ns, cfg in _six.iteritems(copy.deepcopy(extended_cfg) or {}):
        pymap.append('{}:{}:{}'.format(ns, *cfg.get('py-version')))
    pymap.append('')
    return salt.utils.stringutils.to_bytes(os.linesep.join(pymap))