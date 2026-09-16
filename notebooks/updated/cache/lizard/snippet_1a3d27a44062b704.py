def py_str2float(version):
    if version.endswith('pypy'):
        version = version[:-len('pypy')]
    if version in magics:
        magic = magics[version]
        for v, m in list(magics.items()):
            if m == magic:
                try:
                    return float(canonic_python_version[v])
                except:
                    try:
                        m = re.match('^(\\d\\.)(\\d+)\\.(\\d+)$', v)
                        if m:
                            return float(m.group(1) + m.group(2))
                    except:
                        pass
                    pass
                pass
            pass
    raise RuntimeError("Can't find a valid Python version for version %s" %
        version)
    return